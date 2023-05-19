from enum import Enum

SAMPLING_RATE_ECG = 400  # Hz


# 12-lead ECG channel names
class ECGLead(Enum):
    DI = 'DI'
    DII = 'DII'
    DIII = 'DIII'
    AVR = 'AVR'
    AVL = 'AVL'
    AVF = 'AVF'
    V1 = 'V1'
    V2 = 'V2'
    V3 = 'V3'
    V4 = 'V4'
    V5 = 'V5'
    V6 = 'V6'
