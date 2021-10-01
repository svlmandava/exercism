def slices(series, length):
    if length > len(series) or length <= 0:
        raise ValueError(".+Slicing is not possible.")
    return [series[i : i + length] for i in range(len(series) - length + 1)]