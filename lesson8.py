with open('gitignore.txt', 'w') as l8:
    l8.writelines(['/venv\n', '.idea'])

with open('gitignore.txt', 'r') as l8:
    f = l8.readlines()
    sep = ','
    q1 = sep.join(f)
    q1 = q1[::-1]
    q1 = q1.split(',')
    l8.seek(0)
    print(l8.readlines())

with open('lesson8_file.txt', 'w') as l8_2:
    l8_2.writelines(q1)

with open('lesson8_file.txt', 'r') as l8_2:
    print(l8_2.readlines())
