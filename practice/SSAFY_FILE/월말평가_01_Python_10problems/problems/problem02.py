# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
# python 내장함수 min, max 사용 금지
def min_max(scores):
    # scores 안의 값들끼리 비교하기 때문에 scores의 0번째 인덱스를 초기값으로 설정
    minS = scores[0]
    maxS = scores[0]
    #scores range를 돌면서 scores의 인덱스들과 minS, maxS와 비교하여 조건에 해당하면
    #그 값을 할당연산자를 통해 할당해줌
    for score in range(len(scores)):
        if minS >= scores[score]:
            minS = scores[score]
        if maxS <= scores[score]:
            maxS = scores[score]
    # , 를 통해 tuple 형태로 리턴
    return minS, maxS
    # 여기에 코드를 작성하여 함수를 완성합니다.


# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
########## 코드 변경 금지 ############
if __name__ == '__main__':
    scores = [80, 90, 85, 75]
    print(min_max(scores))    # (75, 90)
