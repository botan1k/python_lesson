def lesson4(x):  # выполнение задачи
    d = {}
    for key in x:
        if x[key] >= 3: d[key] = x[key]
    return d


# def lesson4_to_lst(x): # запись значений словаря в список
#    d = []
#    for x, value in dict.items():
#        if value >= 3: d.append(value)
#    return(d)


dict = {'one': 1, 'two': 2, 'thee': 3, 'four': 4, 'five': 5}
print(lesson4(dict))
# print(lesson4_to_lst(dict))
