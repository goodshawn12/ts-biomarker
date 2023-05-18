import h5py
import numpy as np
import pandas as pd

from automatic_ecg_diagnosis import paths


class ECGDataset:
    def __init__(self):
        self.f = h5py.File(paths.ECG_TRACINGS, "r")
        self.x = self.f['tracings']  # convert it to numpy array?
        self.y = pd.read_csv(paths.ANNOT_GOLD_STANDARD)
        self.classes = self.y.columns.tolist()
        self.y = self.y.values
        self.n_classes = len(self.classes)
        self.n_samples = len(self.x)
        self.info = pd.read_csv(paths.PATIENT_ATTRIBUTES)

    def __del__(self):
        self.f.close()