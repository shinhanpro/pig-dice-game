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