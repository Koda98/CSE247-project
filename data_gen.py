"""
Script to generate more training data.

Author: Kyle Oda (kynoda@ucsc.edu)
"""

import numpy as np
from mne.externals.pymatreader import read_mat
import os
import shutil

# TDC_dir = "Data/OriginalData/CleanData/CleanData_TDC"
# os.chdir(TDC_dir)

# Path to TDC data
original_data_path = "Data/OriginalData/CleanData/CleanData_TDC/Music/CGS01_Music_CD.mat"
path = "Data/OriginalData/CleanData/CleanData_TDC/Music/CGS01_Music_CD.mat"

# read data from .mat file
clean_data = read_mat(path)
clean_data = clean_data["clean_data"]
print("Data shape:", np.shape(clean_data))

# create directory for generated data
data_gen_path = "Data/GeneratedData"
if os.path.isdir(data_gen_path):
    shutil.rmtree(data_gen_path)
os.mkdir(data_gen_path)
os.chdir(data_gen_path)

# Generate training data
clip_size = 640  # 5 seconds
start = 0
step = int(clip_size * 0.1)  # 90% overlap
count = 1

while clip_size < np.shape(clean_data)[1]:
    # if count > 5:
    #     break
    print(f"Saving data to NewData_{count}")
    # print(np.shape(clean_data[:, start:filter_size]))
    # np.save(f"NewData_{count}", clean_data[:, start:filter_size])
    np.savetxt(f"NewData_{count}.txt", clean_data[:, start:clip_size])
    count += 1
    start += step
    clip_size += step

