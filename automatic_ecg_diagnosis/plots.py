import numpy as np
import plotly.graph_objects as go

from automatic_ecg_diagnosis import constants


def plot_ecg_tracings(ecg_tracings: np.ndarray = None):
    """Plot ecg tracings from the hdf5 file."""
    if ecg_tracings is None:
        return go.Figure()

    ecg_leads = [lead.value for lead in list(constants.ECGLead)]
