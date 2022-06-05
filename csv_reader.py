import csv

def reader():
    data = []
    with open('students.csv', 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(row)

    new_data = []
    save_member = 0
    for i in range(len(data[0])):
        temp = []
        temp.append(data[0][i])
        if data[1][i][:2] == "по":
            x = 1
        elif data[1][i][:2] == "вт":
            x = 2
        elif data[1][i][:2] == "ср":
            x = 3
        elif data[1][i][:2] == "че":
            x = 4
        elif data[1][i][:2] == "пя":
            x = 5
        elif data[1][i][:1] == "су":
            x = 6
        else:
            x = 7
            
        ln = len(data[1][i])
        if data[1][i][ln-4:] == "ьник":
            y = 1
        elif data[1][i][ln-4:] == "рник":
            y = 2
        elif data[1][i][ln-4:] == "реда":
            y = 3
        elif data[1][i][ln-4:] == "верг":
            y = 4
        elif data[1][i][ln-4:] == "ница":
            y = 5
        elif data[1][i][ln-4:] == "бота":
            y = 6
        else:
            y = 7
        temp.append([x, y])
        temp.append([int(data[2][i][:2]), int(data[2][i][3:5]), int(data[2][i][8:10]), int(data[2][i][11:13])])
        temp.append(data[3][i])
        new_data.append(temp)
    return new_data
