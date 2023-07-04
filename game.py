import getpass

def roundCount(current_round):
    current_round += 1

def playerTurn(current_player):
    if current_player == 1:
        return 2
    else:
        return 1

def bOrW(num):
    if num < 10:
        return "-------------\n흑"
    else:
        return "-------------\n백"

def numBar(used_num):
    num_left = 99 - used_num
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
        return point1, point2
    elif num2 > num1:
        print("Player 2 wins the round!")
        point2 += 1
        print("score is " + str(point1) + " : " + str(point2))
        return point1, point2
    else:
        print("Draw!")
        print("score is " + str(point1) + " : " + str(point2))
        return point1, point2

def gameWinner(point1, point2, current_round):
    if current_round == 9:
        if point1 > point2:
            print("Player 1 wins!")
            return False
        elif point2 > point1:
            print("Player 2 wins!")
            return False
        else:
            print("Round points are equal after 9 rounds!")
            print("Each player receives 33 points and plays 3 more rounds.")
            point1 = 33
            point2 = 33
            return True
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

    while True:
        print("Round:", current_round)
        print("Player", current_player, "turn")
        
        if current_player == 1:
            num1 = int(getpass.getpass(prompt=f"Enter a number: "))
            if used1 == 99:
                num1 = 0
            print(bOrW(num1))
            used1 += num1
            level = numBar(used1)
            if level == "level 0":
                break
            print(level)
        else:
            num2 = int(getpass.getpass(prompt=f"Enter a number: "))
            if used2 == 99:
                num2 = 0
            print(bOrW(num2))
            used2 += num2
            level = numBar(used2)
            if level == "level 0":
                break
            print(level)

        current_player = playerTurn(current_player)

        if current_player == 1:
            num1 = int(getpass.getpass(prompt=f"Enter a number: "))
            if used1 == 99:
                num1 = 0
            print(bOrW(num1))
            used1 += num1
            level = numBar(used1)
            print(level)
        else:
            num2 = int(getpass.getpass(prompt=f"Enter a number: "))
            if used2 == 99:
                num2 = 0
            print(bOrW(num2))
            used2 += num2
            level = numBar(used2)
            print(level)

        point1, point2 = roundWinner(num1, num2, point1, point2)

        if not gameWinner(point1, point2, current_round):
            break

        current_round += 1

game()