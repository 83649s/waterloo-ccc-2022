player_count = int(input())
players_above_forty = 0


for i in range(player_count):
    points = int(input())
    fouls = int(input())
    player_score = (points * 5) - (fouls * 3)
    if player_score > 40:
        players_above_forty += 1

if player_count == players_above_forty:
    print(str(player_count) + '+')
else:
    print(players_above_forty)
