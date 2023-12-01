def solution(deposit, rate, threshold):
    d = deposit
    y = 1
    
    while True:
        d = (rate / 100 * d) + d
        
        if d >= threshold:
            break

        y += 1
        
    return y



























