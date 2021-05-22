"""
File to combine data into npy files
"""

import os
import pathlib
import numpy as np
import glob


def combine_data(path, filename):
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

    # TODO: implement glob or pathlib


if __name__ == "__main__":
    combine_data("Data/GeneratedData/CleanData_IDD/Music", "IDD_music")
    combine_data("Data/GeneratedData/CleanData_IDD/Rest", "IDD_rest")
    combine_data("Data/GeneratedData/CleanData_TDC/Music", "TDC_music")
    combine_data("Data/GeneratedData/CleanData_TDC/Rest", "TDC_rest")

