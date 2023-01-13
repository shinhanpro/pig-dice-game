def game_opening():
    print_char_repeat('-',40)
    print(f"{'Pig Dice Game에 오신걸 환영합니다':^32}")
    print_char_repeat('-',40)

def print_char_repeat(char,num):
    chars=''
    for _ in range(num):
        chars+=char
    print(chars)



# 게임 오프닝 화면 출력
game_opening()
