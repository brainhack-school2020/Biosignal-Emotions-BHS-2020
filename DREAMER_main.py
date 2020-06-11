#!/usr/bin/env python

""" Imports for the Preprocessing module """
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

""" Imports for the Machine Learning module """

from sklearn.model_selection import RandomizedSearchCV
from sklearn.model_selection import GroupKFold
from sklearn.linear_model import SGDClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.gaussian_process.kernels import RBF
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
from sklearn.pipeline import make_pipeline
from sklearn.metrics import plot_roc_curve
from sklearn.metrics import auc
from matplotlib.patches import Patch
from scipy.stats import uniform
from sklearn import svm
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import time

""" Functions for the Preprocessing module """

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

""" Functions for the Machine Learning module """

def CSVtoDataFrame(url = 'https://raw.githubusercontent.com/brainhack-school2020/Biosignal-Emotions-BHS-2020/master/Data/DREAMER_Preprocessed_NotTransformed_NotThresholded.csv'):
    df = pd.read_csv(url, sep=',', index_col=0)
    return df

def SelectTargetEmotions(df,TargetEmotionsList=pd.DataFrame()):
    # TargetEmotionsList not used for now, but can be used in something like : for emotion in TargetEmotionsList: data = df.loc[df['Target_Emotion']==emotion].copy() and append in axis=1
    data = df.loc[(df['Target_Emotion'] == 'anger') | (df['Target_Emotion'] == 'fear') | (df['Target_Emotion'] == 'calmness')].copy()
    data['Stress_bin'] = data['Target_Emotion'].map({'anger': 1, 'fear': 1, 'calmness': 0})
    return data

def BuildKFold(data,n=10,features=pd.DataFrame(),Biosignal_Option='both'):
    # features not used for now, but can be used in something like : for feature in features: X = datal.loc[:,feature].to_numpy()
    group_kfold = GroupKFold(n_splits=n)
    if Biosignal_Option=='eeg':
        X = data.loc[:,'psdtheta_1':'psdbeta_14'].to_numpy()
    elif Biosignal_Option=='ecg':
        X = data.loc[:,'Rate_Mean':'SampEn'].to_numpy()
    elif Biosignal_Option=='both':
        X = data.loc[:,'psdtheta_1':'SampEn'].to_numpy()
    y = data['Stress_bin'].to_numpy()
    groups = data['Participant'].to_numpy()
    for train_index, test_index in group_kfold.split(X, y, groups):
        X_train, X_test = X[train_index], X[test_index]
        y_train, y_test = y[train_index], y[test_index]
    return X, y, groups, X_test, y_test

def run_clf(clf,X,y,groups,X_test, y_test):
  cv = GroupKFold(n_splits=10)
  tprs = []
  aucs = []
  score = []
  runtime = []
  mean_fpr = np.linspace(0, 1, 100)
  fig, ax = plt.subplots()
  for fold, (train, test) in enumerate(cv.split(X, y, groups)):
      clf.fit(X[train], y[train])
      start = time.time()
      score.append(clf.score(X_test, y_test))
      runtime.append(time.time() - start)
      """ viz = plot_roc_curve(clf, X[test], y[test],
                          name='ROC fold {}'.format(fold+1),
                          alpha=0.3, lw=1, ax=ax) 
      interp_tpr = np.interp(mean_fpr, viz.fpr, viz.tpr)
      interp_tpr[0] = 0.0
      tprs.append(interp_tpr)
      aucs.append(viz.roc_auc)
      ax.plot([0, 1], [0, 1], linestyle='--', lw=2, color='r',
          label='Chance', alpha=.8) 
  mean_tpr = np.mean(tprs, axis=0)
  mean_tpr[-1] = 1.0
  mean_auc = auc(mean_fpr, mean_tpr)
  std_auc = np.std(aucs)
  ax.plot(mean_fpr, mean_tpr, color='b',
          label=r'Mean ROC (AUC = %0.2f $\pm$ %0.2f)' % (mean_auc, std_auc),
          lw=2, alpha=.8) 
  std_tpr = np.std(tprs, axis=0)
  tprs_upper = np.minimum(mean_tpr + std_tpr, 1)
  tprs_lower = np.maximum(mean_tpr - std_tpr, 0)
  ax.fill_between(mean_fpr, tprs_lower, tprs_upper, color='grey', alpha=.2,
                  label=r'$\pm$ 1 std. dev.') """
  """ ax.set(xlim=[-0.05, 1.05], ylim=[-0.05, 1.05],
        title="Receiver operating characteristic")
  ax.legend(loc="lower right")
  plt.show()""" # Replace the Notebook plots by saving .eps files maybe
  return score, runtime

""" Main function """

def driver():
    # Description
    description = "DREAMER_main.py [--help] \n usage (preprocessing): DREAMER_main.py preprocessing <dreamer_matfile> <Biosignal_Option> [--Emotion_Option <emotion>] [--Add_Target_Emotion <target>] \n example :  DREAMER_main.py preprocessing Data/DREAMER.mat eeg --Add_Target_Emotion Disgust --Add_Target_Emotion Fear --Emotion_Option 2 \n usage (classification): DREAMER_main.py classification <features_csv_file> \n example : DREAMER_main.py classification https://raw.githubusercontent.com/brainhack-school2020/Biosignal-Emotions-BHS-2020/master/Data/DREAMER_Preprocessed_NotTransformed_NotThresholded.csv"
    parser = ArgumentParser(__file__, description)
    parser.add_argument("user_request", action="store", nargs = '*', help="Action to execute : 'preprocessing' or 'classification'")
    # Input files :
    parser.add_argument("--dreamer_matfile",action="store", help="Path/Name to raw data .mat file : DREAMER.mat")
    # Biosignal options: EEG, ECG, or both
    parser.add_argument("--Biosignal_Option",action="store",choices=["eeg", "ecg", "both"],default="both",help="Biosignal option : 'eeg', 'ecg', or 'both'")
    # Biosignal processing options: whether to divide by the baseline, minmax scaling
    parser.add_argument("--Scaling_Option", action="store",choices=["minmax","none"],default="minmax",help="Scaling option for all the features : minmax (default), none")
    # Emotion options: valence, arousal, thresholded valence/arousal after minmax scaling per participant
    parser.add_argument("--Emotion_Option", action="store", choices=["1","2","3","4"], default="1", help="Emotion options:  1 : Valence_High and Arousal_High \t 2 : Valence_High and Arousal_Low \t 3 : Valence_Low and Arousal_High \t 4 : Valence_Low and Arousal_Low")
    # target emotion (all target emotions, just disgust and anger vs. calmness).
    # the options chosen for each should be listed in columns of the output dataframe
    parser.add_argument("--Add_Target_Emotion", dest="Target_Emotions", action="append", help="Add a target emotion : All, Amusement,Excitement, Happiness, Calmness, Anger, Disgust, Fear, Sadness, Surprise")#choices=["All", "Amusement","Excitement", "Happiness", "Calmness", "Anger", "Disgust", "Fear", "Sadness", "Surprise"], default="All", help="Target emotions (list) : All, Amusement,Excitement, Happiness, Calmness, Anger, Disgust, Fear, Sadness, Surprise")
    # --- Execute the parsing ---
    results = parser.parse_args()
    

    action=results.user_request[0]

    if(action=="preprocessing"):
        results.dreamer_matfile = results.user_request[1]
        results.Biosignal_Option = results.user_request[2]
        output_filename = results.user_request[3]
        del results.user_request
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
        elif results.Biosignal_Option=="ecg":
            print("Creating a DataFrame containing the Features for ECG only ... (This may take a few hours)")
            df_Features = preprocessing_and_feature_extraction_ECG(raw)
            print("Success")
        elif results.Biosignal_Option=="both":
            print("Creating a DataFrame containing the Features for EEG and ECG ... (This may take a few hours)")
            df_EEG = preprocessing_and_feature_extraction_EEG(raw)
            df_ECG = preprocessing_and_feature_extraction_ECG(raw)
            df_Features = pd.concat([df_EEG, df_ECG], axis=1)
            print("Success")
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
        return df_Features, action, output_filename
    elif(action=="classification"):  

        url = results.user_request[1]
        Classification_Biosignal_Option = results.user_request[2]
        output_filename = results.user_request[3]

        del results.user_request

        Results = [] # Achraf : I renamed your previous "results" into "Results" because there is a conflict between it and the argparser's results
        names = ["Nearest Neighbors", "Linear SVM", "RBF SVM", "Gaussian Process",
                "Decision Tree", "Random Forest", "Neural Net", "AdaBoost",
                "Naive Bayes"]
        classifiers = [
            KNeighborsClassifier(3),
            SVC(kernel="linear", C=0.025),
            SVC(gamma=2, C=1),
            GaussianProcessClassifier(1.0 * RBF(1.0)),
            DecisionTreeClassifier(max_depth=5),
            RandomForestClassifier(max_depth=5, n_estimators=10, max_features=1),
            MLPClassifier(alpha=1, max_iter=1000),
            AdaBoostClassifier(),
            GaussianNB()]
        for name, classifier in zip(names, classifiers):
            clf = make_pipeline(MinMaxScaler(), classifier)
            df = CSVtoDataFrame(url) # 'https://raw.githubusercontent.com/brainhack-school2020/Biosignal-Emotions-BHS-2020/master/Data/DREAMER_Preprocessed_NotTransformed_NotThresholded.csv'
            data = SelectTargetEmotions(df)
            X,y,groups,X_test, y_test = BuildKFold(data,Biosignal_Option=Classification_Biosignal_Option)
            score, runtime = run_clf(clf,X,y,groups,X_test, y_test)
            Results.append(['Name', name, 'Mean_Score', np.mean(score), 'Mean_Runtime', np.mean(runtime)])
            print(['Name', name, 'Mean_Score', np.mean(score), 'Mean_Runtime', np.mean(runtime)])
        return pd.DataFrame(Results), action, output_filename # TODO : Convert correctly Results into a valid DataFrame (for now the output is imperfect : one would need to convert Results as a Dictionary then as a DataFrame)

# Main scripting details
if __name__ == "__main__":
    df, action, output_filename = driver()
    if action=="preprocessing" and not(df.empty):
        df.to_csv(output_filename) #df.to_csv("DREAMER_features.csv")
    elif action=="classification" and not(df.empty):
        df.to_csv(output_filename) #df.to_csv("DREAMER_classification.csv")
