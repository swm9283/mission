#8장
#문제 8.1
e2f = {"dog": "chien","cat": "chat","walrus": "morse"}
print(e2f)

#문제 8.2
print(e2f["walrus"])

#문제 8.3
# temp = list(e2f.items()) #길이가 3
# for i in range(0,3):
#     temp[i] = list(temp[i])
# # print(temp)
# for i in range(0,3):
#     temp[i][0], temp[i][1] = temp[i][1],temp[i][0]
# f2e = dict(temp)
# print(f2e)

# e2f = {"dog": "chien","cat": "chat","walrus": "morse"}
# f2e = {}
# for e2f_key,e2f_value in e2f.items():
#     f2e[e2f_value] = e2f_key
# print(f2e)

#comprehension
f2e = {a:b for b,a in e2f.items()}

#문제 8.4
key = list(f2e.keys())
print(key[0])

#문제 8.5
print(e2f.keys())
#문제 8.6
life = {"animals": {"cats": "Henri","octopi": "Grumpy","emus": "Lucy"},"plants": {}, "other": {}}
#문제 8.7
print(life.keys())

#문제 8.8
print(life["animals"])

#문제 8.9
print(life["animals"]["cats"])

#문제 8.10
squares = { i: i**2 for i in range(10)}
print(squares)





