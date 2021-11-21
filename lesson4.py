def lesson4(x):
    d = {}
    for key in x:
        if x[key] >= 3: d[key] = x[key]
    return d

dict = {'one': 1, 'two': 2, 'thee': 3, 'four': 4, 'five': 5}
print(lesson4(dict))