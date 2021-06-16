"""
Script to preprocess data.

# TODO: Modify generate_data() to combine the clips into 1 for each group/type.
        # Then the combine_data function won't be needed

Author: Kyle Oda (kynoda@ucsc.edu)
"""

import numpy as np
from scipy.io import loadmat
import os
import shutil
# import pathlib


def combine_data(path, filename):
    """
    Combines a series of EEG clips into 1 numpy file
    :param path: directory path where clips are saved
    :param filename: name for the new file of combined clips
    :return: None
    """
    base_path = os.getcwd()
    X = []
    for subj_dir in os.listdir(path):
        if subj_dir[0] == ".":
            continue
        subj_dir_path = os.path.join(base_path, path, subj_dir)
        for file in os.listdir(subj_dir_path):
            X.append(np.load(os.path.join(subj_dir_path, file)))
        print(f"Loaded {subj_dir} files")
    np.save(os.path.join("Data/GeneratedData/combined_data", filename), X)


def generate_data(filename, file_path, data_path, clip_len=2, overlap=0.9):
    """
    Generates new data for a given file
    :param filename: name of file to use to generate data from
    :param data_path: path for new data directory
    :param file_path: path to file to generate data
    :param clip_len: how long a clip to slice from original recording
    :param overlap: amount of overlap between adjacent clips
    :return: None
    """

    clip_size = clip_len * freq

    # read data from .mat file
    data = loadmat(file_path)["clean_data"]

    # create directory for new data
    if os.path.isdir(data_path):
        shutil.rmtree(data_path)
    os.makedirs(data_path)
    os.chdir(data_path)

    # generate new data
    start = 0
    step = int(clip_size * (1 - overlap))
    count = 1
    print(f"Generating data for {filename}")
    while clip_size < np.shape(data)[1]:
        np.save(f"{filename[:-4]}_{count}", data[:, start:clip_size])
        count += 1
        start += step
        clip_size += step

    os.chdir(base_path)


if __name__ == "__main__":
    # paths
    original_data_path = "Data/OriginalData/CleanData/"
    generated_data_path = "Data/GeneratedData/"
    base_path = os.getcwd()

    clip_length = 2  # length of clip in seconds
    freq = 128  # sampling frequency
    overlap = 0.9

    # TODO: super jank, should reimplement with pathlib
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
                generate_data(file, f_path, d_path, clip_length, overlap)

    # Combine clips into 1 file for each category
    combine_data("Data/GeneratedData/CleanData_IDD/Music", "IDD_music")
    combine_data("Data/GeneratedData/CleanData_IDD/Rest", "IDD_rest")
    combine_data("Data/GeneratedData/CleanData_TDC/Music", "TDC_music")
    combine_data("Data/GeneratedData/CleanData_TDC/Rest", "TDC_rest")
