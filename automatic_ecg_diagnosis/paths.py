from pathlib import Path

# Path to the root of the project
ROOT = Path(__file__).parent

# User-defined root path to downloaded data folder
ROOT_DATA = Path('/Volumes/shawn-ssd/Data/automatic_ecg_diagnosis')

# Path to the data folder
DIR_DATA = ROOT_DATA / "data"
DIR_ANNOTATIONS = DIR_DATA / "annotations"
DIR_TRAIN = ROOT_DATA / "train_data"
DIR_MODEL = ROOT_DATA / "model"

# Path to ECG test dataset (small)
ECG_TRACINGS = DIR_DATA / "ecg_tracings.hdf5"
PATIENT_ATTRIBUTES = DIR_DATA / "attributes.csv"

# Path to annotations
ANNOT_GOLD_STANDARD = DIR_ANNOTATIONS / "gold_standard.csv"
ANNOT_CARDIOLOGIST_1 = DIR_ANNOTATIONS / "cardiologist1.csv"
ANNOT_CARDIOLOGIST_2 = DIR_ANNOTATIONS / "cardiologist2.csv"

# Path to ECG train dataset (large)
ECG_TRACINGS_0 = DIR_TRAIN / "exams_part0.hdf5"
ANNOT_TRAIN_DATA = DIR_TRAIN / "exams.csv"
