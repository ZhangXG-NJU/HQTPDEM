import os
import numpy as np
import rasterio
from math import sqrt

def get_file_paths(folder):
    return [os.path.join(folder, filename) for filename in os.listdir(folder) if filename.endswith('.tif')]

def process_error_matrix(errmat, method):
    errmat_flat = errmat.flat
    mask = np.logical_and(errmat_flat >= -1000, errmat_flat <= 1000)
    errmat_filtered = np.compress(mask, errmat_flat)
    
    if method == 'mae':
        return np.mean(np.abs(errmat_filtered))
    elif method == 'rmse':
        return sqrt(np.mean(errmat_filtered ** 2))
    elif method == 'maxerr':
        return np.max(np.abs(errmat_filtered))

def measure_whole_dataset(root, method):
    files = get_file_paths(root)
    values = []
    for file in files:
        errmat = rasterio.open(file).read(1)
        value = process_error_matrix(errmat, method)
        filename = os.path.basename(file)
        print("{:<20}, {:<10}, {:.2f}".format(filename, method, value))
        values.append(value)
    print(' ')
    return files, values

root = r'E:\Zhang_XinGang\11_QPTDEM\09_valid_data\10_err'
measure_whole_dataset(root, 'mae')
measure_whole_dataset(root, 'rmse')
#measure_whole_dataset(root, 'maxerr')
