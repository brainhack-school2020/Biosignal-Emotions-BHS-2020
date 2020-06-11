# Biosignal processing for automatic emotion recognition

## Summary 

In this project for [BrainHack School 2020](https://school.brainhackmtl.org/), we used a multimodal biosignal dataset to predict the "target emotion" of audiovisual stimuli. The project was written in Python and encompassed preprocessing, feature extraction, and classification. More information about the contents of this repository can be found at the end of this page.

The project presentation is available [here](https://gitpitch.com/brainhack-school2020/Biosignal-Emotions-BHS-2020).

## Project definition 

### Background

#### About us

##### Danielle

I started my research master's this January, and my thesis project will involve the automatic classification of biosignals, among other things. My background is in cognitive science, and while I've learned about the basics of machine learning, I never got the chance to work on a larger, practical project.

The BrainHack School was a great opportunity for me to work with open data before getting to collect my own.
 
##### Achraf
 
I am currently studying Biomedical Engineering at Polytechnique Montréal (M.Eng) and am enrolled in the Brain Hack School 2020 adventure for growing my technical skills as well as networking. I have been modestly introduced to NeuroImaging before enrolling in the biomedical engineering path and would like to broaden my knowledge of the field and sharpen my skills in it.

My goal through the Brain Hack School 2020 was to learn as much as I can about modern ways of doing NeuroImaging, to improve my python skills through a hands-on multi-disciplinary project, and to exchange information and expertise with the other participants.

The project idea is from Danielle with whom I was collaborating.

#### About the project

Psychological stress has been found to be associated with changes in certain biosignals. Features extracted from these biosignals have increasingly been used for predicting an individual's emotional state, [including the EEG alpha asymmetry index, heart rate variability, and skin conductance response](https://s3.amazonaws.com/academia.edu.documents/60215566/2019_Giannakakis_Review_on_psychological_stress_detection_using_biosignals20190806-1688-7kttp7.pdf?response-content-disposition=inline%3B%20filename%3DReview_on_psychological_stress_detection.pdf&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=ASIATUSBJ6BALIEFO2U4%2F20200521%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20200521T161015Z&X-Amz-Expires=3600&X-Amz-SignedHeaders=host&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJHMEUCIQCDcDSZcyT6u4Lc7Hc16sNh2InzAcekbrsiPyXV2UtM%2FQIgKLX0wumug7pgD59QsVol60DUF42liQhPUKjn7NITiNEqtAMIMBAAGgwyNTAzMTg4MTEyMDAiDDW7xJRp4wDPxgLtryqRA6P76YemmmJBvBnoRuW0%2BGaK9mS1Z61PKckoR8jxyxtvu45NdtS2qyfCAlopFhEH9zMMwHKKs7dwPdwbXuLt6HSQ06bRW8RTtGFE%2FooJvC9%2BZY2Pff1h%2Bnk8HW%2FM%2FDjlP5AzkmDpJ0KUO04PFxoqqBvFFIIy83iafxPVE0fly3fktUhE0kKsuOnBOjyABMzUPYI3nqjej%2BiJ8QpCQbqXx6r8YAuNJ5Nr4LGP2SVFKXA787KJnsrmD1uisIdjqLnjhzXaDZreoeukKMOF3yjQ1xG7srPW%2FWzoFSxLP79bNDEq54MJ145kg2i6vw8UqgdmDmNXjl3y7cLYLSJ%2BEFWkvYHCySYan1qdnjJDbTFYMm7GnRPM%2FVFfe6iwkPDI4gdwKyHnPH4JkEMvI2b7l%2FasmhHHjA932H5ziezXh%2FsJZNi5PdK26OwxxGM3MfiMjBpnf%2FtT%2FDPsq4B9i2i0azwQNiJYgDgw74VA%2BQJEtGPQnHaJjM%2FLud%2BMz35zKh%2BYRUMQqwFWPUOhA6EdYUgYcOUPWY7KMNexmvYFOusBM0Sz5ZgfGF1vsvoowJ42W%2BMbymHSuGfWGkUFug4P8pS02TC2eB9GPSMyN9CHbQ7PV2%2BbWVsPGBeqUtNSe6xOLqVR9goW4K3xWjw1cnSopEyUpXU%2F8C3qsCfUPGEUT2sw05J9F%2BlBBdSD7nZ4pH9SZxKFq5A6JRhzRcKIT11ba4UUznzwcBY6X%2FYgz3PpQYOl%2Bet5MFCw%2F3BcjRgR7nGytsLHNC9LmHGg9YAeQ7N%2Fo9%2BAGVVm6RDXpOeqExF7NkcKDofYQidkfUS6iGhOfdUA%2Fl1IkH4s%2BRbeATH2yeIOsIdEB%2FGqV8vOlEkrPg%3D%3D&X-Amz-Signature=62de6e2c0bd6f2dc619c179bf22988be24a3abdcbe8bbed4fd2c4dfdd2c6b780). 

### Tools 

Tools and techniques we used:
 1.	Bash and Python <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/20/Bash_Logo_black_and_white_icon_only.svg/1200px-Bash_Logo_black_and_white_icon_only.svg.png" alt="Bash" width="50"/> <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/1200px-Python-logo-notext.svg.png" alt="Python" width="50"/> 
 2. Git and GitHub <img src="https://github.githubassets.com/images/modules/open_graph/github-mark.png" alt="GitHub" width="50"/>
 3.	Preprocessing and feature extraction with Scipy and Neurokit <img src="https://docs.scipy.org/doc/scipy-0.12.0/reference/_static/scipyshiny_small.png" alt="Scipy" width="50"/> <img src="https://neurokit.readthedocs.io/en/latest/_static/neurokit.png" alt="NeuroKit" width="50"/>
 4.	Data visualization with Plotly <img src="https://dash.plotly.com/assets/images/logo-plotly.png" alt="Plotly" width="50"/>
 5. Machine learning with Scikit-learn <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/Scikit_learn_logo_small.svg/1200px-Scikit_learn_logo_small.svg.png" alt="Scikit-learn" width="50"/>

### Data 

At the start of the project, we considered using the following emotion-correlated biosignal databases: 

 - [DREAMER: A Database for Emotion Recognition through EEG and ECG Signals from Wireless Low-cost Off-the-Shelf Devices](https://ieeexplore.ieee.org/document/7887697)
    - Biosignal data: EEG and ECG
    - Emotion data: Rating on valence-arousal-dominance scale provided by participants and tags for the "target emotion" of the stimuli
 - [The MAHNOB-HCI-Tagging database](https://mahnob-db.eu/hci-tagging/)
   - Biosignal data: EEG (in the form of BDF files), ECG, respiration amplitude, and skin temperature
   - Emotion data: Rating on valence-arousal scale provided by participants, and for some of the data, emotion tags (e.g. amused) selected by participants
 - [An EEG dataset recorded during affective music listening](https://openneuro.org/datasets/ds002721/versions/1.0.1)
     - Biosignal data: EEG
     - Emotion data: Rating on valence-arousal scale provided by participants (though it's not immediately clear where this can be downloaded)
 - [AffectiveROAD system and database to assess driver's attention.](https://affect.media.mit.edu/share-data.php)
     - Biosignal data: BVP, EDA, ECG, respiration rate, skin temperature
     - Emotion data: "Stress metric" provided by observing experimenter 
     
Ultimately, we decided to use the [DREAMER](https://ieeexplore.ieee.org/document/7887697) dataset which must be requested from the authors [here](https://zenodo.org/record/546113).  

The dataset contains EEG and ECG data from 23 participants were shown 18 videos intended to elicit 9 different emotions - as well as "neutral videos" thought to have no valence for "baseline" data. Biosignal data was collected using the Emotiv EPOC wireless EEG headset and the Shimmer2 ECG sensor. We were especially interested in how accurately we could classify emotions using biosignal data collected by portable, inexpensive devices due to the potential of automatic emotion recognition incorporated into wearables. An image of the equipment is shown below [(from Katsigiannis and Ramzan, 2018)](https://ieeexplore.ieee.org/document/7887697).

![width=200](images/hardware.png)

More information on how the data were collected can be found in the PDF [DREAMER_info](https://github.com/brainhack-school2020/Biosignal-Emotions-BHS-2020/blob/master/docs/DREAMER_info.pdf)  (downloaded from [Zenodo](https://zenodo.org/record/546113)) or in the paper by [Katsigiannis and Ramzan (2018)](https://ieeexplore.ieee.org/document/7887697).


### Deliverables

We were able to complete:
 - Data preprocessing and feature extraction for at least one biosignal.
 
    - [x]  Python script
        
 - Visualization of the relationship between the extracted features and the emotion data. 
 
    - [x]   Jupyter notebook
    
    - [x]   Both interactive and static visualizations

 - Training a classifier to predict the emotion data.
 
    - [x]   Python script
    
    - [x]   Evaluation of classifier performance
     
    - [ ]   Job file

### Progress & Results

We first preprocessed the biosignals and explored the relationship of extracted features with the emotion data, then we evaluated the performance of a number of classifiers.
We created a minimal python script that perform the data preprocessing, feature extraction, and the classifier evaluation.

Achraf focused on preprocessing the biosignals, visually explored the biosignal data and wrote minimal working version of scripts.
Danielle focused on the machine learning pipeline and the evaluation of classifiers performance for the affective data.

#### Achraf: Preprocessing and feature extraction

The preprocessing scripts I wrote were inspired by [Jiaqi1008's repository](https://github.com/Jiaqi1008/Emotion_detection).

* The DREAMER dataset coming as a .MAT file, I used the library Scipy to load it: it contained EEG data, ECG data, and subjective ratings.
* The preprocessing for EEG data consisted of extracting the maximum of the Power Spectrum Density (PSD) for the EEG signals for three bands (theta,alpha,beta), for each of the 14 electrodes used. The library Scipy was used for filtering and PSD extraction (Welch's method).
* The preprocessing for ECG data was done thanks to the library [Neurokit2](https://github.com/neuropsychology/NeuroKit) by first preprocessing the data with the ecg_process() method then by extracting the features with the ecg_intervalrelated() method. The features extracted were the Mean Heart Rate and various Heart Rate Variability (HRV) metrics.
* I tested those preprocessing pipelines on Notebooks first, then wrote a script *DREAMER_main.py* implementing them.
An output example of the script in a terminal can be found [here](https://github.com/brainhack-school2020/Biosignal-Emotions-BHS-2020/blob/master/Deliverables/ComputeCanadaScriptExample_Preprocessing.png)

#### Danielle: Evaluation of classifiers

* Affective data: Disgust and Anger versus Calmness
* Group 10-Fold Cross-Validation using Scikit-learn
* I explored a number of classifiers [based on a script from the sci-kit learn documentation](https://scikit-learn.org/stable/auto_examples/classification/plot_classifier_comparison.html), inspired by the following Classifiers explored: Nearest Neighbors, Linear SVM, RBF SVM, Gaussian Process, Decision Tree, Random Forest, Neural Net, AdaBoost and Naive Bayes
* Achraf implemented my Machine Learning pipeline in the *DREAMER_main.py* script, which I later enriched. 

Our progress and results are presented in deliverables below.

#### Week 3 deliverable: data visualization

##### Danielle's Week 3 deliverables
* [Interactive Figure: "Participant Ratings of Film Clips in Valence-Arousal Space](https://brainhack-school2020.github.io/Biosignal-Emotions-BHS-2020/)
  * [Bonus: a jupyter notebook generating this figure...](https://github.com/brainhack-school2020/Biosignal-Emotions-BHS-2020/blob/master/Deliverables/Week3_Emot_Plot_Danielle.ipynb) written while attempting to follow [PEP8](https://www.python.org/dev/peps/pep-0008/)! 
* [Interactive Figure: "Group 10-Fold Cross Validation with DREAMER data"](https://brainhack-school2020.github.io/Biosignal-Emotions-BHS-2020/DREAMER_group_cross_validation.html)
* [Interactive Figure: "Score vs. Prediction Runtime for all CV Iterations and Classifiers"](https://brainhack-school2020.github.io/Biosignal-Emotions-BHS-2020/classifier_comparison.html)

##### Achraf's Week 3 deliverables
* [A Jupyter Notebook generating static and interactive visuals (ipynb)](https://github.com/brainhack-school2020/Biosignal-Emotions-BHS-2020/blob/master/Deliverables/DREAMER_Achraf.ipynb) and the corresponding [HTML version](https://github.com/brainhack-school2020/Biosignal-Emotions-BHS-2020/blob/master/Deliverables/DREAMER_Achraf.html)
* Static visuals that I found interesting during visual exploration of the data:
  * [Arousal patterns](https://github.com/brainhack-school2020/Biosignal-Emotions-BHS-2020/blob/master/Deliverables/Arousal.png)
  * [Valence patterns](https://github.com/brainhack-school2020/Biosignal-Emotions-BHS-2020/blob/master/Deliverables/Valence.png)
* Screenshot of terminal outputs of the scripts we wrote for Compute Canada (minimal version):
  * [Preprocessing command example](https://github.com/brainhack-school2020/Biosignal-Emotions-BHS-2020/blob/master/Deliverables/ComputeCanadaScriptExample_Preprocessing.png)
  * [Classification command example](https://github.com/brainhack-school2020/Biosignal-Emotions-BHS-2020/blob/master/Deliverables/ComputeCanadaScriptExample_Classification.png)

### Conclusion and acknowledgements

* We worked with the DREAMER dataset which provided EEG and ECG data. The other datasets are worth exploring in that they provide other types of Biosignals such as Skin Temperature, Respiration.
* We could do a preprocessing of biosignals and extract features from EEG and ECG signals, as targeted.
* We tried to find strong correlations between the extracted features and subjective ratings, but the reality was that the correlations were low. This makes the detection of stress from biosignals challenging and not reliable as long as we don't find better features.
* Affective data showed more consistency in that anger and disgust were found to represent stress.
* Affective data was analyzed in a Machine Learning perspective : we compared the performance of multiple classifiers which was of a few milliseconds overall. AdaBoost showed the highest accuracy but at the cost of longer processing time.

#### What we learned in the BHS2020 project
The first week was an intense theoretical and practical overview of many modern tools in neuroimaging, many of which we never heard of before or had limited experience with. The second week taught us how important it is to take enough time to define clearly a project and specify goals for it. Instead of exploring many datasets at the same time, we chose to pick one and make the most out of it.
The third and fourth week were the core of the brain-hacking adventure and taught us many things such as:
* Open Science and Collaborative tools and practices (Git, GitHub, GitPitch)
* Improved coding skills : Python notebooks and scripting
* Deeper understanding of Machine Learning
### Acknowledgments
We would like to thank the course organizers and our instructors who spent a lot of time helping us in the advancement of our project :
* Gregory Kiar
* Agâh Karakuzu
* Loic Tetrel
* Yann Harel

### Repository description
* *Classification* folder: contains a Jupyter Notebook for the classifiers evaluation
* *Data* folder: contains scripts and Jupyter Notebooks for preprocessing, feature extraction, and data visualization. It contains also an *Old* folder containing notebooks from early on in our project when we were exploring other datasets.
* *Deliverables* folder: contains the deliverables for Week 3
* *docs* folder: contains the interactive Plotly figures for the [GitPitch presentation](https://gitpitch.com/brainhack-school2020/Biosignal-Emotions-BHS-2020), *DREAMER_info.PDF*, a document with more information on the dataset, as well as a, *PotentialResources.md*, a Markdown file we used to document links that could help with advancing the project
* *Greg_tutorial* folder: contains *Greg_tutorial.ipynb* and *Greg_tutorial.py* are respectively a demo notebook and the script built based on this notebook that Greg Kiar used during his talk to demonstrate how one can first try code on a notebook then implement it as a script (May 29th 2020 course).
* *images* folder: contains the images for the [GitPitch presentation](https://gitpitch.com/brainhack-school2020/Biosignal-Emotions-BHS-2020)
* *DREAMER_main.py*: main script to be used in Compute Canada.
* *LICENSE*: Creative Commons CC0 1.0 Universal license
* *PITCHME.md*: Markdown source file for the [GitPitch presentation](https://gitpitch.com/brainhack-school2020/Biosignal-Emotions-BHS-2020)

#### Instructions

1. Clone this repository

This can be done with:

```
git clone https://github.com/brainhack-school2020/Biosignal-Emotions-BHS-2020
```
Then change the working directory to ```Biosignal-Emotions-BHS-2020```. 

2. Install the required dependencies (it is recommended that you create and activate a [virtual environment](https://docs.python.org/3/tutorial/venv.html) beforehand)

This notebook was run with ```Python 3.7.6```. A ```requirements.txt``` file lists all of the packages in the virtual environment with which all of the notebooks and scripts were run. To download these packages, you can run:

```
pip install -r documents/requirements.txt
```

3. To run any of the notebooks, run the following command: 

```
jupyter notebook PathToNotebook.ipynb
```


