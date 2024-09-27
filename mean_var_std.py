import numpy as np

def calculate(list):

    if len(list)!= 9:
        raise ValueError('List must contain nine numbers.')
    else: list = np.array(list).reshape(3,3)

    flat = list.flatten()

    media_linhas = np.mean(list, axis=1).tolist()
    media_colunas = np.mean(list, axis=0).tolist()
    media_flat = np.mean(flat).tolist()

    var_linhas = np.var(list,axis=1).tolist()
    var_colunas = np.var(list, axis=0).tolist()
    var_flat = np.var(flat).tolist()

    std_linhas = np.std(list,axis=1).tolist()
    std_colunas = np.std(list, axis=0).tolist()
    std_flat = np.std(flat).tolist()

    max_linhas = np.max(list,axis=1).tolist()
    max_colunas = np.max(list, axis=0).tolist()
    max_flat = np.max(flat).tolist()

    min_linhas = np.min(list,axis=1).tolist()
    min_colunas = np.min(list, axis=0).tolist()
    min_flat = np.min(flat).tolist()

    sum_linhas = np.sum(list,axis=1).tolist()
    sum_colunas = np.sum(list, axis=0).tolist()
    sum_flat = np.sum(flat).tolist()

    calculations = {
        'mean': [media_colunas, media_linhas, media_flat],
        'variance': [var_colunas, var_linhas, var_flat],
        'standard deviation': [std_colunas, std_linhas, std_flat],
        'max': [max_colunas, max_linhas, max_flat],
        'min': [min_colunas, min_linhas, min_flat],
        'sum': [sum_colunas, sum_linhas, sum_flat]
    }
    
    return calculations