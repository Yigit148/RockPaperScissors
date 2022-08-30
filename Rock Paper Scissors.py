
user1 = input("What's your name?")
user2 = input("And your name?")



print("For " + user1 + " a = rock, s = paper, d = scissors")
print("For " + user2 + " j= rock, k = paper, h = scissors")

a = j = "rock"
s = k = "paper"
d = h = "scissors"


user1_answer = input("do yo want to choose rock, paper or scissors?")
user2_answer = input("do you want to choose rock, paper or scissors?")



def compare(u1, u2):
    if u1 == u2:
        return("It's a tie!")
    elif u1 == a:
        if u2 == h:
            return("Rock wins!")
        else:
            return("Paper wins!")
    elif u1 == d:
        if u2 == k:
            return("Scissors win!")
        else:
            return("Rock wins!")
    elif u1 == s:
        if u2 == j:
            return("Paper wins!")
        else:
            return("Scissors win!")
    else:
        return("Invalid input! You have not entered rock, paper or scissors, try again.")

print(compare(user1_answer, user2_answer))

input("Please press Enter to exit")