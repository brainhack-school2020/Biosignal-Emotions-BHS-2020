#!/bin/bash

echo "activate virtual environment (called bioemo on my machine)"
source ../bioemo/bin/activate

echo "loading emotion data and saving as csv"
python load_emotion_data.py --dreamer_matfile="DREAMER.mat" --csv_name="emotion_data.csv"