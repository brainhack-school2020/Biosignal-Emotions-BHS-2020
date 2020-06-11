### Repository description

* *Classification* folder: contains a Jupyter Notebook for the classifier evaluation
* *Data* folder: contains scripts and Jupyter Notebooks for preprocessing, feature extraction, and data visualization. It contains also an *Old* folder containing notebooks from early on in our project when we were exploring other datasets.
* *Deliverables* folder: contains the deliverables for Week 3
* *docs* folder: contains the interactive Plotly figures for the [GitPitch presentation](https://gitpitch.com/brainhack-school2020/Biosignal-Emotions-BHS-2020), *DREAMER_info.PDF*, a document with more information on the dataset, as well as a, *PotentialResources.md*, a Markdown file we used to document links that could help with advancing the project
* *Greg_tutorial* folder: contains *Greg_tutorial.ipynb* and *Greg_tutorial.py* are respectively a demo notebook and the script built based on this notebook that Greg Kiar used during his talk to demonstrate how one can first try code on a notebook then implement it as a script (May 29th 2020 course).
* *images* folder: contains the images for the [GitPitch presentation](https://gitpitch.com/brainhack-school2020/Biosignal-Emotions-BHS-2020)
* *DREAMER_main.py*: main script to be used in Compute Canada.
* *LICENSE*: Creative Commons CC0 1.0 Universal license
* *PITCHME.md*: Markdown source file for the [GitPitch presentation](https://gitpitch.com/brainhack-school2020/Biosignal-Emotions-BHS-2020)
* *run.sh*: Bash script for running the preprocessing and classifiers evaluation 

#### Instructions 

1. Request access to the DREAMER dataset on [Zenodo](https://zenodo.org/record/546113).  

2. Clone this repository

This can be done with:

```
git clone https://github.com/brainhack-school2020/Biosignal-Emotions-BHS-2020
```
Then change the working directory to ```Biosignal-Emotions-BHS-2020```. 

3. Install the required dependencies (it is recommended that you create and activate a [virtual environment](https://docs.python.org/3/tutorial/venv.html) beforehand)

This notebook was run with ```Python 3.7.6```. A ```requirements.txt``` file lists all of the packages in the virtual environment with which all of the notebooks and scripts were run. To download these packages, you can run:

```
pip install -r documents/requirements.txt
```

4. Move the ```DREAMER.mat``` file downloaded from Zenodo to ```Biosignal-Emotions-BHS-2020/Data```. 

5. For preprocessing, feature extraction, and classification with only the EEG data, only the ECG data, and both the EEG and ECG data, you can run:

```
bash run.sh
```

6. For the notebooks, you can run ```jupyter notebook``` and then the path to the notebook, e.g.:

```
jupyter notebook Deliverables/Week3_Emot_Plot_Danielle.ipynb	
```
