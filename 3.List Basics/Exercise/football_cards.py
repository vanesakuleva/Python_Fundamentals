red_flags = input(). split(' ')
team_a= 11
team_b= 11
players_loses = []
condition = False


for i in red_flags:
    if i not in  players_loses :
        players_loses.append(i)
        if 'A' in i:
            team_a -= 1
        elif 'B' in i:
            team_b -= 1
        if team_a < 7 or team_b < 7 :
            condition = True
            break

print(f"Team A - {team_a}; Team B - {team_b}")
if condition :
    print ("Game was terminated")


