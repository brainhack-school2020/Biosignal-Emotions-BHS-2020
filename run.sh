#!/bin/bash

echo "Preprocessing the DREAMER Dataset (EEG only) ..."
python DREAMER_main.py preprocessing Data/DREAMER.mat eeg DREAMER_features_eeg.csv --Add_Target_Emotion anger --Add_Target_Emotion fear --Add_Target_Emotion calmness
echo "Success. The output was saved in DREAMER_features_eeg.csv"
echo "Evaluation of the performance of classifiers (EEG only) ..."
python DREAMER_main.py classification DREAMER_features_eeg.csv eeg DREAMER_classification_eeg.csv
echo "Success. The output was saved in DREAMER_classification_eeg.csv"


echo "Preprocessing the DREAMER Dataset (ECG only) ..."
python DREAMER_main.py preprocessing Data/DREAMER.mat ecg DREAMER_features_ecg.csv --Add_Target_Emotion anger --Add_Target_Emotion fear --Add_Target_Emotion calmness
echo "Success. The output was saved in DREAMER_features_ecg.csv"
echo "Evaluation of the performance of classifiers (ECG only) ..."
python DREAMER_main.py classification DREAMER_features_ecg.csv ecg DREAMER_classification_ecg.csv
echo "Success. The output was saved in DREAMER_classification_ecg.csv"


echo "Preprocessing the DREAMER Dataset (both EEG and ECG) ..."
python DREAMER_main.py preprocessing Data/DREAMER.mat both DREAMER_features_both.csv --Add_Target_Emotion anger --Add_Target_Emotion fear --Add_Target_Emotion calmness
echo "Success. The output was saved in DREAMER_features_both.csv"
echo "Evaluation of the performance of classifiers (both EEG and ECG) ..."
python DREAMER_main.py classification DREAMER_features_both.csv both DREAMER_classification_both.csv
echo "Success. The output was saved in DREAMER_classification_both.csv"
