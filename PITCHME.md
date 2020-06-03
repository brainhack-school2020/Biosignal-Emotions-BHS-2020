### Biosignal processing for automatic emotion recognition

#### by the Effective Affective Team 
##### AKA Danielle & Achraf
<sup><sub>Made with GitPitch (thank you Agah!)</sub></sup>

<sup><sub> Link to this presentation :
  
  https://gitpitch.com/brainhack-school2020/Biosignal-Emotions-BHS-2020 </sub></sup>

---

# Punchline !


---

## Outline 

1. Project definition
2. Tools
3. Biosignals data
4. Emotional data
5. Machine Learning aspect
6. What we learned in BHS2020

---

## Project idea

### Goal 
Predicting affective states based on biosignals for automatic stress detection in a wearable

### Dataset

DREAMER dataset: Participants were shown videos intended to elicit certain emotions while wearing an EEG headset and ECG sensors

<sup><sub> (The DREAMER dataset must be requested to the authors : https://ieeexplore.ieee.org/document/7887697 ) </sub></sup>


---

## Tools

![width=200](images/scipy.png)
![width=200](images/scipy_importexample.png)
![width=200](images/scipy_signalexample.png)

<sup><sub> Can read .MAT files in python </sub></sup>

<sup><sub> Example for EEG : Easy specification of bands (Theta, Alpha, Beta), PSD</sub></sup>


![width=200](images/plotly.png)

<sup><sub> Interactive data visualization (Exploration) </sub></sup>

---

## Tools

![width=500](images/neurokit2.png)
![width=600](images/neurokit2_importexample.png)

Example for ECG : 2 lines to extract Features !
![width=500](images/neurokit2_ecgdemo.png)

---

### Big data : Overview

<sup><sub><sub>23 subjects x 18 videos x 2 paradigms = 828 EEG recordings (x14 electrodes)!</sub></sub></sup>

![width=400](images/basl.gif)
![width=400](images/stim.gif)

Challenge : Extract relevant features from all this !

---

#### Biosignals preprocessing : Features extraction

EEG & ECG

![width=200](images/EEG_features.png)
![width=200](images/ECG_features.png)

<sup><sub> ECG : Features = Maximum of the PSDs for each of the 14 electrodes for each band : Theta (8-16Hz), Alpha (16-26Hz), Beta (26-60Hz)</sub></sup>

<sub><sub>Neurokit2 automatically extracts features e.g. Mean Heart Rate, Heart Rate Variability</sub></sub>

---

### Exploring the data

![width=800](images/plotly_EEG.gif)

---

### Exploring the data

![width=800](images/plotly_ECG.gif)

---
### Valence and Arousal ↔ Biosignal Features

Pearson's correlation

![width=800](images/pearson_eeg_ecg.png)

---

@snap[north span-100]
### Emotion data
@snapend

@snap[south span-100]
<iframe src="https://brainhack-school2020.github.io/Biosignal-Emotions-BHS-2020/" width="1000" height="500" frameborder="0" marginwidth="0" marginheight="0"></iframe>
@snapend

---

@snap[north span-100]
### Cross-validation
@snapend

@snap[south span-100]
<iframe src="https://brainhack-school2020.github.io/Biosignal-Emotions-BHS-2020/DREAMER_group_cross_validation.html" width="1000" height="500" frameborder="0" marginwidth="0" marginheight="0"></iframe>
@snapend

---

## What we learned in the BHS2020

- Distance teamwork
- Enhanced our Python skills
- Modern data visualization tools and practices


---

# Thank you!
