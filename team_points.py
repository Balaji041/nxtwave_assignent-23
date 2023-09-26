def calculate_league_points(wins, draws, losses):
    # Complete this function
    return (wins*4 +draws*2)-losses

statistics = input().split(",")
wins = int(statistics[0])
draws = int(statistics[1])
losses = int(statistics[2])
# Call the calculate_league_points function
print(calculate_league_points(wins,draws,losses))

"""
input:4,1,2
output:16
"""
