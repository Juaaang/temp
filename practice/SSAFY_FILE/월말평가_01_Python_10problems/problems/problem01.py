# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
def average(scores):
    # 여기에 코드를 작성하여 함수를 완성합니다.
    
    # sumS : scores index들의 합, lenS = scores index들의 길이
    sumS = 0
    lenS = 0
    # scores 리스트를 돌면서
    for score in scores:
        #sumS에 score의 값을 더해주고
        sumS += score
        #lenS에 score의 인덱스 1개당 1을 카운트해서 길이를 구함
        lenS += 1
    # 합 / 길이로 나누어서 평균 리턴
    return sumS / lenS
        

# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
########## 코드 변경 금지 ############
if __name__ == '__main__':
    scores = [80, 90, 85, 75]
    print(average(scores))    # 82.5