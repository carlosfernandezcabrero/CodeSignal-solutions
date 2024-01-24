def solution(min1, min2_10, min11, s):
    m = 0
    m_aux = m

    while True:
        if m >= 10:
            s = s - min11
            m_aux = m + 1
        elif m > 0 and m < 10:
            s = s - min2_10
            m_aux = m + 1
        elif m == 0:
            s = s - min1
            m_aux = m + 1

        if s <= 0:
            if s == 0:
                m = m_aux
            break

        m = m_aux

    return m
