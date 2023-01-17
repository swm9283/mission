#7장
#문제 7.1
years_list = list(range(1999,2005))
#문제 7.2
print(years_list[2])
#문제 7.3
print(years_list[-1])
#문제 7.8
surprise = ["Groucho","Chico","Harpo"]
#문제 7.9
surprise[-1] = surprise[-1].lower()
# 첫 번째 방식.
# surprise_harpo_list=list(surprise[-1])
# surprise_harpo_list.reverse()
# surprise_harpo_string = "".join(surprise_harpo_list).title()
# surprise[-1] = surprise_harpo_string
# print(surprise)

#두 번째 방식
# surprise[-1] = surprise[-1].lower()
# surprise[-1] = surprise[-1][::-1].title()
# print(surprise)

#세 번째 방식
surprise[-1] = surprise[-1].lower()
surprise_reverse = " "
for i in  surprise[-1]:
    surprise_reverse = i + surprise_reverse
surprise[-1] = surprise_reverse.title()
print(surprise)

#문제 7.10
even_list = [even for even in range(11) if even % 2 ==0]
print(even_list)

#문제 7.11
start1 = ["fee","fie","foe"]
rhymes = [("flop", "get a mop"),("fope","turn the rope"),("fa","get your ma"),("fudge","call the judge"),("fat","pet the cat"),
          ("fog","walk the dog"),("fun","say we're done")]
start2 = "Someone better"
for i in range(len(rhymes)):
    print(f"{start1[0].title()}! {start1[1].title()}! {start1[2].title()}! {rhymes[i][0].title()}!")
    print(f"{start2} \t {rhymes[i][1]}.")
