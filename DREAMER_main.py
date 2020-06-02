#!/usr/bin/env python
# "shebang"

# If you call a script with:
#   python my_script.py
#       the shebang doesn't matter

#  ./my_script.py  (similar to executing a bash script)
#       therefore, always use one, it doesn't hurt anybody

from sklearn import preprocessing as pre
from argparse import ArgumentParser
from scipy import signal

import matplotlib
matplotlib.use('agg')

import scipy.io as sio
import neurokit2 as nk
import pandas as pd
import numpy as np
import math

# Checklist :
#   preprocessing_and_feature_extraction_EEG(raw)
#   preprocessing_and_feature_extraction_ECG(raw)
#   preprocessing_and_feature_extraction_EEG_baseline(raw,seconds)
#   preprocessing_and_feature_extraction_ECG_baseline(raw,seconds min=40)

# EEG Feature Extraction : feature_extraction_EEG
def preprocessing_and_feature_extraction_EEG(raw):#(file_name_csv,raw):
    EEG_tmp=np.zeros((23,18,42))
    for participant in range(0,23):
        for video in range(0,18):
            for i in range(0,14):
                B,S=[],[]
                basl=raw['DREAMER'][0,0]['Data'][0,participant]['EEG'][0,0]['baseline'][0,0][video,0][:,i]
                stim=raw['DREAMER'][0,0]['Data'][0,participant]['EEG'][0,0]['stimuli'][0,0][video,0][:,i]
                B=preprocessing(basl,B)
                S=preprocessing(stim,S)
                Extrod=np.divide(S,B)
                EEG_tmp[participant,video,3*i]=Extrod[0]
                EEG_tmp[participant,video,3*i+1]=Extrod[1]
                EEG_tmp[participant,video,3*i+2]=Extrod[2]
    col=[]
    for i in range(0,14):
        col.append('psdtheta_'+str(i + 1)+'_un')
        col.append('psdalpha_'+str(i + 1)+'_un')
        col.append('psdbeta_'+str(i + 1)+'_un')
    EEG=pd.DataFrame(EEG_tmp.reshape((23 * 18,EEG_tmp.shape[2])),columns=col)
    scaler=pre.StandardScaler()
    for i in range(len(col)):
        EEG[col[i][:-3]]=scaler.fit_transform(EEG[[col[i]]])
    EEG.drop(col,axis=1,inplace=True)
    # EEG.to_csv(file_name_csv) # We decided not to use CSV files
    return EEG

def preprocessing_and_feature_extraction_ECG(raw):#(file_name_csv,raw):
    data_ECG={}
    for participant in range(0,23):
        for video in range(0,18):
            # load raw baseline and stimuli data for left and right
            basl_l=raw['DREAMER'][0,0]['Data'][0,participant]['ECG'][0,0]['baseline'][0,0][video,0][:,0]
            stim_l=raw['DREAMER'][0,0]['Data'][0,participant]['ECG'][0,0]['stimuli'][0,0][video,0][:,0]
            basl_r=raw['DREAMER'][0,0]['Data'][0,participant]['ECG'][0,0]['baseline'][0,0][video,0][:,1]
            stim_r=raw['DREAMER'][0,0]['Data'][0,participant]['ECG'][0,0]['stimuli'][0,0][video,0][:,1]
            # process with neurokit
            ecg_signals_b_l,info_b_l=nk.ecg_process(basl_l,sampling_rate=256)
            ecg_signals_s_l,info_s_l=nk.ecg_process(stim_l,sampling_rate=256)
            ecg_signals_b_r,info_b_r=nk.ecg_process(basl_r,sampling_rate=256)
            ecg_signals_s_r,info_s_r=nk.ecg_process(stim_r,sampling_rate=256)
            # divide stimuli features by baseline features
            # would be interesting to compare classification accuracy when we
            # don't do this
            features_ecg_l=nk.ecg_intervalrelated(ecg_signals_s_l)/nk.ecg_intervalrelated(ecg_signals_b_l)
            features_ecg_r=nk.ecg_intervalrelated(ecg_signals_s_r)/nk.ecg_intervalrelated(ecg_signals_b_r)
            # average left and right features
            # would be interesting to compare classification accuracy when we
            # rather include both left and right features
            features_ecg=(features_ecg_l+features_ecg_r)/2
            if not len(data_ECG):
                data_ECG=features_ecg
            else:
                data_ECG=pd.concat([data_ECG,features_ecg],ignore_index=True)
    return data_ECG


def preprocessing(raw, feature):
    overall=signal.firwin(9,[0.0625,0.46875],window='hamming')
    theta=signal.firwin(9,[0.0625,0.125],window='hamming')
    alpha=signal.firwin(9,[0.125,0.203125],window='hamming')
    beta=signal.firwin(9,[0.203125,0.46875],window='hamming')
    filtedData=signal.filtfilt(overall,1,raw)
    filtedtheta=signal.filtfilt(theta,1,filtedData)
    filtedalpha=signal.filtfilt(alpha,1,filtedData)
    filtedbeta=signal.filtfilt(beta,1,filtedData)
    ftheta,psdtheta=signal.welch(filtedtheta,nperseg=256)
    falpha,psdalpha=signal.welch(filtedalpha,nperseg=256)
    fbeta,psdbeta=signal.welch(filtedbeta,nperseg=256)
    feature.append(max(psdtheta))
    feature.append(max(psdalpha))
    feature.append(max(psdbeta))
    return feature





def feature_extraction_EEG_end_baseline(file_name_csv,raw,secs):
    # 128 Hz is the sampling rate for the EEG data
    fs_EEG = 128
    N_EEG = math.ceil(fs_EEG*secs)
    EEG_tmp=np.zeros((23,18,42))
    for participant in range(0,23):
        for video in range(0,18):
            for i in range(0,14):
                B,S=[],[]
                basl=raw['DREAMER'][0,0]['Data'][0,participant]['EEG'][0,0]['baseline'][0,0][video,0][-1-N_EEG:-1,i]
                Extrod=preprocessing(basl,B)
                EEG_tmp[participant,video,3*i]=Extrod[0]
                EEG_tmp[participant,video,3*i+1]=Extrod[1]
                EEG_tmp[participant,video,3*i+2]=Extrod[2]
    col=[]
    for i in range(0,14):
        col.append('psdtheta_'+str(i + 1)+'_un')
        col.append('psdalpha_'+str(i + 1)+'_un')
        col.append('psdbeta_'+str(i + 1)+'_un')
    EEG=pd.DataFrame(EEG_tmp.reshape((23 * 18,EEG_tmp.shape[2])),columns=col)
    scaler=pre.StandardScaler()
    for i in range(len(col)):
        EEG[col[i][:-3]]=scaler.fit_transform(EEG[[col[i]]])
    EEG.drop(col,axis=1,inplace=True)
    EEG.to_csv(file_name_csv)
    return EEG

def Participants_Data(raw):
    # Create new dataframe with emotion, participant, and video data
    a=np.zeros((23,18,9),dtype=object)
    for participant in range(0,23):
        for video in range(0,18):
            a[participant,video,0]=raw['DREAMER'][0,0]['Data'][0,participant]['Age'][0][0][0]
            a[participant,video,1]=raw['DREAMER'][0,0]['Data'][0,participant]['Gender'][0][0][0]
            a[participant,video,2]=participant+1
            a[participant,video,3]=video+1
            a[participant,video,4]=['Searching for Bobby Fischer','D.O.A.', 'The Hangover', 'The Ring', '300',
                      'National Lampoon\'s VanWilder', 'Wall-E', 'Crash', 'My Girl', 'The Fly',
                      'Pride and Prejudice', 'Modern Times', 'Remember the Titans', 'Gentlemans Agreement',
                      'Psycho', 'The Bourne Identitiy', 'The Shawshank Redemption', 'The Departed'][video]
            a[participant,video,5]=['calmness', 'surprise', 'amusement', 'fear', 'excitement', 'disgust',
                      'happiness', 'anger', 'sadness', 'disgust', 'calmness', 'amusement',
                      'happiness', 'anger', 'fear', 'excitement', 'sadness', 'surprise'][video]
            a[participant,video,6]=raw['DREAMER'][0,0]['Data'][0,participant]['ScoreValence'][0,0][video,0].astype(float)
            a[participant,video,7]=raw['DREAMER'][0,0]['Data'][0,participant]['ScoreArousal'][0,0][video,0].astype(float)
            a[participant,video,8]=raw['DREAMER'][0,0]['Data'][0,participant]['ScoreDominance'][0,0][video,0].astype(float)
    b=pd.DataFrame(a.reshape((23*18,a.shape[2])),columns=['Age','Gender','Participant','Video','Video_Name','Target_Emotion','Valence','Arousal','Dominance'])
    ## combine feature extraction dataframes with the new dataframe
    #all_data=pd.concat([data_EEG,data_ECG,b],axis=1)
    return b

def minmax(df):
    for column in df.columns:
            if (((df[column].dtype == np.int64) or (df[column].dtype == np.float_)) or (column=='Valence' or column=='Arousal' or column=='Dominance') and not(column=="Video")):#if not(df[column].dtype == np.object) and not(column=="Video"): # : Fails for integers
                if not((np.max(df[column])-np.min(df[column]))==0):
                    df[column]=(df[column]-np.min(df[column]))/(np.max(df[column])-np.min(df[column]))
    return df

def driver():
    # Description
    description = "Biosignal Emotions project BHS 2020 \n usage : DREAMER_main.py <dreamer_matfile> <Biosignal_Option> <Biosignal_Processing_Function> [--Emotion_Option <emotion>] [--Add_Target_Emotion <target>] \n example : DREAMER_main.py Data/DREAMER.mat eeg --Add_Target_Emotion Disgust --Add_Target_Emotion Fear"
    parser = ArgumentParser(__file__, description)
    # Input files :
    parser.add_argument("dreamer_matfile",action="store",
                        help="Path/Name to raw data .mat file : DREAMER.mat")
    # Biosignal options: EEG, ECG, or both
    parser.add_argument("Biosignal_Option",action="store",choices=["eeg", "ecg", "both"],default="both",help="Biosignal option : 'eeg', 'ecg', or 'both'")
    # Biosignal processing options: whether to divide by the baseline, minmax scaling
    parser.add_argument("--Scaling_Option", action="store",
                        choices=["minmax","none"],
                        default="minmax",
                        help="Scaling option for all the features : minmax (default), none")
    # Emotion options: valence, arousal, thresholded valence/arousal after minmax scaling per participant
    parser.add_argument("--Emotion_Option", action="store", choices=["1","2","3","4"], default="1", help="Emotion options:  1 : Valence_High and Arousal_High \t 2 : Valence_High and Arousal_Low \t 3 : Valence_Low and Arousal_High \t 4 : Valence_Low and Arousal_Low")
    # target emotion (all target emotions, just disgust and anger vs. calmness).
    # the options chosen for each should be listed in columns of the output dataframe
    parser.add_argument("--Add_Target_Emotion", dest="Target_Emotions", action="append", help="Add a target emotion : All, Amusement,Excitement, Happiness, Calmness, Anger, Disgust, Fear, Sadness, Surprise")#choices=["All", "Amusement","Excitement", "Happiness", "Calmness", "Anger", "Disgust", "Fear", "Sadness", "Surprise"], default="All", help="Target emotions (list) : All, Amusement,Excitement, Happiness, Calmness, Anger, Disgust, Fear, Sadness, Surprise")
    # --- Execute the parsing ---
    results = parser.parse_args()
    # --- Create a DataFrame containing the parsing summary
    # --- Convert the Argparse's namespace to a dictionary via vars( ) and convert the resulting dictionary into a DataFrame via pd.DataFrame( )
    df_Configuration = pd.DataFrame(vars(results))
    print("Configuration DataFrame:")
    print(df_Configuration)
    # Load the .MAT file
    print("Loading "+str(results.dreamer_matfile)+" ...")
    raw = sio.loadmat(results.dreamer_matfile)
    print("Success")
    


    ### Processing pipeline :
    ## 1. Create a DataFrame containing the Features, according to the user choice for Biosignals (eeg,ecg,both)
    df_Features=pd.DataFrame()
    if results.Biosignal_Option=="eeg":
        print("Creating a DataFrame containing the Features for EEG only ... (This may take a few minutes)")
        df_Features = preprocessing_and_feature_extraction_EEG(raw)
        print("Success")
        #print(df_Features)
        #return df_Features
    elif results.Biosignal_Option=="ecg":
        print("Creating a DataFrame containing the Features for ECG only ... (This may take a few hours)")
        df_Features = preprocessing_and_feature_extraction_ECG(raw)
        print("Success")
        #return df_Features
    elif results.Biosignal_Option=="both":
        print("Creating a DataFrame containing the Features for EEG and ECG ... (This may take a few hours)")
        df_EEG = preprocessing_and_feature_extraction_EEG(raw)
        df_ECG = preprocessing_and_feature_extraction_ECG(raw)
        df_Features = pd.concat([df_EEG, df_ECG], axis=1)
        print("Success")
        #return df_Features
    print(df_Features)
    ## 2. Add Participant's data :
    print("Reading Participant's data ...")
    df_Participants_Data = Participants_Data(raw)
    print("Success")
    print("Concatenating Participant's data into the Features DataFrama")
    df_Features = pd.concat([df_Features,df_Participants_Data],axis=1)
    print("Success")
    ## 3. Scaling of all numerical data : minmax (default)
    if(results.Scaling_Option=="minmax"):
        print("Scaling (minmax) ...")
        df_Features=minmax(df_Features)
        print("Success")
    else:
        print("No scaling. Skipping this step.")
    print(df_Features)
    return df_Features

# Main scripting details
if __name__ == "__main__":
    # Step 1 : Preprocessing
    df_Features = driver()
    # Step 2 : Machine Learning (TODO)