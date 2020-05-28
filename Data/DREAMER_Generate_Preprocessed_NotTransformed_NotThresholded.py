# import necessary libraries
import scipy.io as sio
import numpy as np
import pandas as pd

# load features extracted from preprocessed EEG and ECG data
path_EEG='DREAMER_Extracted_EEG.csv'
path_ECG='DREAMER_Extracted_ECG.csv'
data_EEG=pd.read_csv(path_EEG).drop(['Unnamed: 0'],axis=1)
data_ECG=pd.read_csv(path_ECG).drop(['Unnamed: 0'],axis=1)
# load mat file containing raw biosignal, emotion, participant, and video data
data=sio.loadmat('DREAMER.mat')

# create new dataframe with emotion, participant, and video data
a=np.zeros((23,18,9),dtype=object)
for participant in range(0,23):
    for video in range(0,18):
        a[participant,video,0]=data['DREAMER'][0,0]['Data'][0,participant]['Age'][0][0][0]
        a[participant,video,1]=data['DREAMER'][0,0]['Data'][0,participant]['Gender'][0][0][0]
        a[participant,video,2]=participant+1
        a[participant,video,3]=video+1
        a[participant,video,4]=['Searching for Bobby Fischer','D.O.A.', 'The Hangover', 'The Ring', '300',
                  'National Lampoon\'s VanWilder', 'Wall-E', 'Crash', 'My Girl', 'The Fly',
                  'Pride and Prejudice', 'Modern Times', 'Remember the Titans', 'Gentlemans Agreement',
                  'Psycho', 'The Bourne Identitiy', 'The Shawshank Redemption', 'The Departed'][video]
        a[participant,video,5]=['calmness', 'surprise', 'amusement', 'fear', 'excitement', 'disgust',
                  'happiness', 'anger', 'sadness', 'disgust', 'calmness', 'amusement',
                  'happiness', 'anger', 'fear', 'excitement', 'sadness', 'surprise'][video]
        a[participant,video,6]=data['DREAMER'][0,0]['Data'][0,participant]['ScoreValence'][0,0][video,0]
        a[participant,video,7]=data['DREAMER'][0,0]['Data'][0,participant]['ScoreArousal'][0,0][video,0]
        a[participant,video,8]=data['DREAMER'][0,0]['Data'][0,participant]['ScoreDominance'][0,0][video,0]
b=pd.DataFrame(a.reshape((23*18,a.shape[2])),columns=['Age','Gender','Participant','Video','Video_Name','Target_Emotion','Valence','Arousal','Dominance'])
# combine feature extraction dataframes with the new dataframe
all_data=pd.concat([data_EEG,data_ECG,b],axis=1)
print(all_data.head())
all_data.to_csv('DREAMER_Preprocessed_NotTransformed_NotThresholded.csv')
