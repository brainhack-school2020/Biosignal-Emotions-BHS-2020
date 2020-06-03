### Biosignal processing for automatic emotion recognition

#### by the Effective Affective Team 
##### AKA Danielle & Achraf
<sup><sub>Made with GitPitch (thank you Agah!)</sub></sup>

<sup><sub> Link to this presentation :
  
  https://gitpitch.com/brainhack-school2020/Biosignal-Emotions-BHS-2020 </sub></sup>

---

# Hook !


---

# Outline 

1. Test
2. Test2

---

## Project idea

### Goal 
Predicting affective states based on biosignals for automatic stress detection in a wearable

### Dataset

DREAMER dataset: Participants were shown videos intended to elicit certain emotions while wearing an EEG headset and ECG sensors

<sup><sub> (The DREAMER dataset must be requested to the authors : https://ieeexplore.ieee.org/document/7887697 ) </sub></sup>


---

## Tools
### Scipy
![width=100](images/scipy.png)
![width=100](images/scipy_importexample.png)
![width=100](images/scipy_signalexample.png)
### Plotly
![width=100](images/plotly.png)

---

## Tools
### Neurokit2
![width=500](images/neurokit2.png)
![width=500](images/neurokit2_importexample.png)
![width=500](images/neurokit2_ecgdemo.png)

---

### Big data : Overview

<sub>23 subjects x 18 videos x 2 paradigms = 828 EEG recordings !
(+14 electrodes per EEG recording) </sub>

![width=500](images/stim.gif) ![width=100](images/basl.gif)

---

### Biosignals preprocessing : Features extraction
### EEG  <br/> ECG
![width=100](images/EEG_features.png) ![width=100](images/ECG_features.png)

---

### Exploring the data
### EEG
![width=100](images/plotly_EEG.gif)

---

### Exploring the data
### ECG
![width=100](images/plotly_ECG.gif)

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

---

# Thank you!
