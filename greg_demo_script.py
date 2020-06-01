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


def preprocessing_and_feature_extraction_ECG(file_name_csv,raw):
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


def feature_extraction_EEG(file_name_csv,raw):
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
    EEG.to_csv(file_name_csv)
    return EEG


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


def driver():
    description = "Biosignal Emotions project BHS 2020."
    parser = ArgumentParser(__file__, description)
    parser.add_argument("dreamer_matfile", action="store",
                        help="Path to raw data mat file, i.e. DREAMER.mat.")
    parser.add_argument("dreamer_eeg_csv", action="store",
                        help="")
    parser.add_argument("threshold", action="store", default=0.4, type=float,
                        help="")
    parser.add_argument("mode", action="store",
                        choices=["process", "store", "deleteeverything"],
                        default="process",
                        help="")
    parser.add_argument("--n_datapoints", "-n", action="store", type=int,
                        help="number of datapoints")
    parser.add_argument("--crash", "-q", action="store_true")

    results = parser.parse_args()

    raw = sio.loadmat(results.dreamer_matfile)

    df_ECG = preprocessing_and_feature_extraction_ECG('DREAMER_Extracted_EEG.csv', raw)
    # print(df_ECG.head())

    df_EEG = feature_extraction_EEG('DREAMER_Extracted_EEG.csv', raw)
    # print(df_EEG.head())

    last_four_secs_EEG = feature_extraction_EEG_end_baseline('Extracted_EEG_last4s.csv', raw, 4)
    # print(last_four_secs_EEG.head())

    # load features extracted from preprocessed EEG and ECG data
    path_EEG='DREAMER_Extracted_EEG.csv'
    path_ECG='DREAMER_Extracted_ECG.csv'
    data_EEG=pd.read_csv(path_EEG).drop(['Unnamed: 0'],axis=1)
    data_ECG=pd.read_csv(path_ECG).drop(['Unnamed: 0'],axis=1)
    # load mat file containing raw biosignal, emotion, participant, and video data
    raw=sio.loadmat(results.dreamer_matfile)

    # create new dataframe with emotion, participant, and video data
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
            a[participant,video,6]=raw['DREAMER'][0,0]['Data'][0,participant]['ScoreValence'][0,0][video,0]
            a[participant,video,7]=raw['DREAMER'][0,0]['Data'][0,participant]['ScoreArousal'][0,0][video,0]
            a[participant,video,8]=raw['DREAMER'][0,0]['Data'][0,participant]['ScoreDominance'][0,0][video,0]
    b=pd.DataFrame(a.reshape((23*18,a.shape[2])),columns=['Age','Gender','Participant','Video','Video_Name','Target_Emotion','Valence','Arousal','Dominance'])
    # combine feature extraction dataframes with the new dataframe
    all_data=pd.concat([data_EEG,data_ECG,b],axis=1)
    print(all_data.head())
    all_data.to_csv('DREAMER_Preprocessed_NotTransformed_NotThresholded.csv')

    All_Features = pd.read_csv("DREAMER_Preprocessed_NotTransformed_NotThresholded.csv")
    del All_Features['Unnamed: 0']
    Last4s_EEG_Features = pd.read_csv('Extracted_EEG_last4s.csv')
    del Last4s_EEG_Features['Unnamed: 0']
    for column in All_Features.columns:
        if not(All_Features[column].dtype == np.object):
            All_Features[column]=(All_Features[column]-np.min(All_Features[column]))/(np.max(All_Features[column])-np.min(All_Features[column]))
    for column in Last4s_EEG_Features.columns:
        if not(Last4s_EEG_Features[column].dtype == np.object):
            Last4s_EEG_Features[column]=(Last4s_EEG_Features[column]-np.min(Last4s_EEG_Features[column]))/(np.max(Last4s_EEG_Features[column])-np.min(Last4s_EEG_Features[column]))


# main scripting details could go here
if __name__ == "__main__":
    driver()

