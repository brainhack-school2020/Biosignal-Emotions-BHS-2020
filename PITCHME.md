### Biosignal processing for automatic emotion recognition

#### by the Effective Affective Team 
##### AKA Danielle & Achraf
<sup><sub>Made with GitPitch (thank you Agah!)</sub></sup>

---

### Hook !



---

### Outline 

1. Test
2. Test2

---

### Project idea

# Goal 
Predicting affective states based on biosignals for automatic stress detection in a wearable

# Dataset

DREAMER dataset: Participants were shown videos intended to elicit certain emotions while wearing an EEG headset and ECG sensors

(The DREAMER dataset must be requested to the authors : https://ieeexplore.ieee.org/document/7887697 )

---

@snap[north span-100]
### Emotion data
@snapend

@snap[south span-100]
<iframe src="https://brainhack-school2020.github.io/Biosignal-Emotions-BHS-2020/" width="1000" height="500" frameborder="0" marginwidth="0" marginheight="0"></iframe>
@snapend


---

### Tools
# Scipy
![width=100](images/scipy.png)
![width=100](images/scipy_importexample.png)
![width=100](images/scipy_signalexample.png)
# Neurokit2
![width=100](images/neurokit2.png)
![width=100](images/neurokit2_importexample.png)
![width=100](images/neurokit2_ecgdemo.png)
# Plotly
![width=100](images/plotly.png)

---

### Big data : Overview
![width=100](images/stim.gif) ![width=100](images/basl.gif)

---

### Biosignals preprocessing : Features extraction
## EEG                        ECG
![width=100](images/EEG_features.png) ![width=100](images/ECG_features.png)

---

### Exploring the data
## EEG
![width=100](images/plotly_EEG.gif)

---

### Exploring the data
## ECG
![width=100](images/plotly_ECG.gif)

---
### Valence and Arousal versus Biosignal Features
## Pearson's correlation
![width=100](images/pearson_eeg_ecg.png)

---

@snap[north span-100]
### Cross-validation
@snapend

@snap[south span-100]
<iframe src="https://brainhack-school2020.github.io/Biosignal-Emotions-BHS-2020/DREAMER_group_cross_validation.html" width="1000" height="500" frameborder="0" marginwidth="0" marginheight="0"></iframe>
@snapend

---

# Thank you!
