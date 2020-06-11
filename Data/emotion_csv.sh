#!/bin/bash

echo "activate virtual environment (which I called bioemo)"
cd ..
source bioemo/bin/activate

echo "loading emotion data as saving as csv"
cd Data
python3 load_emotion_data.py --dreamer_matfile="DREAMER.mat" --csv_name="emotion_data.csv"
