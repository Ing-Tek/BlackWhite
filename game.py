import getpass

def roundCount(current_round):
    current_round += 1

def playerTurn(current_round, last_winner):
    if current_round == 1:
        return 1
    else:
        return last_winner

def bOrW(num):
    return "-------------\n흑" if num < 10 else "-------------\n백"

def numBar(used_num, max_num=99):
    num_left = max_num - used_num
    if num_left > 79:
        return "80 ~ 99\n-------------"
    elif num_left > 59:
        return "60 ~ 79\n-------------"
    elif num_left > 39:
        return "40 ~ 59\n-------------"
    elif num_left > 19:
        return "20 ~ 39\n-------------"
    else:
        return "0 ~ 19\n-------------"

def roundWinner(num1, num2, point1, point2):
    if num1 > num2:
        print("Player 1 wins the round!")
        point1 += 1
        print("score is " + str(point1) + " : " + str(point2))
        print("---------------Round End---------------\n\n")
        return point1, point2, 1
    elif num2 > num1:
        print("Player 2 wins the round!")
        point2 += 1
        print("score is " + str(point1) + " : " + str(point2))
        print("---------------Round End---------------\n\n")
        return point1, point2, 2
    else:
        print("Draw!")
        print("score is " + str(point1) + " : " + str(point2))
        print("---------------Round End---------------\n\n")
        return point1, point2, 0

def gameWinner(point1, point2, current_round, bonus_round=False):
    if bonus_round:
        if current_round == 3:
            if point1 > point2:
                print("Player 1 wins!")
                return False
            elif point2 > point1:
                print("Player 2 wins!")
                return False
            else:
                print("Draw!")
                return False
        elif point1 >= 2 or point2 >= 2:
            print("Player", 1 if point1 > point2 else 2, "wins!")
            return False
        elif current_round > 3:
            print("Draw!")
            return False
        else:
            return True
    else:
        if current_round == 9:
            if point1 > point2:
                print("Player 1 wins!")
                return False
            elif point2 > point1:
                print("Player 2 wins!")
                return False
            else:
                return 11
        elif point1 >= 5:
            print("Player 1 wins!")
            return False
        elif point2 >= 5:
            print("Player 2 wins!")
            return False
        else:
            return True

def game():
    current_round = 1
    current_player = 1
    used1 = 0
    used2 = 0
    point1 = 0
    point2 = 0
    max_num = 99
    bonus_round = False
    last_winner = 1
    last_winner_save = last_winner
    roundLog = {}

    while True:
        print("Round:", current_round)
        print("Player", current_player, "turn")

        if current_player == 1:
            num1 = int(getpass.getpass(prompt=f"Enter a number: "))
            if used1 == max_num:
                num1 = 0
            elif num1 > max_num - used1:
                num1 = max_num - used1
            print(bOrW(num1))
            used1 += num1
            level = numBar(used1, max_num)
            if level == "level 0":
                break
            print(level)
        else:
            num2 = int(getpass.getpass(prompt=f"Enter a number: "))
            if used2 == max_num:
                num2 = 0
            elif num2 > max_num - used2:
                num2 = max_num - used2
            print(bOrW(num2))
            used2 += num2
            level = numBar(used2, max_num)
            if level == "level 0":
                break
            print(level)

        if current_player == 1:
            num1 = int(getpass.getpass(prompt=f"Enter a number: "))
            if used1 == max_num:
                num1 = 0
            elif num1 > max_num - used1:
                num1 = max_num - used1
            print(bOrW(num1))
            used1 += num1
            level = numBar(used1, max_num)
            print(level)
        else:
            num2 = int(getpass.getpass(prompt=f"Enter a number: "))
            if used2 == max_num:
                num2 = 0
            elif num2 > max_num - used2:
                num2 = max_num - used2
            print(bOrW(num2))
            used2 += num2
            level = numBar(used2, max_num)
            print(level)


        print(f"{num2}")
        point1, point2, last_winner = roundWinner(num1, num2, point1, point2)
        if last_winner == 0:
            last_winner = last_winner_save
        else:
            last_winner_save = last_winner
        current_player = playerTurn(current_round, last_winner)
        roundLog[current_round] = [f"player1 : {num1} / {max_num - used1}", f"player2 : {num2} / {max_num - used2}", f"score {point1} : {point2}"]

        if gameWinner(point1, point2, current_round, bonus_round) == 11:
            print("Bonus Round!")
            print("Players will play 3 more rounds with 33 as the maximum number")
            current_round = 0
            point1 = 0
            point2 = 0
            max_num = 33
            bonus_round = True
        elif not gameWinner(point1, point2, current_round, bonus_round):
            last_winner = 1 if point1 > point2 else 2
            for round in roundLog:
                print(f"round {round}: {roundLog[round]}")
            break

        current_round += 1

game()
