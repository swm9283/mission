pokemons= [["피카츄", 200], ["파이리", 100], ["꼬부기", 90], ["거북왕", 30], ["망나뇽", 15]]

#위치를 찾아야돼.

def add_friends(data):
    len_pokemons = len(pokemons)
    pokemons.append(data)
    for i in range(len_pokemons-1,-1,-1):
        if data[1] >= pokemons[i][1]:
            pokemons[i + 1] = pokemons[i]
            pokemons[i] = data

    return pokemons
def question():
    name = input("포켓몬 도감에 추가할 포켓몬을 입력하세요. :")
    number = int(input("포켓몬의 체력을 입력하세요. : "))
    data = [name,number]
    return data
if __name__ == "__main__":
    pokemons = [["피카츄", 200], ["파이리", 100], ["꼬부기", 90], ["거북왕", 30], ["망나뇽", 15]]
    while True:
        option = input("1) 포켓몬 추가 생성  2) 포켓몬 추가 종료 : ")
        if option == "1":
            data = question()
            pokemons = add_friends(data)
            print(f" 결과 :{pokemons} , 추가한 data : {data} ")

        elif option == "2":
            print("프로그램이 종료 되었습니다.")
            break
        else:
            print("옵션에서 선택해주세요.")








