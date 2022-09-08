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
    vox_by_time = np.reshape(data, (-1, data.shape[-1])
    vox_diff = np.diff(vox_by_time, axis=1)
    return np.sqrt(np.mean(vox_diff**2,axis=0))
