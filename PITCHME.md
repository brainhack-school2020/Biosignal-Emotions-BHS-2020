### Biosignal processing for automatic emotion recognition

#### by the Effective Affective Team 
##### AKA Danielle & Achraf
<sup><sub>Made with GitPitch (thank you Agah!)</sub></sup>

<sup><sub> Link to this presentation :
  
  https://gitpitch.com/brainhack-school2020/Biosignal-Emotions-BHS-2020 </sub></sup>

---

### Detecting Stress ?

![width=400](https://everythingweknowsofar.com/wp-content/uploads/2016/07/1446064502480.jpg)

<p><sup><sub>Have you ever felt stress and didn't manage to communicate it ?</sub></sup></p>
<p><sup><sub>Could your body speak it for you ?</sub></sup></p>
<p><sup><sub>What about having a wearable that can dynamically inform us about it ?</sub></sup></p>

---

## Outline 

1. Project definition
2. Tools
3. Biosignal data
4. Decisions and replication
5. Building a classifier
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

### Big data ! Overview

<sup><sub><sub>23 subjects x 18 videos x 2 paradigms = 828 EEG recordings (x14 electrodes)!</sub></sub></sup>

##### Baseline & Stimulus

![width=400](images/basl.gif)
![width=400](images/stim.gif)

Challenge : Extract relevant features from all this !

---

#### Biosignals preprocessing : Features extraction

EEG & ECG

![width=200](images/EEG_features.png)
![width=200](images/ECG_features.png)

<sup><sub> EEG : Features = Maximum of the PSD for each electrode for 3 bands : Theta (8-16Hz), Alpha (16-26Hz), Beta (26-60Hz)</sub></sup>

<sub><sub> ECG : Neurokit2 automatically extracts features e.g. Mean Heart Rate, HRV </sub></sub>

---

### Exploring the data

![width=800](images/plotly_EEG.gif)

---

### Exploring the data

![width=800](images/plotly_ECG.gif)

---
#### Subjective ratings ↔ Physiological Features ?

Pearson's correlation

![width=800](images/pearson_eeg_ecg.png)

##### Still challenging to find relevant features for automatic emotion recognition ...

---
### Decisions, decisions...

- How should we preprocess the biosignal data?
- Should we transform the data? How? MixMax scaling? Z-scoring?
- Which features should we use? 
- Should we divide features extracted from “stimuli” data (collected when emotional videos were played) by those extracted from “baseline” data?   
- What should we even predict?!


##### Replication of existing work? Not always straightforward!

---

@snap[north span-100]
### Affective data
@snapend

@snap[south span-100]
<iframe src="https://brainhack-school2020.github.io/Biosignal-Emotions-BHS-2020/" width="900" height="500" frameborder="0" marginwidth="0" marginheight="0"></iframe>
@snapend

---

@snap[north span-100]
### Cross-validation
@snapend

@snap[south span-100]
<iframe src="https://brainhack-school2020.github.io/Biosignal-Emotions-BHS-2020/DREAMER_group_cross_validation.html" width="900" height="500" frameborder="0" marginwidth="0" marginheight="0"></iframe>
@snapend

---

@snap[north span-100]
### Classifier Comparison
@snapend

@snap[south span-100]
<iframe src="https://brainhack-school2020.github.io/Biosignal-Emotions-BHS-2020/classifier_comparison.html" width="900" height="500" frameborder="0" marginwidth="0" marginheight="0"></iframe>
@snapend

---

### Future work

- Seeing how changing earlier decisions affects performance (e.g. preprocessing)
- Experimenting with methods to reduce prediction runtime
- Testing classifier performance on entirely new dataset

---

### What we learned in BHS2020

- More experience with GitHub
- New data visualization tools
- Deeper understanding of machine learning
- Better Python skills
- Appropriate use of notebooks (interactive visualizations vs. complex pipelines for HPC) 
- Exposure to open science tools and practices!

---

## Many thanks to the instructors and organizers!
