#!/usr/bin/env python
from argparse import ArgumentParser
import scipy.io as sio
import pandas as pd
import numpy as np

def participant_emotion(raw):
    a = np.zeros((23, 18, 9), dtype=object)
    for participant in range(0, 23):
        for video in range(0, 18):
            a[participant, video,
              0] = raw["DREAMER"][0, 0]["Data"][0, participant]["Age"][0][0][0]
            a[participant, video,
              1] = raw["DREAMER"][0, 0]["Data"][0,
                                                participant]["Gender"][0][0][0]
            a[participant, video, 2] = int(participant + 1)
            a[participant, video, 3] = int(video + 1)
            a[participant, video, 4] = [
                "Searching for Bobby Fischer",
                "D.O.A.",
                "The Hangover",
                "The Ring",
                "300",
                "National Lampoon's VanWilder",
                "Wall-E",
                "Crash",
                "My Girl",
                "The Fly",
                "Pride and Prejudice",
                "Modern Times",
                "Remember the Titans",
                "Gentlemans Agreement",
                "Psycho",
                "The Bourne Identitiy",
                "The Shawshank Redemption",
                "The Departed",
            ][video]
            a[participant, video, 5] = [
                "calmness",
                "surprise",
                "amusement",
                "fear",
                "excitement",
                "disgust",
                "happiness",
                "anger",
                "sadness",
                "disgust",
                "calmness",
                "amusement",
                "happiness",
                "anger",
                "fear",
                "excitement",
                "sadness",
                "surprise",
            ][video]
            a[participant, video, 6] = int(raw["DREAMER"][0, 0]["Data"][
                0, participant]["ScoreValence"][0, 0][video, 0])
            a[participant, video, 7] = int(raw["DREAMER"][0, 0]["Data"][
                0, participant]["ScoreArousal"][0, 0][video, 0])
            a[participant, video, 8] = int(raw["DREAMER"][0, 0]["Data"][
                0, participant]["ScoreDominance"][0, 0][video, 0])
    b = pd.DataFrame(
        a.reshape((23 * 18, a.shape[2])),
        columns=[
            "age",
            "gender",
            "participant",
            "video",
            "video_name",
            "target_emotion",
            "valence",
            "arousal",
            "dominance",
        ],
    )
    return b

def driver():
    # Description
    description = "Loads emotion data from .mat file"
    parser = ArgumentParser(__file__, description)
    parser.add_argument("--dreamer_matfile", action="store", 
                        help="Path to raw data .mat file: DREAMER.mat")
    parser.add_argument("--csv_name", "-n", action="store",
                        help="filename for the csv, if not empty will save as csv")
    results = parser.parse_args()
    raw = sio.loadmat(results.dreamer_matfile)
    df_emotion = participant_emotion(raw)
    if results.csv_name:
        df_emotion.to_csv(results.csv_name)
    return df_emotion
                    
if __name__ == "__main__":
    df_emotion = driver()
