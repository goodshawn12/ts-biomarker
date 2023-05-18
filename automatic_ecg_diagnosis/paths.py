from pathlib import Path

# Path to the root of the project
ROOT = Path(__file__).parent
ROOT_DATA = Path('/Volumes/shawn-ssd/Data/automatic_ecg_diagnosis')  # Change to your data path)

# Path to the data folder
DIR_DATA = ROOT_DATA / "data"
DIR_ANNOTATIONS = DIR_DATA / "annotations"

# Path to ECG data
ECG_TRACINGS = DIR_DATA / "ecg_tracings.hdf5"
PATIENT_ATTRIBUTES = DIR_DATA / "attributes.csv"

# Path to annotations
ANNOT_GOLD_STANDARD = DIR_ANNOTATIONS / "gold_standard.csv"
ANNOT_CARDIOLOGIST_1 = DIR_ANNOTATIONS / "cardiologist1.csv"
ANNOT_CARDIOLOGIST_2 = DIR_ANNOTATIONS / "cardiologist2.csv"
