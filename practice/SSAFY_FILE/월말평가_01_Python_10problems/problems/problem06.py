# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
def over_24(people):
    # 여기에 코드를 작성하여 함수를 완성합니다.
    #cnt 선언 및 0 할당
    cnt = 0
    # people range를 돌면서 people의 인덱스에서 ['age']키로 접근
    # 조건문에 해당하면 카운트
    for idx in range(len(people)):
        if  people[idx]['age'] > 24:
            cnt += 1
    return cnt


# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
########## 코드 변경 금지 ############
if __name__ == '__main__':
    people = [
        {'name': '김싸피', 'age': 25},
        {'name': '이싸피', 'age': 28},
        {'name': '조싸피', 'age': 29},
        {'name': '아싸피', 'age': 23},
        {'name': '최싸피', 'age': 22},
        {'name': '고싸피', 'age': 21},
        {'name': '유싸피', 'age': 26},
        {'name': '후싸피', 'age': 20},
    ]

    print(over_24(people))  # 4