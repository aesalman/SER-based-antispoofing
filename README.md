# SER-based-antispoofing

This repository contains code for Speech Emotion Recognition Based Audio Antispoofing.


## Installation
Clone this repository to your workspace using the following command.

`git clone git@github.com:hashim19/SER-based-antispoofing.git'

`cd SER-based-antispoofing`

### Follow this [tutorial](https://www.freecodecamp.org/news/how-to-setup-virtual-environments-in-python/) to create a virtual environment in the parent directory of this repository

Activate the virtual environment using the following commands. 

`source *environment name* /bin/activate`

Once, the environment is activated, run the following command in the parent directory of this repository to install the required libraries.

`pip3 install -r requiremnts.txt`

We are using disvoice to extract prosody and articulation features, disvoice needs praat which can be installed using

`sudo apt-get install praat`

## Usage
Download the [famous figures](https://drive.google.com/drive/folders/1bCWCn8zv72pUIl4NlAg78bILscIfQTH5?usp=drive_link) dataset at the root of this repository.

main.py gives an example of how you can generate features and plot them. At the start of this file, give the speaker names for whom you want to generate the features.

Run `python3 main.py`

This will generate a directory with the name 'output'. This directory will contain the features in the form of pickle files.

