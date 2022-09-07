""" Scan outlier metrics
"""

# Any imports you need
import numpy as np

def dvars(img):
    """ Calculate dvars metric on Nibabel image `img`

    The dvars calculation between two volumes is defined as the square root of
    (the mean of the (voxel differences squared)).

    Parameters
    ----------
    img : nibabel image

    Returns
    -------
    dvals : 1D array
        One-dimensional array with n-1 elements, where n is the number of
        volumes in `img`.
    """
    data = img.get_fdata()
    # voxel diff  =  (data from 0 to -1) - (data from 1 to the end of array)
    vol_diff = data[...,:-1].reshape((-1,data.shape[-1]-1))-data[...,1:].reshape((-1,data.shape[-1]-1))
    return np.sqrt(np.mean(vol_diff**2,axis=0))
