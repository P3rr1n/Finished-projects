def win(current_game):
    global game_won
    # Horizontal
    for row in game:
        all_match = True
        if row.count(row[0]) == len(row) and row[0] != 0:
            print(f"Player {row[0]} is the winner horizontally (-)!")
            game_won = True
    # Diagonal
    daigs = []
    for ix in range(len(game)):
        daigs.append(game[ix][ix])
    if daigs.count(daigs[0]) == len(daigs) and daigs[0] != 0:
        print(f"Player {daigs[0]} is the winner diagonally (\\)!")
        game_won = True

    down_daigs = []
    for ix in range(len(game)):
        down_daigs.append(game[ix][len(game) - ix - 1])
    if down_daigs.count(down_daigs[0]) == len(down_daigs) and down_daigs[0] != 0:
        print(f"Player {down_daigs[0]} is the winner diagonally (/)!")
        game_won = True
    # Vertical
    for col in range(len(game)):
        check = []

        for row in game:
            check.append(row[col])

        if check.count(check[col]) == len(check) and check[col] != 0:
            print(f"Player {check[0]} is the winner vertically (|)!")
            game_won = True
