from enum import Enum

SAMPLING_RATE_ECG = 400  # Hz


# 12-lead ECG channel names
class ECGLead(Enum):
    LEAD_I = 'Lead I'
    LEAD_II = 'Lead II'
    LEAD_III = 'Lead III'
    LEAD_aVR = 'Lead aVR'
    LEAD_aVL = 'Lead aVL'
    LEAD_aVF = 'Lead aVF'
    V1 = 'V1'
    V2 = 'V2'
    V3 = 'V3'
    V4 = 'V4'
    V5 = 'V5'
    V6 = 'V6'
