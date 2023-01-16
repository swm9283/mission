#mission 2
#문제 6.2
guess_me = 7
number = 10
while True:
    if number < guess_me:
        print("too low")
    elif number == guess_me:
        print("found it")
        break
    else:
        print("oops")
        break
    number = number +1
