#Examples:
data = [['Group1', [1, 4], [20, 0, 22, 0], 'cirmiuwu#1039,Bankai#6237'], ['Group2', [2, 5], [20, 0, 22, 0], 'cirmiuw#1039'], ['Group3', [7, 1], [16, 0, 18, 0], 'Bankai#6237,Ktirskikh#8472']]
nickname = 'cirmiuw#1039'
channel = 'Group2'
day = 2
hours = 21
minutes = 18

def log(data, nickname, channel, day, hours, minutes):
    if day == 0:
        day = 7
    for i in range(len(data)):
        if data[i][0] == channel and day >= data[i][1][0] and day <= data[i][1][1] and data[i][2][0] <= hours and data[i][2][2] >= hours:
            for j in range(len(data[i][3])-len(nickname)+1):
                if data[i][3][j:len(nickname)+j] == nickname:
                    f = open('log.txt', 'r+')
                    file = f.read()
                    if len(file) == 0:
                        f.write(f'Списки посетивших занятия: {nickname} посетил голосовую комнату {channel} в {hours}:{minutes}')
                        print(f"Пользователя {nickname} отметили.")
                    else:
                        f.write(f'; {nickname} посетил голосовую комнату {channel} в {hours}:{minutes}')
                        print(f"Пользователя {nickname} отметили.")
                    f.close()
def clear():
    f = open('log.txt', 'w')
    f.close()
    print('Файл log.txt очищен.')
                    
