# Project Description BrainHack School 2020

![BrainHack School](bhs2020.png)

## Summary 

*Project title* : **Biosignal processing for automatic emotion recognition**

In this project we intended to use multimodal datasets found from open data sources with the goal of using *biosignal processing* and *machine learning* techniques to perform *automatic emotion recognition*.
The project was performed using *Python* and *high performance computing* to build a classifier of discrete emotional states.
We made use of *data visualization* and share our work through *notebooks*.

The project presentation is available [here](https://gitpitch.com/brainhack-school2020/Biosignal-Emotions-BHS-2020).

## Project definition 

### Background

#### About us

<ins>*Danielle*</ins>

 I’m a master’s student working on the development of a device for students on the autism spectrum. The project envisions a device that can address students’ auditory sensitivities by filtering out distressing classroom sounds in real-time. I plan to use machine learning techniques for the following 2 components of the project: 

 1.	Audio event classification for the detection of identified classroom sounds
 2.	Biosignal-based automatic emotion recognition for the detection of sound-induced distress

 Assuming that #2 is where I can make the most of the expertise of fellow BrainHack school participants, I thought I could focus on biosignal processing for automatic emotion recognition during the project weeks.
 
<ins>*Achraf*</ins>
 
I am currently studying Biomedical Engineering at Polytechnique Montréal (M.Eng) and am enrolled in the Brain Hack School 2020 adventure for growing my technical skills as well as networking. I have been modestly introduced to NeuroImaging before enrolling in the biomedical engineering path and would like to broaden my knowledge of the field and sharpen my skills in it.

My goal through the Brain Hack School 2020 was to learn as much as I can about modern ways of doing NeuroImaging, to improve my python skills through a hands-on multi-disciplinary project, and to exchange information and expertise with the other participants.

The project idea is from Danielle with whom I was collaborating.

#### About the project

Psychological stress has been found to be associated with changes in certain biosignals. Features extracted from these biosignals have increasingly been used for predicting an individual's emotional state, [including the EEG alpha asymmetry index, heart rate variability, and skin conductance response.](https://s3.amazonaws.com/academia.edu.documents/60215566/2019_Giannakakis_Review_on_psychological_stress_detection_using_biosignals20190806-1688-7kttp7.pdf?response-content-disposition=inline%3B%20filename%3DReview_on_psychological_stress_detection.pdf&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=ASIATUSBJ6BALIEFO2U4%2F20200521%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20200521T161015Z&X-Amz-Expires=3600&X-Amz-SignedHeaders=host&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJHMEUCIQCDcDSZcyT6u4Lc7Hc16sNh2InzAcekbrsiPyXV2UtM%2FQIgKLX0wumug7pgD59QsVol60DUF42liQhPUKjn7NITiNEqtAMIMBAAGgwyNTAzMTg4MTEyMDAiDDW7xJRp4wDPxgLtryqRA6P76YemmmJBvBnoRuW0%2BGaK9mS1Z61PKckoR8jxyxtvu45NdtS2qyfCAlopFhEH9zMMwHKKs7dwPdwbXuLt6HSQ06bRW8RTtGFE%2FooJvC9%2BZY2Pff1h%2Bnk8HW%2FM%2FDjlP5AzkmDpJ0KUO04PFxoqqBvFFIIy83iafxPVE0fly3fktUhE0kKsuOnBOjyABMzUPYI3nqjej%2BiJ8QpCQbqXx6r8YAuNJ5Nr4LGP2SVFKXA787KJnsrmD1uisIdjqLnjhzXaDZreoeukKMOF3yjQ1xG7srPW%2FWzoFSxLP79bNDEq54MJ145kg2i6vw8UqgdmDmNXjl3y7cLYLSJ%2BEFWkvYHCySYan1qdnjJDbTFYMm7GnRPM%2FVFfe6iwkPDI4gdwKyHnPH4JkEMvI2b7l%2FasmhHHjA932H5ziezXh%2FsJZNi5PdK26OwxxGM3MfiMjBpnf%2FtT%2FDPsq4B9i2i0azwQNiJYgDgw74VA%2BQJEtGPQnHaJjM%2FLud%2BMz35zKh%2BYRUMQqwFWPUOhA6EdYUgYcOUPWY7KMNexmvYFOusBM0Sz5ZgfGF1vsvoowJ42W%2BMbymHSuGfWGkUFug4P8pS02TC2eB9GPSMyN9CHbQ7PV2%2BbWVsPGBeqUtNSe6xOLqVR9goW4K3xWjw1cnSopEyUpXU%2F8C3qsCfUPGEUT2sw05J9F%2BlBBdSD7nZ4pH9SZxKFq5A6JRhzRcKIT11ba4UUznzwcBY6X%2FYgz3PpQYOl%2Bet5MFCw%2F3BcjRgR7nGytsLHNC9LmHGg9YAeQ7N%2Fo9%2BAGVVm6RDXpOeqExF7NkcKDofYQidkfUS6iGhOfdUA%2Fl1IkH4s%2BRbeATH2yeIOsIdEB%2FGqV8vOlEkrPg%3D%3D&X-Amz-Signature=62de6e2c0bd6f2dc619c179bf22988be24a3abdcbe8bbed4fd2c4dfdd2c6b780). 

### Tools 

Tools and techniques we did use:
 1.	High-performance computing: Compute Canada
 2.	Preprocessing and feature extraction with Python
 3.	Data visualization with Python
 4.	GitHub
 5.	Python Virtual Environment

### Data 

So far, we have access to the following emotion-correlated biosignal databases: 

 - [The MAHNOB-HCI-Tagging database](https://mahnob-db.eu/hci-tagging/)
   - Biosignal data: EEG (in the form of BDF files), ECG, respiration amplitude, and skin temperature
   - Emotion data: Rating on valence-arousal scale provided by participants, and for some of the data, emotion tags (e.g. amused) selected by participants
 - [DREAMER: A Database for Emotion Recognition through EEG and ECG Signals from Wireless Low-cost Off-the-Shelf Devices](https://ieeexplore.ieee.org/document/7887697)
    - Biosignal data: EEG and ECG
    - Emotion data: Rating on valence-arousal-dominance scale provided by participants
 - [An EEG dataset recorded during affective music listening](https://openneuro.org/datasets/ds002721/versions/1.0.1)
     - Biosignal data: EEG
     - Emotion data: Rating on valence-arousal scale provided by participants
 - [AffectiveROAD system and database to assess driver's attention.](https://affect.media.mit.edu/share-data.php)
     - Biosignal data: BVP, EDA, ECG, respiration rate, skin temperature
     - Emotion data: "Stress metric" provided by observing experimenter 

### Deliverables

Our goals for the project were to complete:
 - Data preprocessing and feature extraction for at least one biosignal using Compute Canada.
 
    - [x]  Python scripts
    
    - [ ]  Job files
    
 - Visualization of the relationship between the extracted features and the emotion data. 
 
    - [x]   Python scripts
    
    - [x]   Image files included in report/notebook

 - Training of a classifier to predict the emotion data using Compute Canada.
 
    - [x]   Python scripts
    
    - [x]   Evaluation of classifier performance
     
    - [ ]   Job files

### Progress & Results

The dataset we ended up using is [DREAMER: A Database for Emotion Recognition through EEG and ECG Signals from Wireless Low-cost Off-the-Shelf Devices](https://ieeexplore.ieee.org/document/7887697).
We first performed a preprocessing of the biosignals and explored the affective data, then we evaluated the performance of many classifiers.
We created minimal python scripts that are to be executed on Compute Canada, and which let the user perform the data preprocessing and the classifiers evaluation.
The preprocessing scripts we wrote were inspired by [Jiaqi1008's repository](https://github.com/Jiaqi1008/Emotion_detection).

#### Preprocessing pipeline
* The DREAMER dataset coming as a .MAT file, we used the library Scipy to load it : it contained EEG data, ECG data, and subjective ratings.
* The preprocessing for EEG data consisted of extracting the maximum of the Power Spectrum Density (PSD) for the EEG signals for three bands (theta,alpha,beta), for each of the 14 electrodes used. The library Scipy was used for filtering and PSD extraction (Welch's method).
* The preprocessing for ECG data was done thanks to the library [Neurokit2](https://github.com/neuropsychology/NeuroKit) by first preprocessing the data with the ecg_process() method then by extracting the features with the ecg_intervalrelated() method. The features extracted were the Mean Heart Rate and various Heart Rate Variability (HRV) metrics.
* An output example of the script intended to be used in Compute Canada in a terminal can be found [here](https://github.com/brainhack-school2020/Biosignal-Emotions-BHS-2020/blob/master/Deliverables/ComputeCanadaScriptExample_Preprocessing.png)

#### Classification performance evaluation

* Affective data : Disgust and Anger versus Calmness
* k-Fold Cross-Validation : 10
* Classifiers explored : Nearest Neighbors, Linear SVM, RBF SVM, Gaussian Process, Decision Tree, Random Forest, Neural Net, AdaBoost and Naive Bayes
* An output example of the script intended to be used in Compute Canada in a terminal can be found [here](https://github.com/brainhack-school2020/Biosignal-Emotions-BHS-2020/blob/master/Deliverables/ComputeCanadaScriptExample_Classification.png)

Our progress and results were reported in Jupyter Notebooks which are presented below.

### Week 3 deliverable: data visualization

#### Danielle's Week 3 deliverables
* [Interactive Figure: "Participant Ratings of Film Clips in Valence-Arousal Space](https://brainhack-school2020.github.io/Biosignal-Emotions-BHS-2020/)
  * [Bonus: a jupyter notebook generating this figure...](https://github.com/brainhack-school2020/Biosignal-Emotions-BHS-2020/blob/master/Deliverables/Week3_Emot_Plot_Danielle.ipynb) written while attempting to follow [PEP8](https://www.python.org/dev/peps/pep-0008/)! This was my first time trying to write code following any standard, so feedback is welcome :) 
* [Interactive Figure: "Group 10-Fold Cross Validation with DREAMER data"](https://brainhack-school2020.github.io/Biosignal-Emotions-BHS-2020/DREAMER_group_cross_validation.html)
* [Interactive Figure: "Score vs. Prediction Runtime for all CV Iterations and Classifiers"](https://brainhack-school2020.github.io/Biosignal-Emotions-BHS-2020/classifier_comparison.html)

#### Achraf's Week 3 deliverables
* [A Jupyter Notebook generating static and interactive visuals (ipynb)](https://github.com/brainhack-school2020/Biosignal-Emotions-BHS-2020/blob/master/Deliverables/DREAMER_Achraf.ipynb) and the corresponding [HTML version](https://github.com/brainhack-school2020/Biosignal-Emotions-BHS-2020/blob/master/Deliverables/DREAMER_Achraf.html)
* Static visuals that I found interesting during visual exploration of the data :
  * [Arousal patterns](https://github.com/brainhack-school2020/Biosignal-Emotions-BHS-2020/blob/master/Deliverables/Arousal.png)
  * [Valence patterns](https://github.com/brainhack-school2020/Biosignal-Emotions-BHS-2020/blob/master/Deliverables/Valence.png)
* Screenshot of terminal outputs of the scripts we wrote for Compute Canada (minimal version) :
  * [Preprocessing command example](https://github.com/brainhack-school2020/Biosignal-Emotions-BHS-2020/blob/master/Deliverables/ComputeCanadaScriptExample_Preprocessing.png)
  * [Classification command example](https://github.com/brainhack-school2020/Biosignal-Emotions-BHS-2020/blob/master/Deliverables/ComputeCanadaScriptExample_Classification.png)

### Repository description :

* *Classification* folder : contains a Jupyter Notebook for the classifiers evaluation
* *Data* folder : this folder used to contain the data we worked on. Currently it contains scripts and Jupyter Notebooks for features extraction and data visualization. It contains also an *Old* folder in which we put our first trials of Week 2 (CoLab notebook, another dataset that we were about to use).
* *Deliverables* folder : contains the deliverables for Week 3
* *docs* folder : contains the interactive Plotly figures for the [GitPitch presentation](https://gitpitch.com/brainhack-school2020/Biosignal-Emotions-BHS-2020)
* *images* folder : contains the images for the [GitPitch presentation](https://gitpitch.com/brainhack-school2020/Biosignal-Emotions-BHS-2020)
* *DREAMER_main.py* : main script to be used in Compute Canada.
* *Greg_tutorial.ipynb* and *Greg_tutorial.py* are respectively a demo notebook and the script built based on this notebook that Gregory Kiar used our repository during his lecture to demonstrate how one can first try code on a notebook then implement it as a script (May 29th 2020 course).
* *LICENSE* : Creative Commons CC0 1.0 Universal license
* *PITCHME.md* : Markdown source file for the [GitPitch presentation](https://gitpitch.com/brainhack-school2020/Biosignal-Emotions-BHS-2020)
* *PotentialResources.md* : Markdown file we used as a common register for links that could help advancing the project

### Conclusion
####
* We worked with the DREAMER dataset which provided EEG and ECG data. The other datasets are worth exploring in that they provide other types of Biosignals such as Skin Temperature, Respiration.
* We could do a preprocessing of biosignals and extract features from EEG and ECG signals, as targeted.
* We tried to find strong correlations between the extracted features and subjective ratings, but the reality was that the correlations were low. This makes the detection of stress from biosignals challenging and not reliable as long as we don't find better features.
* Affective data showed more consistency in that anger and disgust were found to represent stress.
* Affective data was analyzed in a Machine Learning perspective : we compared the performance of multiple classifiers which was of a few milliseconds overall. AdaBoost showed the highest accuracy but at the cost of longer processing time.
#### What we learned in the BHS2020 project
The first week was an intense theoretical and practical overview of many modern tools in neuroimaging, many of which we never heard of before.
The second week taught us how important it is to take enough time to define clearly a project and specify goals for it. Instead of exploring many datasets at the same time, we chose to pick one and make the most out of it.
The third and fourth week were the core of the brain-hacking adventure and taught us many things such as :
* Open Science and Collaborative tools and practices (Git, GitHub, GitPitch)
* Improved coding skills : Python notebooks and scripting
* Deeper understanding of Machine Learning
### Acknowledgments
We would like to thank the course organizers and our instructors who spent a lot of time helping us in the advancement of our project :
* Gregory Kiar
* Agâh Karakuzu
* Loic Tetrel
* Yann Harel
