#mission2.
#문제6.3
guess_me = 9
for number in range(10):
    if guess_me >9:
        print("oops")
        break
    if number < guess_me:
        print("too low")
    elif number == guess_me:
        print("found it",number)
        break








# elif number == guess_me:
#     print("found it")
#     break
# else:
#     print("oops")
#     break
