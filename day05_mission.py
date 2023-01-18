#mission
#문제 8.11
odd_number = {odd for odd in range(10) if odd % 2 == 1}
print(odd_number)

#문제 8.12
#generator를 잘이해하지 못함
#generator : object
#generator를 만드는 방식 중 하나가 generator comprehension
aids = (f'Got {i}' for i in range(10)) #generator comprehension
for aid in aids:
    print(aid)

#문제 8.13
key = "optimist", "pessimist","troll"
val = "the glass is half full","the glass is half empty","How did you get a glass?"
handmade_dictionnary = dict(zip(key,val))
print(handmade_dictionnary)

#문제 8.14
titles = ["Creature of Habit","crewel Fate"]
plots = ["A nun turns into a monster", "A haunted yarn shop"]
movies = dict(zip(titles,plots))
print(movies)

#문제 9.1
def good():
    print(["Harry","Ron","Hermione"])
good()