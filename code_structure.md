├── data                > All data goes here
│   └── group-00
│       ├── hash_list.txt
│       ├── sub-01
├── findoutlie          > Use these files for finding outlies,
|   |                     files in this folder use moduels in /scripts
│   ├── detectors.py    > Utilities for detecting outliers
|   |                   def iqr_detector
│   ├── __init__.py     > init for python module 
│   ├── metrics.py      > Scan outlier metrics
|   |                   > def dvars(img)
|   |                      Calculate dvars metric
|   |                      on Nibabel image `img`
│   ├── outfind.py      > Module with routines for finding outliers
|   |                   > def detect_outliers(fname):
|   |                       Detect outliers given image file path `filename`
|   |                     def find_outliers(data_directory):
|   |                       Return filenames and outlier indices
|   |                       for images in `data_directory`.
│   ├── spm_funcs.py    > This module defines functions implementing
|   |                     algorithms in SPM
│   └── tests
│       ├── ds107_sub012_t1r2_small.nii
│       ├── get_global_signals.m
│       ├── global_signals.txt
│       ├── test_detectors.py
│       ├── test_dvars.py
│       └── test_spm_funcs.py
├── scripts
│   ├── find_outliers.py    > Python script to find outliers
|   |                           def print_outliers(data_directory)
|   |                           def get_parser()
|   |                           def main()
│   └── validate_data.py    > Python script to validate data
|   |                           def file_hash(filename):
|   |                           def validate_data(data_directory):
|   |                           def main():
├── solutions
│   ├── detectors.py
│   ├── metrics.py
│   ├── test_detectors.py
│   ├── test_spm_funcs.py
│   ├── validate_data.py
│   └── write_solutions.sh
├── on_the_project.md
├── pyproject.toml
├── pytest.ini
├── README.md
├── requirements.txt
