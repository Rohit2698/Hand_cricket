def login_user():
    print("WELCOME TO HAND CRICKET...")
    print("1.Start")
    print("2.See Record")
    print("3.exit")
    n = input("Select Choice")
    if n == "Start":
        team = input("Enter name of the Team = ")
        player = input("Enter total players u want = ")
        play_game(team, player)


def user_batting(x, y):
    score = 0
    wicket = 0
    comp_score = x
    player = y
    if comp_score == 0:
        while wicket < y:
            bat = int(input("Enter Run = "))
            if bat > 6:
                print("You cannot score more than 6 Runs in a ball")
            else:
                bowl = random.randint(1, 6)
                if int(bat) != int(bowl):
                    score = int(score) + int(bat)
                    print(str(score) + "/" + str(wicket))
                else:
                    print(" OUT !")
                    wicket += 1
    else:
        while wicket < player and score < comp_score:
            bat = int(input("Enter Run = "))
            if bat > 6:
                print("You cannot score more than 6 Runs in a ball")
            else:
                bowl = random.randint(1, 6)
                if int(bat) != int(bowl):
                    score = int(score) + int(bat)
                    print(str(score) + "/" + str(wicket))
                else:
                    print(" OUT !")
                    wicket += 1
    return score


def user_bowling(x, y):
    score = 0
    wicket = 0
    comp_score = x
    player = y
    if comp_score == 0:
        while wicket < player:
            bowl = input("Enter Run =")
            bat = random.randint(1,6)
            if int(bowl) != int(bat):
                score = int(score) + int(bat)
                print(str(score) + "/" + str(wicket))
            else:
                print(" OUT !")
                wicket += 1
    else:
        while wicket < player and score < comp_score:
            bowl = input("Enter Run =")
            bat = random.randint(1,6)
            if int(bowl) != int(bat):
                score = int(score) + int(bat)
                print(str(score) + "/" + str(wicket))
            else:
                print(" OUT !")
                wicket += 1
    return score


def play_game(team, player):
    plus = 0
    team_name = team
    players = int(player)
    print("Welcome for a toss " + str(team_name))
    print("1.odd  2.even")
    toss = input("enter odd or even = ")
    number = input("Enter number = ")
    number2 = random.randint(1, 6)
    print(number2)
    plus = int(number) + int(number2)
    print(plus)
    if plus % 2 != 0:
        temp = "odd"
    else:
        temp = "even"

    if toss != temp:
        print("You Lost the toss")
        choose = ['Batting', 'Bowling']
        select = random.choice(choose)
        print("Computer chosses" + str(select))
        if select == "Batting":
            print("User Coming for Bowling")
            comp_score = user_bowling(0, players)
            print("Computer Score =" + str(comp_score))
            print("User Coming for Batting")
            user_score = user_batting(comp_score, players)
            print("USER Score =" + str(user_score))
            if user_score > comp_score:
                print("USER WINS CONGRATULATION")
            else:
                print("COMPUTER WINS BETTER LUCK NEXT TIME!!!")
        else:
            print("USer Coming for Batting")
            user_score = user_batting(0, players)
            print("User Score =" + str(user_score))
            print("Computer Coming for Batting")
            comp_score = user_bowling(0, players)
            print("Computer Score =" + str(comp_score))
            if user_score > comp_score:
                print("USER WINS CONGRATULATIONS!!!!")
            else:
                print("COMPUTER WINS BEETER LUCK NEXT TIME!!!!")
    else:
        print("You won the toss")
        print("1. Batting   2.Bowling")
        choice = input("What do u want to do =")
        if choice == "Batting":
            print("User Coming for Batting")
            user_score = user_batting(0, players)
            print("User Score =" + str(user_score))
            print("COmputer Coming For Batting")
            comp_score = user_bowling(user_score, players)
            print("Computer Score =" + str(comp_score))
            if user_score > comp_score:
                print("USER WINS CONGRATULATIONS!!!!")
            else:
                print("COMPUTER WINS BETTER LUCK NEXT TIME!!!!")

        else:
            print("Computer Coming for Batting")
            comp_score = user_bowling(0, players)
            print("Computer Score =" + str(comp_score))
            print("User Coming For Batting")
            user_score = user_batting(comp_score, players)
            print("User Score =" + str(user_score))
            if user_score > comp_score:
                print("USER WINS CONGRATULATION")
            else:
                print("COMPUTER WINS BETTER LUCK NEXT TIME!!!")

import random
login_user()