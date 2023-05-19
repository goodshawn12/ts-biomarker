import numpy as np
import plotly.graph_objects as go


def plot_ecg_tracings(ecg_tracings: np.ndarray = None):
    """Plot ecg tracings from the hdf5 file."""
    if ecg_tracings is None:
        return go.Figure()
