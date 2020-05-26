# Potentially useful resources for the project

## Loading data

1. For [MAHNOB HCI-Tagging](https://mahnob-db.eu/hci-tagging/): [python-edf](https://bitbucket.org/cleemesser/python-edf/src/default/) to load the biosignal data in the EDF files
2. For [MAHNOB HCI-Tagging](https://mahnob-db.eu/hci-tagging/): [Bob Database interface for the Mahnob HCI-Tagging database](https://gitlab.idiap.ch/bob/bob.db.hci_tagging)
3. For [DREAMER](https://ieeexplore.ieee.org/document/7887697): [scipy.io.loadmat](https://docs.scipy.org/doc/scipy/reference/generated/scipy.io.loadmat.html) to load the MAT file

## Preprocessing data

1. [NeuroKit2](https://github.com/neuropsychology/NeuroKit)
2. [mne](https://pypi.org/project/mne/)

## Feature selection

1. Determining features that we can expect to correlate with stress/changes in emotion: [Review on psychological stress detection using biosignals](https://s3.amazonaws.com/academia.edu.documents/60215566/2019_Giannakakis_Review_on_psychological_stress_detection_using_biosignals20190806-1688-7kttp7.pdf?response-content-disposition=inline%3B%20filename%3DReview_on_psychological_stress_detection.pdf&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=ASIATUSBJ6BALIEFO2U4%2F20200521%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20200521T161015Z&X-Amz-Expires=3600&X-Amz-SignedHeaders=host&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJHMEUCIQCDcDSZcyT6u4Lc7Hc16sNh2InzAcekbrsiPyXV2UtM%2FQIgKLX0wumug7pgD59QsVol60DUF42liQhPUKjn7NITiNEqtAMIMBAAGgwyNTAzMTg4MTEyMDAiDDW7xJRp4wDPxgLtryqRA6P76YemmmJBvBnoRuW0%2BGaK9mS1Z61PKckoR8jxyxtvu45NdtS2qyfCAlopFhEH9zMMwHKKs7dwPdwbXuLt6HSQ06bRW8RTtGFE%2FooJvC9%2BZY2Pff1h%2Bnk8HW%2FM%2FDjlP5AzkmDpJ0KUO04PFxoqqBvFFIIy83iafxPVE0fly3fktUhE0kKsuOnBOjyABMzUPYI3nqjej%2BiJ8QpCQbqXx6r8YAuNJ5Nr4LGP2SVFKXA787KJnsrmD1uisIdjqLnjhzXaDZreoeukKMOF3yjQ1xG7srPW%2FWzoFSxLP79bNDEq54MJ145kg2i6vw8UqgdmDmNXjl3y7cLYLSJ%2BEFWkvYHCySYan1qdnjJDbTFYMm7GnRPM%2FVFfe6iwkPDI4gdwKyHnPH4JkEMvI2b7l%2FasmhHHjA932H5ziezXh%2FsJZNi5PdK26OwxxGM3MfiMjBpnf%2FtT%2FDPsq4B9i2i0azwQNiJYgDgw74VA%2BQJEtGPQnHaJjM%2FLud%2BMz35zKh%2BYRUMQqwFWPUOhA6EdYUgYcOUPWY7KMNexmvYFOusBM0Sz5ZgfGF1vsvoowJ42W%2BMbymHSuGfWGkUFug4P8pS02TC2eB9GPSMyN9CHbQ7PV2%2BbWVsPGBeqUtNSe6xOLqVR9goW4K3xWjw1cnSopEyUpXU%2F8C3qsCfUPGEUT2sw05J9F%2BlBBdSD7nZ4pH9SZxKFq5A6JRhzRcKIT11ba4UUznzwcBY6X%2FYgz3PpQYOl%2Bet5MFCw%2F3BcjRgR7nGytsLHNC9LmHGg9YAeQ7N%2Fo9%2BAGVVm6RDXpOeqExF7NkcKDofYQidkfUS6iGhOfdUA%2Fl1IkH4s%2BRbeATH2yeIOsIdEB%2FGqV8vOlEkrPg%3D%3D&X-Amz-Signature=62de6e2c0bd6f2dc619c179bf22988be24a3abdcbe8bbed4fd2c4dfdd2c6b780) 
2. [The first answer of this StackExchange question](https://stats.stackexchange.com/questions/64825/should-feature-selection-be-performed-only-on-training-data-or-all-data)
3. To compare findings on stress with findings on Valence-Arousal: [This paper identifying stress regions in the Valence-Arousal space](https://link.springer.com/article/10.1007/s11042-016-3637-2)

## Determining classes for emotion recognition

1. [Emotion Classification in Arousal Valence Model using MAHNOB-HCI Database](https://pdfs.semanticscholar.org/3750/b635d455fee489305b24ead4b7e9233b7209.pdf)

## Scripts - Good practices

1. https://github.com/hyruuk/saflow/blob/master/scripts/saflow_raw2BIDS.py for BIDS restructuration of raw EEG data (yharel109)
