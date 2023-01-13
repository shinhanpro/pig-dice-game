import play_game
from common import print_char_repeat ,user_input_n,user_input


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


play_game.play_game(n,target_score)
