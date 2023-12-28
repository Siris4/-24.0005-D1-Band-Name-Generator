def play_game():
    w = True
    while w == True:
        x = 0
        y = 100
        for new in range(x, y):
            print(new)
            if w == False:
                break
            elif new > 50:
                w = False

# play again? (function)
        zzz = input(f"Do you want to play again? (Y or N): ").upper()
        if zzz == "Y":
            return play_game()
        else:
            print("Okay!! Have a great rest of your day!")
            return False

play_game()