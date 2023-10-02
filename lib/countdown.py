# your code goes here!
# def countdown(number):
#     while number > 0:
#         print(f"{number} SECOND(S)!")
#         number -= 1
#     print("HAPPY NEW YEAR!")

# # Test case for the countdown function
# def test_countdown(capsys):
#     countdown(3)
#     captured = capsys.readouterr()
#     assert captured.out == "3 SECOND(S)!\n2 SECOND(S)!\n1 SECOND(S)!\nHAPPY NEW YEAR!\n"


import time

def countdown(number):
    while number > 0:
        print(f'{number} SECOND(S)!')
        number -= 1
    print("HAPPY NEW YEAR!")

def countdown_with_sleep(number):
    while number > 0:
        print(f'{number} SECOND(S)!')
        time.sleep(1)  # Add a one-second delay
        number -= 1
    print("HAPPY NEW YEAR!")
