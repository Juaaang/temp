# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
def caesar(word, n):
    # 여기에 코드를 작성하여 함수를 완성합니다.
    word = input()
    n = input()
    rlt = ""
    for idx in range(len(word)):
        new_word = ord(word[idx]) + int(n)
        if (chr(new_word).islower() and new_word > 122) or (chr(new_word).isupper() and new_word > 90):
            new_word -= 26
        rlt += chr(new_word)
    return rlt  
    


# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
########## 코드 변경 금지 ############
if __name__ == '__main__':
    print(caesar('apple', 5))      # fuuqj
    print(caesar('ssafy', 1))      # ttbgz
    print(caesar('Python', 10))    # Zidryx
