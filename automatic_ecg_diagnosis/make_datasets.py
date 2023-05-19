import h5py
import pandas as pd

from automatic_ecg_diagnosis import paths, constants


class ECGDataset:
    def __init__(self, test_set=True):
        if test_set:  # smaller dataset for testing
            self.f = h5py.File(paths.ECG_TRACINGS, "r")
            self.y = pd.read_csv(paths.ANNOT_GOLD_STANDARD)
            self.info = pd.read_csv(paths.PATIENT_ATTRIBUTES)
        else:
            self.f = h5py.File(paths.ECG_TRACINGS_0, "r")  # TODO: add more part files
            self.y = pd.read_csv(paths.ANNOT_TRAIN_DATA)
            self.info = None

        self.x = self.f['tracings']  # convert it to numpy array?
        self.classes = self.y.columns.tolist()
        self.y = self.y.values
        self.n_classes = len(self.classes)
        self.n_samples = len(self.x)
        self.n_labels = self.y.shape[0]
        self.sample_rate = constants.SAMPLING_RATE_ECG

    def __del__(self):
        self.f.close()
