"""
Script to generate more training data.

Author: Kyle Oda (kynoda@ucsc.edu)
"""

import numpy as np
from mne.externals.pymatreader import read_mat
import os
import shutil

# paths
original_data_path = "Data/OriginalData/CleanData/"
generated_data_path = "Data/GeneratedData/"
base_path = "/Users/koda/Documents/UCSC/CSE247/project"

# GLOBAL VARS
clip_length = 5  # length of clip in seconds
freq = 128  # sampling frequency


def generate_data(filename, file_path, data_path, clip_len):
    """
    Generates new data for a given file

    :param filename: name of file to use to generate data from
    :param data_path: path for new data directory
    :param file_path: path to file to generate data
    :param clip_len: how long a clip to slice from original recording
    :return: None
    """

    clip_size = clip_len * freq

    # read data from .mat file
    data = read_mat(file_path)["clean_data"]

    # create directory for new data
    if os.path.isdir(data_path):
        shutil.rmtree(data_path)
    os.makedirs(data_path)
    os.chdir(data_path)

    # generate new data
    start = 0
    step = int(clip_size * 0.1)  # 90% overlap
    count = 1
    print(f"Generating data for {filename}")
    while clip_size < np.shape(data)[1]:
        np.savetxt(f"{filename[:-4]}_{count}.txt", data[:, start:clip_size])
        count += 1
        start += step
        clip_size += step

    os.chdir(base_path)


for group_dir in os.listdir(original_data_path):
    if group_dir[0] == ".":
        continue
    group_dir_path = os.path.join(original_data_path, group_dir)
    for type_dir in os.listdir(group_dir_path):
        if type_dir[0] == ".":
            continue
        type_dir_path = os.path.join(original_data_path, group_dir, type_dir)
        for file in os.listdir(type_dir_path):
            if file[0] == ".":
                continue
            # create directory for file and populate with new data.
            f_path = os.path.join(base_path, type_dir_path, file)
            file_dir = file[:-4]
            d_path = os.path.join(base_path, generated_data_path, group_dir, type_dir, file_dir)
            generate_data(file, f_path, d_path, clip_length)
