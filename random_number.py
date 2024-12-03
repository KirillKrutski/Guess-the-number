import random

number_of_the_system = random.randint(1, 100)

your_trying = 0

while True:
    your_number = int(input("Search number 1-100: "))
    your_trying += 1
    if your_number < number_of_the_system:
        print("So small")
    elif your_number > number_of_the_system:
        print("So big")
    else:
        print(f"Congratulation! You win! Attempts - {your_trying}")
        break