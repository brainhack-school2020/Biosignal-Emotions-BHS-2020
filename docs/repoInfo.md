### Repository description

* [Classification](https://github.com/brainhack-school2020/Biosignal-Emotions-BHS-2020/tree/master/Classification) folder: contains a Jupyter Notebook for the classifier evaluation
* [Data](https://github.com/brainhack-school2020/Biosignal-Emotions-BHS-2020/tree/master/Data) folder: contains scripts and Jupyter Notebooks for preprocessing, feature extraction, and data visualization. It also contains an [Old](https://github.com/brainhack-school2020/Biosignal-Emotions-BHS-2020/tree/master/Data/Old) folder containing notebooks from early on in our project when we were exploring other datasets
* [Deliverables](https://github.com/brainhack-school2020/Biosignal-Emotions-BHS-2020/tree/master/Deliverables) folder: contains some of our visualizations, in the form of image files, HTML files, or Jupyter Notebooks
* [docs](https://github.com/brainhack-school2020/Biosignal-Emotions-BHS-2020/tree/master/docs) folder: contains this document, some interactive figures, [DREAMER_info.pdf](https://github.com/brainhack-school2020/Biosignal-Emotions-BHS-2020/blob/master/docs/DREAMER_info.pdf), a document with more information on the dataset, as well as [PotentialResources.md](https://github.com/brainhack-school2020/Biosignal-Emotions-BHS-2020/blob/master/docs/PotentialResources.md), a Markdown file we used to document links that could help with advancing the project
* [Greg_tutorial](https://github.com/brainhack-school2020/Biosignal-Emotions-BHS-2020/blob/master/Greg_tutorial) folder: contains [Greg_tutorial.ipynb](https://github.com/brainhack-school2020/Biosignal-Emotions-BHS-2020/blob/master/Greg_tutorial/Greg_tutorial.ipynb) and [Greg_tutorial.py](https://github.com/brainhack-school2020/Biosignal-Emotions-BHS-2020/blob/master/Greg_tutorial/Greg_tutorial.py), which are respectively a demo notebook and the script built based on this notebook that Greg Kiar used during [his talk on scripting in Python](https://www.youtube.com/watch?v=zpOQENxs1G4) (May 29th 2020 course).
* [images](https://github.com/brainhack-school2020/Biosignal-Emotions-BHS-2020/blob/master/images) folder: contains some images used in the [GitPitch presentation](https://gitpitch.com/brainhack-school2020/Biosignal-Emotions-BHS-2020)
* [DREAMER_main.py](https://github.com/brainhack-school2020/Biosignal-Emotions-BHS-2020/blob/master/DREAMER_main.py): main script for preprocessing, feature extraction, and classifier evaluation
* [LICENSE](https://github.com/brainhack-school2020/Biosignal-Emotions-BHS-2020/blob/master/LICENSE): Creative Commons CC0 1.0 Universal license
* [PITCHME.md](https://github.com/brainhack-school2020/Biosignal-Emotions-BHS-2020/blob/master/PITCHME.md): Markdown source file for the [GitPitch presentation](https://gitpitch.com/brainhack-school2020/Biosignal-Emotions-BHS-2020)
* [run.sh](https://github.com/brainhack-school2020/Biosignal-Emotions-BHS-2020/blob/master/run.sh): Bash script for running the preprocessing, feature extraction, and classifier evaluation
* [requirements.txt](https://github.com/brainhack-school2020/Biosignal-Emotions-BHS-2020/blob/master/requirements.txt): Lists the packages in the virtual environment with which all of the notebooks and scripts were run (has some unnecessary packages)

#### Instructions 

1. Request access to the DREAMER dataset on [Zenodo](https://zenodo.org/record/546113).  

2. Clone this repository

This can be done with:

```
git clone https://github.com/brainhack-school2020/Biosignal-Emotions-BHS-2020
```
Then change the working directory to ```Biosignal-Emotions-BHS-2020```. 

3. Install the required dependencies (it is recommended that you create and activate a [virtual environment](https://docs.python.org/3/tutorial/venv.html) beforehand)

The scripts and notebooks were run with ```Python 3.7.6```. To download the packages from the ```requirements.txt``` file, you can run:

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

Alternatively, you can open them in binder in your browser:

https://notebooks.gesis.org/binder/v2/gh/brainhack-school2020/Biosignal-Emotions-BHS-2020/85279820daf948d114d780e39d609c4f704f8cb1 [![Binder](https://mybinder.org/badge_logo.svg)](https://notebooks.gesis.org/binder/v2/gh/brainhack-school2020/Biosignal-Emotions-BHS-2020/85279820daf948d114d780e39d609c4f704f8cb1)
