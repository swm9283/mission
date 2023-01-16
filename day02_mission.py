#mission 2
# 체리는 작고 녹색이 아니다
# 완두콩은 작고 녹색이다
# 수박은 크고 녹색이다
# 호박은 크고 녹색이 아니다
# small = True
# green = True
import random
small = random.choice([True,False]) #리스트에서 랜덤하게 선택한다
green = random.choice([True,False]) #리스트에서 랜덤하게 선택한다


if small:
    if green:
        print("pea")
    else:
        print("cherry")
else:
    if green:
        print("watermelon")
    else:
        print("pumpkin")

