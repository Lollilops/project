game_close = False
num_pos = 1
while not game_close:
    game_over = False
    if num_pos == 1:
        while not game_over:
            num_pos = int(input("1 \n"))
            if num_pos != 1:
                game_over = True
    if num_pos == 2:
        while not game_over:
            num_pos = int(input("2 \n"))
            if num_pos != 2:
                game_over = True
    if num_pos == 3:
        while not game_over:
            num_pos = int(input("3 \n"))
            if num_pos != 3:
                game_over = True
    if num_pos == 4:
        game_close = True
