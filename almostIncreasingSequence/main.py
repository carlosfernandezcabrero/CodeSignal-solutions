import numpy as np


def solution(sequence):
    if (np.diff(sequence) >= 0).all() and np.unique(sequence).size == len(sequence):
        return True

    copy_len = len(sequence) - 1

    for i, _ in enumerate(sequence):
        current_seq = sequence[i]

        if (
            (i == 0 and current_seq < sequence[i + 1])
            or (i == copy_len and sequence[i - 1] < current_seq)
            or (not sequence[i - 1] < current_seq < sequence[i + 1])
        ):
            _sequence_copy = np.delete(sequence, i)
            is_increasing = (np.diff(_sequence_copy) >= 0).all()

            if is_increasing and np.unique(_sequence_copy).size == copy_len:
                return True

    return False
