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

def result_print(winner_list,cnt,user_name):
    print_char_repeat('-',40)
    print(f"총 {cnt}번 게임을 진행하셨습니다.")
    for k,v in winner_list.items():
        if k==0:
            print_char_repeat('*',40)
            print(f"{user_name} 게임에 {v}번  승리하였습니다.")
            print_char_repeat('*',40)
            continue
        print(f"{k} 번째 컴퓨터는 게임에 {v}번 승리하였습니다.")