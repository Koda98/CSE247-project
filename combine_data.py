"""
File to combine data into npy files
"""

import os
import numpy as np


def combine_data(path, filename):
    base_path = os.getcwd()
    X = []
    for subj_dir in os.listdir(path):
        if subj_dir[0] == ".":
            continue
        subj_dir_path = os.path.join(base_path, path, subj_dir)
        for file in os.listdir(subj_dir_path):
            X.append(np.loadtxt(os.path.join(subj_dir_path, file)))
        print(f"Loaded {subj_dir} files")
    np.save(os.path.join("Data/GeneratedData", filename), X)


if __name__ == "__main__":
    combine_data("Data/GeneratedData/CleanData_IDD/Rest", "IDD_rest")

# X = []
# Y = []
#
# data_path = "Data/GeneratedData/CleanData_IDD/"
# base_path = os.getcwd()
#
# for type_dir in os.listdir(data_path):
#     if type_dir[0] == ".":
#         continue
#     type_dir_path = os.path.join(base_path, data_path, type_dir)
#     for subject in os.listdir(type_dir_path):
#         if subject[0] == ".":
#             continue
#         subject_dir_path = os.path.join(type_dir_path, subject)
#         for file in os.listdir(subject_dir_path):
#             if "Music" in file:
#                 Y.append(1)
#             elif "Rest" in file:
#                 Y.append(0)
#             X.append(np.loadtxt(os.path.join(type_dir_path, subject, file)))
#         print(f"Loaded {subject} files")

