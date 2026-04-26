def solution(data, ext, val_ext, sort_by):
    col_idx = {"code": 0, "date": 1, "maximum": 2, "remain": 3}
    filtered_data = list(filter(lambda x: x[col_idx[ext]] < val_ext, data))
    sorted_data = sorted(filtered_data, key=lambda x: x[col_idx[sort_by]])
    return sorted_data