# pig-dice-game

주사위를 던져 나온 숫자를 기록하여 특정 점수 이상을 얻은 사람이 이기는 게임

#### 게임 방법
```python
python pig_dice_game.py
```

- 총 n 명의 플레이어가 게임에 참가 
  - 1명의 유저 vs n-1명의 컴퓨터

1. 참가 인원 입력 
2. 사용자 이름 입력
3. 최종 승자를 결정한 타겟 점수 입력  
4. 주사위를 굴림 (랜덤)
    1. (2~6) 사이의 숫자가 나올 시 계속해서 주사위를 굴릴 것인지 (roll) 그동안 모아둔 값을 저장할지 (bank) 선택
        
        1. roll 선택시 주사위를 굴리고 값 축적
        2. bank 선택시 축적된 값 저장 후 해당 사용자 턴 종료
    
    2. 주사위의 값 1이면 해당 사용자 턴 종료 
 5. 4의 과정을 타겟 점수를 얻은 플레이어가 있을때까지 반복
 6. 승자가 결정 되면 게임을 반복할 것인지 선택
    1. Y 선택시 4의 과정 진행
    2. N 선택시 우승한 이력이 있는 플레이어의 우승 횟수 출력
   
#### 참고

- [GAME | pig dice game](https://www.mathsweek.ie/2021/games/pig.html)

- [DOCS | Optimal Play of the Dice Game Pig](https://cupola.gettysburg.edu/cgi/viewcontent.cgi?article=1003&context=csfac)