### Biosignal processing for automatic emotion recognition

#### by the Effective Affective Team 
##### AKA Danielle & Achraf
<sup><sub>Made with GitPitch (thank you Agah!)</sub></sup>

<sup><sub> Link to this presentation:
  
  https://gitpitch.com/brainhack-school2020/Biosignal-Emotions-BHS-2020 </sub></sup>

---

### Detecting Stress?

![width=400](https://everythingweknowsofar.com/wp-content/uploads/2016/07/1446064502480.jpg)

<p><sup><sub>Have you ever felt stress and didn't manage to communicate it?</sub></sup></p>
<p><sup><sub>Could your body speak it for you?</sub></sup></p>
<p><sup><sub>What about having a wearable that can dynamically inform us about it?</sub></sup></p>

---

## Outline 

1. Project definition
2. Tools
3. Biosignal data
4. Challenges
5. Building a classifier
6. What we learned in BHS2020

---

## Project idea

### Goal 
Predicting affective states based on biosignals for automatic stress detection in a wearable

### Dataset

DREAMER dataset: Participants were shown videos intended to elicit certain emotions while wearing an EEG headset and ECG sensors

<sup><sub> (The DREAMER dataset must be requested from the authors: https://zenodo.org/record/546113) </sub></sup>

---

### EEG & ECG Acquisition

![width=500](images/DREAMER_papertitle.png)

![width=500](images/hardware.png)

---

## Tools

![width=200](images/scipy.png)
![width=200](images/scipy_importexample.png)
![width=200](images/scipy_signalexample.png)

<sup><sub> Can read .MAT files in python </sub></sup>

<sup><sub> Example for EEG: Easy specification of bands (Theta, Alpha, Beta), PSD</sub></sup>


![width=200](images/plotly.png)

<sup><sub> Interactive data visualization (Exploration) </sub></sup>

---

## Tools

![width=500](images/neurokit2.png)
![width=600](images/neurokit2_importexample.png)

Example for ECG: 2 lines to extract features!
![width=500](images/neurokit2_ecgdemo.png)

---

### Big data ! Overview

<sup><sub><sub>23 subjects x 18 videos x 2 paradigms = 828 EEG recordings (x14 electrodes)!</sub></sub></sup>

##### Baseline & Stimulus

![width=400](images/basl.gif)
![width=400](images/stim.gif)

Challenge: Extract relevant features from all this!

---

#### Biosignal preprocessing : Feature extraction

EEG & ECG

![width=200](images/EEG_features.png)
![width=200](images/ECG_features.png)

<sup><sub> EEG: Features = Maximum of the PSD for each electrode for 3 bands: Theta (8-16Hz), Alpha (16-26Hz), Beta (26-60Hz)</sub></sup>

<sub><sub> ECG: Neurokit2 automatically extracts features e.g. Mean Heart Rate, HRV </sub></sub>

---

### Exploring the data

![width=800](images/plotly_EEG.gif)

---

### Exploring the data

![width=800](images/plotly_ECG.gif)

---
#### Subjective ratings ↔ Physiological Features?

Pearson's correlation

![width=800](images/pearson_eeg_ecg.png)

##### Still challenging to find relevant features for automatic emotion recognition...

---
### Decisions, decisions...

- Biosignal data preprocessing?
- Feature selection?
- What should we even predict?!

<img src="https://imgs.xkcd.com/comics/decision_paralysis.png" alt="xkcd" width="215"/>

##### Replication of existing work? Not always straightforward!

---

### Affective data

<iframe src="https://brainhack-school2020.github.io/Biosignal-Emotions-BHS-2020/" width="1500" height="500" frameborder="0" marginwidth="0" marginheight="0"></iframe>

---

### Cross-validation

<iframe src="https://brainhack-school2020.github.io/Biosignal-Emotions-BHS-2020/DREAMER_group_cross_validation.html" width="1500" height="500" frameborder="0" marginwidth="0" marginheight="0"></iframe>

---
### Classifier comparison

<iframe src="https://brainhack-school2020.github.io/Biosignal-Emotions-BHS-2020/classifier_comparison.html" width="1500" height="500" frameborder="0" marginwidth="0" marginheight="0"></iframe>

---

### Future work

See how classifier performance changes with...
- Our earlier decisions <img src="https://neurokit.readthedocs.io/en/latest/_static/neurokit.png" alt="Neurokit" width="100"/>  
- Methods to reduce runtime <img src="https://cdn.onlinewebfonts.com/svg/img_554245.png" alt="Runtime" width="75"/> 
- An entirely new dataset <img src="https://upload.wikimedia.org/wikipedia/commons/4/40/OpenNeuro_Logo.png" alt="OpenNeuro" width="100"/> 

---

### What we learned in BHS2020

- More experience with GitHub <img src="https://github.githubassets.com/images/modules/open_graph/github-mark.png" alt="GitHub" width="75"/>
- Deeper understanding of machine learning <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/Scikit_learn_logo_small.svg/1200px-Scikit_learn_logo_small.svg.png" alt="Scikit learn" width="75"/>
- Improved coding skills <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/1200px-Python-logo-notext.svg.png" alt="Python" width="50"/> <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/38/Jupyter_logo.svg/1200px-Jupyter_logo.svg.png" alt="Jupyter" width="50"/> <img src="https://cdn.onlinewebfonts.com/svg/img_437009.png" alt="Python" width="50"/> 
- Appropriate use of notebooks <img src="https://dash.plotly.com/assets/images/logo-plotly.png" alt="Plotly" width="100"/>  <sub> vs. </sub> <img src="https://www.computecanada.ca/wp-content/uploads/2015/04/BILINGUAL-CC-WEB-LOGO.png" alt="ComputeCanada" width="50"/>
- Exposure to open science practices <img src="https://i2.wp.com/openscience.com/wp-content/uploads/2012/07/open_access.png?ssl=1" alt="BHS" width="25"/> 

---

## Many thanks to the instructors and organizers!

<sup><sub> Our instructors: Agah, Greg, Loic, Yann</sub></sup>
