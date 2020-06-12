# Biosignal processing for automatic emotion recognition
[![Binder](https://mybinder.org/badge_logo.svg)](https://notebooks.gesis.org/binder/v2/gh/brainhack-school2020/Biosignal-Emotions-BHS-2020/85279820daf948d114d780e39d609c4f704f8cb1)

Team contributers: Danielle and Achraf

## Summary 

In this project for [BrainHack School 2020](https://school.brainhackmtl.org/), we used multimodal biosignal data to predict the "target emotion" of audiovisual stimuli. The project was written in Python and encompassed preprocessing, feature extraction, and classification. More information about the contents of this repository and instructions for how to run them can be found in [the "repoInfo" Markdown file](https://github.com/brainhack-school2020/Biosignal-Emotions-BHS-2020/blob/master/docs/repoInfo.md) located in [the docs folder](https://github.com/brainhack-school2020/Biosignal-Emotions-BHS-2020/tree/master/docs).

The project presentation is available [here](https://gitpitch.com/brainhack-school2020/Biosignal-Emotions-BHS-2020).

## Project definition 

### Background

#### About us

##### Danielle

I started my research master's this January, and my thesis project will involve the automatic classification of biosignals among other things. My background is in cognitive science, and while I've already learned about the basics of machine learning and neuroinformatics, I would like to improve my skills by working on a practical project with real data. 
 
##### Achraf
 
I am currently studying Biomedical Engineering at Polytechnique Montréal (M.Eng) and am enrolled in the Brain Hack School 2020 adventure for growing my technical skills as well as networking. I have been modestly introduced to NeuroImaging before enrolling in the biomedical engineering path and would like to broaden my knowledge of the field and sharpen my skills in it.

#### About the project

Psychological stress has been found to be associated with changes in certain biosignals. Features extracted from these biosignals have increasingly been used for predicting an individual's emotional state, including the EEG alpha asymmetry index, heart rate variability, and skin conductance response [(Giannakakis et al., 2019)](https://s3.amazonaws.com/academia.edu.documents/60215566/2019_Giannakakis_Review_on_psychological_stress_detection_using_biosignals20190806-1688-7kttp7.pdf?response-content-disposition=inline%3B%20filename%3DReview_on_psychological_stress_detection.pdf&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=ASIATUSBJ6BALIEFO2U4%2F20200521%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20200521T161015Z&X-Amz-Expires=3600&X-Amz-SignedHeaders=host&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJHMEUCIQCDcDSZcyT6u4Lc7Hc16sNh2InzAcekbrsiPyXV2UtM%2FQIgKLX0wumug7pgD59QsVol60DUF42liQhPUKjn7NITiNEqtAMIMBAAGgwyNTAzMTg4MTEyMDAiDDW7xJRp4wDPxgLtryqRA6P76YemmmJBvBnoRuW0%2BGaK9mS1Z61PKckoR8jxyxtvu45NdtS2qyfCAlopFhEH9zMMwHKKs7dwPdwbXuLt6HSQ06bRW8RTtGFE%2FooJvC9%2BZY2Pff1h%2Bnk8HW%2FM%2FDjlP5AzkmDpJ0KUO04PFxoqqBvFFIIy83iafxPVE0fly3fktUhE0kKsuOnBOjyABMzUPYI3nqjej%2BiJ8QpCQbqXx6r8YAuNJ5Nr4LGP2SVFKXA787KJnsrmD1uisIdjqLnjhzXaDZreoeukKMOF3yjQ1xG7srPW%2FWzoFSxLP79bNDEq54MJ145kg2i6vw8UqgdmDmNXjl3y7cLYLSJ%2BEFWkvYHCySYan1qdnjJDbTFYMm7GnRPM%2FVFfe6iwkPDI4gdwKyHnPH4JkEMvI2b7l%2FasmhHHjA932H5ziezXh%2FsJZNi5PdK26OwxxGM3MfiMjBpnf%2FtT%2FDPsq4B9i2i0azwQNiJYgDgw74VA%2BQJEtGPQnHaJjM%2FLud%2BMz35zKh%2BYRUMQqwFWPUOhA6EdYUgYcOUPWY7KMNexmvYFOusBM0Sz5ZgfGF1vsvoowJ42W%2BMbymHSuGfWGkUFug4P8pS02TC2eB9GPSMyN9CHbQ7PV2%2BbWVsPGBeqUtNSe6xOLqVR9goW4K3xWjw1cnSopEyUpXU%2F8C3qsCfUPGEUT2sw05J9F%2BlBBdSD7nZ4pH9SZxKFq5A6JRhzRcKIT11ba4UUznzwcBY6X%2FYgz3PpQYOl%2Bet5MFCw%2F3BcjRgR7nGytsLHNC9LmHGg9YAeQ7N%2Fo9%2BAGVVm6RDXpOeqExF7NkcKDofYQidkfUS6iGhOfdUA%2Fl1IkH4s%2BRbeATH2yeIOsIdEB%2FGqV8vOlEkrPg%3D%3D&X-Amz-Signature=62de6e2c0bd6f2dc619c179bf22988be24a3abdcbe8bbed4fd2c4dfdd2c6b780). This research has allowed for the development of technologies that can respond to users' emotions [(Carroll et al., 2013)](https://ieeexplore.ieee.org/abstract/document/6681439) and motivated the creation of multiple datasets containing emotion-correlated biosignal data [(Wiem & Lachiri, 2017)](https://pdfs.semanticscholar.org/3750/b635d455fee489305b24ead4b7e9233b7209.pdf). In this project, we were broadly interested in the task of emotion recognition, using a publicly available dataset to explore how we could predict emotions using biosignals.

### Tools 

Tools and techniques we used:
 1.	Bash and Python <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/20/Bash_Logo_black_and_white_icon_only.svg/1200px-Bash_Logo_black_and_white_icon_only.svg.png" alt="Bash" width="40"/> <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/1200px-Python-logo-notext.svg.png" alt="Python" width="40"/> 
 2. Git and GitHub <img src="https://github.githubassets.com/images/modules/open_graph/github-mark.png" alt="GitHub" width="50"/>
 3.	Preprocessing and feature extraction with Scipy and Neurokit <img src="https://docs.scipy.org/doc/scipy-0.12.0/reference/_static/scipyshiny_small.png" alt="Scipy" width="40"/> <img src="https://neurokit.readthedocs.io/en/latest/_static/neurokit.png" alt="NeuroKit" width="40"/>
 4.	Data visualization with Plotly <img src="https://dash.plotly.com/assets/images/logo-plotly.png" alt="Plotly" width="50"/>
 5. Machine learning with Scikit-learn <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/Scikit_learn_logo_small.svg/1200px-Scikit_learn_logo_small.svg.png" alt="Scikit-learn" width="50"/>

### Data 

At the start of the project, we considered using the following databases: 

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

The dataset contains EEG and ECG data from 23 participants were shown 18 videos intended to elicit 9 different emotions - as well as "neutral videos" thought to have no valence for "baseline" data. Biosignal data was collected using the Emotiv EPOC wireless EEG headset and the Shimmer2 ECG sensor. We were especially interested in how accurately we could classify emotions using biosignal data collected by portable, inexpensive devices due to the potential of automatic emotion recognition incorporated into wearables. An image of the equipment is shown below [(from Katsigiannis & Ramzan, 2018)](https://ieeexplore.ieee.org/document/7887697).

<p align="center">
 <img src="images/hardware.png" alt="DREAMER_hardware" width="500"/>
</p>

More information on how the data were collected can be found in the PDF [DREAMER_info](https://github.com/brainhack-school2020/Biosignal-Emotions-BHS-2020/blob/master/docs/DREAMER_info.pdf)  (downloaded from [Zenodo](https://zenodo.org/record/546113)) or in the paper by [Katsigiannis and Ramzan (2018)](https://ieeexplore.ieee.org/document/7887697).


### Deliverables

We were able to complete:
 - Data preprocessing and feature extraction for at least one biosignal.
 
    - [x]  [Python script](https://github.com/brainhack-school2020/Biosignal-Emotions-BHS-2020/blob/master/DREAMER_main.py)
        
 - Visualization of the relationship between the extracted features and the emotion data. 
 
    - [x]   [Jupyter notebook](https://github.com/brainhack-school2020/Biosignal-Emotions-BHS-2020/blob/master/Deliverables/DREAMER_Achraf.ipynb)
    
    - [x]   Both [interactive](https://brainhack-school2020.github.io/Biosignal-Emotions-BHS-2020/HR_fear_anger_calm.html) and [static](https://github.com/brainhack-school2020/Biosignal-Emotions-BHS-2020/blob/master/Deliverables/RMSSD_fear_anger_calm.png) visualizations

 - Training a classifier to predict the emotion data.
 
    - [x]   [Python script](https://github.com/brainhack-school2020/Biosignal-Emotions-BHS-2020/blob/master/DREAMER_main.py)
    
    - [x]   [Evaluation of classifier performance](https://github.com/brainhack-school2020/Biosignal-Emotions-BHS-2020/blob/master/Classification/DREAMER_classifier_comparison.ipynb)
     
    - [x]   [Shell script](https://github.com/brainhack-school2020/Biosignal-Emotions-BHS-2020/blob/master/run.sh)

### Progress & Results

We first preprocessed the biosignals and explored the relationship of extracted features with the emotion data, then we evaluated the performance of a number of classifiers. We created a minimal python script that performs the data preprocessing, feature extraction, and the classifier evaluation.

#### Achraf: Preprocessing and feature extraction

The preprocessing scripts I wrote were inspired by [Jiaqi1008's repository](https://github.com/Jiaqi1008/Emotion_detection). The DREAMER dataset being a .mat file, I used the library Scipy to load it: it contained EEG data, ECG data, and subjective ratings. 

The preprocessing for EEG data consisted of extracting the maximum of the Power Spectrum Density (PSD) for the EEG signals for three bands (theta, alpha, beta), for each of the 14 electrodes used. The library Scipy was used for filtering and PSD extraction (Welch's method). 

The preprocessing for ECG data was done thanks to the library [Neurokit2](https://github.com/neuropsychology/NeuroKit) by first preprocessing the data with the ecg_process() method then by extracting the features with the ecg_intervalrelated() method. The features extracted were the Mean Heart Rate and various Heart Rate Variability (HRV) metrics. 

I tested those preprocessing pipelines in notebooks first, then I wrote a script [DREAMER_main.py](https://github.com/brainhack-school2020/Biosignal-Emotions-BHS-2020/blob/master/DREAMER_main.py) implementing them. An output example of the script in a terminal can be found [here](https://github.com/brainhack-school2020/Biosignal-Emotions-BHS-2020/blob/master/Deliverables/ComputeCanadaScriptExample_Preprocessing.png)

#### Danielle: Evaluation of classifiers

I was interested in training a classifier to detect stress, but at the beginning of the project, I wasn't sure how exactly we should use the data to do so. I wanted to be able to compare my results to others, but there appears to be a wide range of ways to evaluate stress detection, further complicated by the fact that research on automatic emotion recognition and stress detection has relied on different models of emotion [(Wiem & Lachiri, 2017)](https://pdfs.semanticscholar.org/3750/b635d455fee489305b24ead4b7e9233b7209.pdf).

We first considered predicting self-reported valence and arousal scores, but then we explored the data and looked at the relationship between some of the features we extracted and valence/arousal. It seemed like these features did not indicate changes in valence or arousal as much as we'd hoped. It would be interesting to see how well we could predict valence and arousal using different methods of preprocessing, feature extraction, scaling, thresholding etc., but for the sake of this project, we thought we'd start with an easier classification problem.

In the paper describing DREAMER [(Katsigiannis & Ramzan, 2018)](https://ieeexplore.ieee.org/document/7887697), Table I contains the "target emotion" of each video clip with the video ID. The target emotion was not includied in the .mat file downloaded from Zenodo, so I [added this information to each datapoint based on the video ID](https://github.com/brainhack-school2020/Biosignal-Emotions-BHS-2020/blob/master/Data/load_emotion_data.py). Including this information allowed us to predict the emotions that were intended to be evoked by each stimulus, rather than self-reported emotions.

There were 9 different target emotions: "calmness", "surprise", "amusement", "fear", "excitement", "disgust", "happiness", "anger", and "sadness". Before determining whether we could predict the full sprectrum of emotions, I wanted to see whether we could distinguish "calmness" from two emotions on the opposite side of the spectrum: "anger" and "fear". This constituted a binary classification task: "calmness" vs. "not calmness".

To try to get an idea of how the classifiers would perform given biosignal data from completely new people, I evaluated the classifers using [Group 10-Fold Cross-Validation](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GroupKFold.html), with the groups being the participants - meaning that the training set and validation set always consisted of data from separate participants. However, we should note that we used the entire dataset for data exploration; there was no held-out test set that we only used solely for evaluation. Evaluating the classifiers on another emotion-correlated biosignal dataset may provide a more realistic idea of the classifiers' generalizability.

I selected a number of classifiers [based on a script from the sci-kit learn documentation](https://scikit-learn.org/stable/auto_examples/classification/plot_classifier_comparison.html): Nearest Neighbors, Support Vector Machine with a linear kernel, Support Vector Machine with an RBF kernel, Gaussian Process, Decision Tree, Random Forest, Multi-layer Perceptron, AdaBoost, and Naive Bayes. The accuracy averaged over the splits for each classifier, with features extracted from both the EEG and ECG data, is shown below:

| Name              | Mean Accuracy |
|-------------------|---------------|
| Nearest Neighbors | 0.87          |
| Linear SVM        | 0.67          |
| RBF SVM           | 0.87          |
| Gaussian Process  | 0.7           |
| Decision Tree     | 0.9           |
| Random Forest     | 0.9           |
| Neural Net        | 0.73          |
| AdaBoost          | 0.98          |
| Naive Bayes       | 0.59          |

[AdaBoost](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.AdaBoostClassifier.html), an ensemble method, had the highest mean accuracy. I also measured the average prediction runtime, and AdaBoost was relatively slow compared to the other classifiers (about 5-10 ms, while most of the others were around 1 ms, on my machine). While we didn't get to do this during this project, it would be interesting to see how methods to reduce runtime affect performance.

#### Week 3 deliverable: data visualization

##### Danielle's Week 3 deliverables
* Interactive Figure: ["Participant Ratings of Film Clips in Valence-Arousal Space](https://brainhack-school2020.github.io/Biosignal-Emotions-BHS-2020/)
  * Bonus: [a jupyter notebook generating this figure...](https://github.com/brainhack-school2020/Biosignal-Emotions-BHS-2020/blob/master/Deliverables/Week3_Emot_Plot_Danielle.ipynb) written while using a [linter](https://pypi.org/project/pycodestyle/), which I know about thanks to [Greg's talk on scripting](https://www.youtube.com/watch?v=zpOQENxs1G4)! [![Binder](https://mybinder.org/badge_logo.svg)](https://gesis.mybinder.org/binder/v2/gh/brainhack-school2020/Biosignal-Emotions-BHS-2020/85279820daf948d114d780e39d609c4f704f8cb1?filepath=Deliverables%2FWeek3_Emot_Plot_Danielle.ipynb)

* Interactive Figure: ["Group 10-Fold Cross Validation with DREAMER data"](https://brainhack-school2020.github.io/Biosignal-Emotions-BHS-2020/DREAMER_group_cross_validation.html)
* Interactive Figure: ["Score vs. Prediction Runtime for all CV Iterations and Classifiers"](https://brainhack-school2020.github.io/Biosignal-Emotions-BHS-2020/classifier_comparison.html)

##### Achraf's Week 3 deliverables
* [A Jupyter Notebook generating static and interactive visuals (ipynb)](https://github.com/brainhack-school2020/Biosignal-Emotions-BHS-2020/blob/master/Deliverables/DREAMER_Achraf.ipynb) and the corresponding [HTML version](https://github.com/brainhack-school2020/Biosignal-Emotions-BHS-2020/blob/master/Deliverables/DREAMER_Achraf.html)
* Static visuals that I found interesting during visual exploration of the data:
  * [Arousal patterns](https://github.com/brainhack-school2020/Biosignal-Emotions-BHS-2020/blob/master/Deliverables/Arousal.png)
  * [Valence patterns](https://github.com/brainhack-school2020/Biosignal-Emotions-BHS-2020/blob/master/Deliverables/Valence.png)
* Screenshot of terminal outputs of the scripts we wrote for Compute Canada (minimal version):
  * [Preprocessing command example](https://github.com/brainhack-school2020/Biosignal-Emotions-BHS-2020/blob/master/Deliverables/ComputeCanadaScriptExample_Preprocessing.png)
  * [Classification command example](https://github.com/brainhack-school2020/Biosignal-Emotions-BHS-2020/blob/master/Deliverables/ComputeCanadaScriptExample_Classification.png)

### Conclusion and acknowledgements

During the BrainHack School, we hoped to learn as much as we could about modern (neuro)scientific practice, to improve our Python skills through a hands-on multi-disciplinary project, and to exchange information and expertise with the other participants.

The first week was an intense theoretical and practical overview of many modern tools in neuroimaging, many of which we had very limited experience with or had never even heard of. The second week taught us how important it is to take enough time to clearly define a project and specify goals for it. Starting with a relatively broad project, it was difficult to narrow our goals down to one dataset and method, but ultimately we chose to pick one and see it through to the end. 

The third and fourth weeks were the core of the brain-hacking adventure and taught us many things such as:

* Improved coding skills: Python notebooks & scripting
* Deeper understanding of machine learning
* Open science tools and practices

While we weren't able to incorporate all of the tools that we had hoped to use in our project, we are grateful to have been exposed to them. Knowing where we can find [helpful online resources](https://school.brainhackmtl.org/schedule/) on all of the topics covered, we hope to slowly integrate what we've learned into our own work, post-BrainHack.

We would like to thank the course organizers and our instructors who spent a lot of time helping us with of our project and generally enlightening us:

* Greg
* Agâh
* Loic
* Yann

### References

Carroll, E. A., Czerwinski, M., Roseway, A., Kapoor, A., Johns, P., Rowan, K., & Schraefel, M. C. (2013, September). Food and mood: Just-in-time support for emotional eating. In *2013 Humaine Association Conference on Affective Computing and Intelligent Interaction* (pp. 252-257). IEEE.

Giannakakis, G., Grigoriadis, D., Giannakaki, K., Simantiraki, O., Roniotis, A., & Tsiknakis, M. (2019). Review on psychological stress detection using biosignals. *IEEE Transactions on Affective Computing.*

Katsigiannis, S., & Ramzan, N. (2017). DREAMER: A database for emotion recognition through EEG and ECG signals from wireless low-cost off-the-shelf devices. *IEEE journal of biomedical and health informatics*, 22(1), 98-107.

Wiem, M. B. H., & Lachiri, Z. (2017). Emotion classification in arousal valence model using MAHNOB-HCI database. *Int. J. Adv. Comput. Sci. Appl. IJACSA*, 8(3).
