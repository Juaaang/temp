# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
def calculator(*numbers):
    # 여기에 코드를 작성하여 함수를 완성합니다.
    # 입력값을 list화 해준 input_V 선언
    input_V = list(map(int, input().split()))
    # input_L : input_V의 길이
    input_L = len(input_V)

    # 0보다 큰 양의 정수가 들어오지 않으면 '양의 정수를 입력하세요' 문구 리턴
    for idx in range(len(input_V)):
        if input_V[idx] <= 0:
            return '양의 정수를 입력하세요'

    # 입력값이 없으면 0 리턴
    if input_L == 0:
        return 0

    # 입력값이 1개일때 인덱스가 1개이므로 원의 넓이 공식을 이용해 리턴
    if input_L == 1:
        return (input_V[0]**2) * 3.14
    
    # 입력값이 2개일때 입력값의 합에 따라 조건을 나누고 각자 식에 대입하여 리턴
    if input_L == 2:
        if (input_V[0] + input_V[1]) % 2:
            return (input_V[0] * input_V[1]) / 2
        else:
            return input_V[0] * input_V[1]
    
    # 입력값이 3개보다 크다면 (합, 평균) 형태의 튜플로 반환
    if input_L >= 3:
        return sum(input_V), sum(input_V) / input_L

# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
########## 코드 변경 금지 ############
if __name__ == '__main__':
    print(calculator(5))                # 78.5
    print(calculator(10, 20))           # 200
    print(calculator(10, 20, 30, 40))   # (100, 25.0)
    print(calculator())                 # 0