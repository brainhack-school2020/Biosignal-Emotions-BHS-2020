# Project Description BrainHack School 2020

![BrainHack School](bhs2020.png)

## Summary 

Biosignal processing for automatic emotion recognition using open data.

## Project definition 

### Background

#### About us

Danielle:

 I’m a master’s student working on the development of a device for students on the autism spectrum. The project envisions a device that can address students’ auditory sensitivities by filtering out distressing classroom sounds in real-time. I plan to use machine learning techniques for the following 2 components of the project: 

 1.	Audio event classification for the detection of identified classroom sounds
 2.	Biosignal-based automatic emotion recognition for the detection of sound-induced distress

 Assuming that #2 is where I can make the most of the expertise of fellow BrainHack school participants, I thought I could focus on biosignal processing for automatic emotion recognition during the project weeks.
 
Achraf:
 
I am currently studying Biomedical Engineering at Polytechnique Montréal (M.Eng) and am enrolled in the Brain Hack School 2020 adventure for growing my technical skills as well as networking. I have been modestly introduced to NeuroImaging before enrolling in the biomedical engineering path and would like to broaden my knowledge of the field and sharpen my skills in it.

My goal through the Brain Hack School 2020 is to learn as much as I can about modern ways of doing NeuroImaging, to improve my python skills through a hands-on multi-disciplinary project, and to exchange information and expertise with the other participants.

The project idea is from Danielle with whom I will be collaborating.

#### About the project

Psychological stress [has been found to be associated with changes in certain biosignals, including physiological measures such as EEG and ECG, as well as physical measures such as respiratory rate and skin temperature](https://s3.amazonaws.com/academia.edu.documents/60215566/2019_Giannakakis_Review_on_psychological_stress_detection_using_biosignals20190806-1688-7kttp7.pdf?response-content-disposition=inline%3B%20filename%3DReview_on_psychological_stress_detection.pdf&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=ASIATUSBJ6BALIEFO2U4%2F20200521%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20200521T161015Z&X-Amz-Expires=3600&X-Amz-SignedHeaders=host&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJHMEUCIQCDcDSZcyT6u4Lc7Hc16sNh2InzAcekbrsiPyXV2UtM%2FQIgKLX0wumug7pgD59QsVol60DUF42liQhPUKjn7NITiNEqtAMIMBAAGgwyNTAzMTg4MTEyMDAiDDW7xJRp4wDPxgLtryqRA6P76YemmmJBvBnoRuW0%2BGaK9mS1Z61PKckoR8jxyxtvu45NdtS2qyfCAlopFhEH9zMMwHKKs7dwPdwbXuLt6HSQ06bRW8RTtGFE%2FooJvC9%2BZY2Pff1h%2Bnk8HW%2FM%2FDjlP5AzkmDpJ0KUO04PFxoqqBvFFIIy83iafxPVE0fly3fktUhE0kKsuOnBOjyABMzUPYI3nqjej%2BiJ8QpCQbqXx6r8YAuNJ5Nr4LGP2SVFKXA787KJnsrmD1uisIdjqLnjhzXaDZreoeukKMOF3yjQ1xG7srPW%2FWzoFSxLP79bNDEq54MJ145kg2i6vw8UqgdmDmNXjl3y7cLYLSJ%2BEFWkvYHCySYan1qdnjJDbTFYMm7GnRPM%2FVFfe6iwkPDI4gdwKyHnPH4JkEMvI2b7l%2FasmhHHjA932H5ziezXh%2FsJZNi5PdK26OwxxGM3MfiMjBpnf%2FtT%2FDPsq4B9i2i0azwQNiJYgDgw74VA%2BQJEtGPQnHaJjM%2FLud%2BMz35zKh%2BYRUMQqwFWPUOhA6EdYUgYcOUPWY7KMNexmvYFOusBM0Sz5ZgfGF1vsvoowJ42W%2BMbymHSuGfWGkUFug4P8pS02TC2eB9GPSMyN9CHbQ7PV2%2BbWVsPGBeqUtNSe6xOLqVR9goW4K3xWjw1cnSopEyUpXU%2F8C3qsCfUPGEUT2sw05J9F%2BlBBdSD7nZ4pH9SZxKFq5A6JRhzRcKIT11ba4UUznzwcBY6X%2FYgz3PpQYOl%2Bet5MFCw%2F3BcjRgR7nGytsLHNC9LmHGg9YAeQ7N%2Fo9%2BAGVVm6RDXpOeqExF7NkcKDofYQidkfUS6iGhOfdUA%2Fl1IkH4s%2BRbeATH2yeIOsIdEB%2FGqV8vOlEkrPg%3D%3D&X-Amz-Signature=62de6e2c0bd6f2dc619c179bf22988be24a3abdcbe8bbed4fd2c4dfdd2c6b780). For EEG data 

### Tools 

Tools and techniques we plan to use:
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

At the end of this project, we plan to complete:
 - Data preprocessing and feature extraction for at least one biosignal using Compute Canada.
 
    &rarr; Python scripts
    
    &rarr; Job files
    
 - Visualization of the relationship between the extracted features and the emotion data. 
 
    &rarr; Python scripts
    
    &rarr; Image files included in report/notebook

 - Training of a classifier to predict the emotion data using Compute Canada.
 
     &rarr; Python scripts
    
     &rarr; Evaluation of classifier performance
     
     &rarr; Job files
