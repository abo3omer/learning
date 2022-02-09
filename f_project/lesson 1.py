def f_age_program():
    name = input("please enter your name : ")
    porne = input("pleade enter your porne year : ")
    curent = input("please enter curent year : ")
    result = float(curent) - float(porne)
    print("Hellow Mr,Ms " + name.upper() + " your age is " + str(result) +
          " years old")


def elmax(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3


def maching(str1, str2):
    if str1 == str2:
        print("that is OK")
    else:
        print("that is not OK")


def cal():
    num1 = float(input("please enter firest number : "))
    operator = input("please enter the operator : ")
    num2 = float(input("please enter second number : "))
    if operator == "+":
        return (num1 + num2)
    elif operator == "-":
        return (num1 - num2)
    elif operator == "/":
        return (num1 / num2)
    elif operator == "*":
        return (num1 * num2)
    else:
        print("please enter correct operator")


# fac = ["ahmed", "mohamed", "mahmoud", "ashrafa"]
#
# for x in fac:
#     if x == "ashrafa":
#         print("good")
#         break
# else:
#     print("not good")


def gessing():
    coorect_word = "ahmed"
    gess_word = ""
    traying_count = 0
    max_traying = 3

    while gess_word != coorect_word and traying_count < max_traying:
        gess_word = input("enter correct word : ")
        traying_count += 1
        if traying_count <= max_traying and gess_word == coorect_word:
            print("you win")
        elif traying_count >= max_traying:
            print("gime over")


def guessing():
    na_1 = input("enter first name : ")
    na_2 = input("enter sacond name : ")
    na_3 = input("enter third name : ")
    na_4 = input("enter fourth name : ")

    list = {na_1, na_2, na_3, na_4}
    correct_word = list.pop()
    guess_word = ""
    traying_count = 0
    traying_limet = 3
    end_life = False

    while guess_word != correct_word and end_life == False:
        guess_word = input("enter gussing name : ")
        traying_count += 1
        if traying_count >= traying_limet:
            end_life = True

    if guess_word == correct_word and traying_count == 1:
        print("welldone your score is 50")
    elif guess_word == correct_word and traying_count == 2:
        print("welldone your score is 30")
    elif guess_word == correct_word and traying_count == 3:
        print("welldone your score is 10")
    else:
        print("gime over")


def power(base_num, power_num):
    result = 1
    for index in range(power_num):
        result = result * base_num
    return result


# num = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9],
#     [0]
# ]
# for row in num:
#     for cul in row:
#         print(cul*cul)