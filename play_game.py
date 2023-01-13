from random import randint
from common import print_char_repeat ,user_input_n,user_input
    
def play_game(n,target_score):
    winner=0
    users_score=[0]*n # 사용자 수 만큼 유저 점수 리스트 생성
    i=0
    check=False

    def user_loop_game(target_score):
        nonlocal winner
        nonlocal check
        while True:
            user_pick= input("주사위를 더 돌릴지 멈출지 선택하세요. (roll or bank): ")#roll or bank 입력 받기
            if user_pick=="roll":
                roll=randint(1,6)
                print(f"주사위 값은 {roll}입니다.")
                if roll==1:
                    users_score[turn]=0   
                    break
                else:
                    users_score[turn]+=roll
                    if users_score[turn]>=target_score:
                        winner=turn  
                        check=True
                        break             
            elif user_pick=="bank":
                break
    def com_loop_game(target_score):
        nonlocal winner
        nonlocal check
        while True:
            com_pick= randint(0,1)
            if com_pick==0:
                roll=randint(1,6)
                print(f"주사위 값은 {roll}입니다.")                    
                if roll==1:
                    users_score[turn]=0
                    break
                else:
                    users_score[turn]+=roll   
                    if users_score[turn]>=target_score:
                        check=True
                        winner=turn         
                        break                                                                 
            elif com_pick==1:
                break

    while True:
        print_char_repeat('-',40)
        if check==True: #승자가 발생하면?
            print(f"winner는 {winner}입니다 (0=user,1~n=com)")
            return winner
            break
        turn=i%n
        if(turn==0): #사용자 턴이라면?
            print(f"당신의 차례입니다!")
            user_loop_game(target_score)
            print(f"{users_score[turn]}점 입니다")

        else: #컴퓨터 턴이라면?
            print(f"{turn}번째 컴퓨터의 차례입니다.")
            com_loop_game(target_score)
            print(f"{users_score[turn]}점 입니다")
        i+=1 #턴 변경을 위해 추가
#play_game(3,20)       
    
