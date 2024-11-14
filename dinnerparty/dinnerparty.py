import random

def count_my_friends():
    """count of my friends who go to the party"""
    count_fr = int(input("Enter the num of friends: >"))
    if count_fr <=0:
        print("No one is joining for the party")
        return 1 #only you 8-)
    else:
        return count_fr + 1 # +you 8-)

#-------------------------------

def fr_list(count_fr):
    """add friednds name to dict and balance eq 0"""
    friends = {}
    #empty list
    print("Enter the name of every friend , each on a new line:")
    for _ in range(count_fr):
        name = input("> ")
        friends[name] = 0
    return friends
#----------------------------
def split_bill(friends):
    """Split the bill for friends."""
    total_bill = float(input("Enter the bill summ: "))
    #float - bill with coins )
    split_bill = round(total_bill / len(friends), 2)
    for name in friends:
        friends[name] = split_bill
    return friends
#----------------------
def choose_lucky(friends):
    """Random selects lucky friend."""
    answ = input("Do you want use 'Who is lucky, today?' Write Yes or No: ")
    if answ.lower() == "yes":
        lucky = random.choice(list(friends.keys()))
        print(f"{lucky} is the lucky one!")
        return lucky
    else:
        print("Have not lucky friends")
        return None
#--------------------
def bill_minus_lucky(friends, lucky):
    """bill with friend who pay 0 """
    if lucky:
        amount_to_pay = round(sum(friends.values()) / (len(friends) - 1), 2)
        for name in friends:
            friends[name] = amount_to_pay if name != lucky\
                else 0
    return friends
#--------------------------

count_fr = count_my_friends()
friends = fr_list(count_fr)
print(friends)
#--------------------------
friends = split_bill(friends)
print(friends)
#--------------------------
lucky_one = choose_lucky(friends)
friends = bill_minus_lucky(friends, lucky_one)
print(friends)
