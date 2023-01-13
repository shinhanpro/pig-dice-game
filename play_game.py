from random import randint
#n, target_score
    
def play_game(n,target_score):
    winner=0
    users_score=[0]*n # 사용자 수 만큼 유저 점수 리스트 생성
    i=0
    check=False
    while True:
        if check==True: #승자가 발생하면?
            print(f"winner는 {winner}입니다 (0=user,1~n=com)")
            break
        turn=i%n
        if(turn==0): #사용자 턴이라면?
            print(f"{turn}유저의 차례입니다.")
            print("check",check)
            print(f"{users_score[turn]}점 입니다")

        else: #컴퓨터 턴이라면?
            print(f"{turn}컴퓨터의 차례입니다.")
            print(f"{users_score[turn]}점 입니다")
        i+=1 #턴 변경을 위해 추가 
#play_game(3,20)       
    
