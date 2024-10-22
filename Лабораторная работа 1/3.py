list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

a = len(list_players)
middle_index = len(list_players) // 2

first_team = list_players[:middle_index]
second_team = list_players[middle_index:]

print('Общее количество игроков: ', a)
print(first_team)
print(second_team)
