def slices(series, length):
    if (length > len(series)) or (length <= 0) or (len(series) == ''):
        raise ValueError(".+")
    return [''.join(series[i : i + length]) for i in range(len(series) - length + 1)]