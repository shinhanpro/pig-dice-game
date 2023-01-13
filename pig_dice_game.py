def print_char_repeat(char,num):
    chars=''
    for _ in range(num):
        chars+=char
    print(chars)


def user_input_n(msg):
    try :
        n=int(input(f"{msg:^32}"))
        return n
    except ValueError:
        return user_input_n(msg)

def user_input(msg):
    user_str=input(f'{msg:^32}')
    return  user_str

def game_opening():
    print_char_repeat('-',40)
    print(f"{'Pig Dice Game에 오신걸 환영합니다':^32}")
    print_char_repeat('-',40)
    n=user_input_n('참여할 인원을 입력해주세요 ex) 7(숫자) \n > ')
    print_char_repeat('-',40)
    user_name= user_input('당신의 이름을 알려주세요 ex) MEME \n> ')
    print_char_repeat('-',40)
    target_score=user_input_n('목표 점수를 입력해주세요 ex) 50 \n > ')
    print_char_repeat('-',40)
    return (n,user_name,target_score)


# 게임 오프닝 화면 출력
n,user_name,target_score=game_opening()
