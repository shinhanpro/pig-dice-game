def print_char_repeat(char,num):
    chars=''
    for _ in range(num):
        chars+=char
    print(chars)


def user_input_n():
    try :
         n=int(input("참여할 인원을 입력해주세요 ex) 7 > "))
         return n
    except ValueError:
        print('* 숫자만 입력해주세요\n')
        user_input_n()


def game_opening():
    print_char_repeat('-',40)
    print(f"{'Pig Dice Game에 오신걸 환영합니다':^32}")
    print_char_repeat('-',40)

    n=user_input_n()



# 게임 오프닝 화면 출력
game_opening()
