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



def game_board(game_map, player=0, row=0, column=0):
    try:
        global played
        if game_map[row][column] !=0:
            print("This position is taken! Choose another")
            return False
        print("   0  1  2")
        if player != 0:
            game_map[row][column] = player
        for count, row in enumerate(game_map):
            print(count, row)
        played = True
        return game_map
    except:
        print("Something went wrong")
        return False


play = True
player = [1, 2]
while play:
    game = [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]
    game_won = False
    game = game_board(game)
    current_player = player[0]
    while not game_won:
        print(f"Current player: {current_player}")
        played = False
        while not played:
            column_choice = int(input("What column do you want to play (0, 1, 2): "))
            row_choice = int(input("What row do you want to play (0, 1, 2): "))
            game_board(game, current_player, row_choice, column_choice)
            win(game)
        if current_player == player[0]:
            current_player = player[1]
        else:
            current_player = player[0]
    play = int(input("Do you want to play again 0 no and 1 yes: "))

