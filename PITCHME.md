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

<sup><sub> Example for EEG : Easy specification of bands (Theta, Alpha, Beta), filtering, PSD</sub></sup>


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

Hard to extract relevant features from so many Biosignals !

---

### Biosignals preprocessing : Features extraction

EEG

![width=100](images/EEG_features.png)

<sup><sub>
Theta band : 8Hz - 16Hz
Alpha band : 16Hz - 26 Hz
Beta band   : 26 Hz - 60Hz

Maximum of the PSDs for each of the 14 electrodes
</sub></sup>

---

### Biosignals preprocessing : Features extraction

ECG

![width=200](images/ECG_features.png)

<sub><sub>Neurokit2 automatically extracts features</sub></sub>

---

### Exploring the data

![width=800](images/plotly_EEG.gif)

---

### Exploring the data

![width=800](images/plotly_ECG.gif)

---
### Valence and Arousal versus Biosignal Features
### Pearson's correlation
![width=100](images/pearson_eeg_ecg.png)

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
