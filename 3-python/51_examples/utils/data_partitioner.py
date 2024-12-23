import numpy as np
from zlib import crc32

def shuffle_and_split_data(data, test_ratio):
    """
    This function splits the data without using any identifier.
    Due to this, the model can be exposed to whole data when you run this multiple times.
    """
    shuffled_indices = np.random.permutation(len(data))
    test_set_size = int(len(data) * test_ratio)
    test_indices = shuffled_indices[:test_set_size]
    train_indices = shuffled_indices[test_set_size:]
    return data.iloc[train_indices], data.iloc[test_indices]

def is_id_in_test_set(identifier, test_ratio):
    """
    Check if there is identifier field
    """
    return crc32(np.int64(identifier)) < test_ratio * 2**32

def split_data_with_id_hash(data, test_ratio, id_column):
    """
    Split data based on identifier so that all data do not get exposed to the model
    """
    ids = data[id_column]
    in_test_set = ids.apply(lambda id_: is_id_in_test_set(id_, test_ratio))
    return data.loc[~in_test_set], data.loc[in_test_set]

