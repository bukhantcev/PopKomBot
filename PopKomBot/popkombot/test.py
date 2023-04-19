with open('Access.txt', 'r', encoding='UTF-8') as file:
    file = file.readlines()
    file.append('dddddddd')
    print(file)
