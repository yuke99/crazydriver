import sys,os,random
import pygame
from pygame.locals import*

#현재 위치
GAME_ROOT_FOLDER = os.path.dirname(__file__)
#이미지 폴더 위치 정의
IMAGE_FOLDER = os.path.join(GAME_ROOT_FOLDER, "Images")



#게임의 색상 정의하기
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)

#게임 변수 초기화 하기
moveSpeed = 5 #적의 움직이는 속도

#게임시작
#파이게임 초기화
pygame.init()

#프레임매니저 초기화
#파이게임의 time라이브러리에서 시계 클래스를 이용해 인스턴스(객체)를 만드는 과정
clock = pygame.time.Clock()
#프레임 레이트 설정, 1초에 60프레임 또는 그 이하로 화면을 업데이트
clock.tick(60)

#제목 표시줄 설정
pygame.display.set_caption("Crazy Driver")

#이미지 불러오기
IMG_ROAD = pygame.image.load(os.path.join(IMAGE_FOLDER, "Road.png"))
IMG_PLAYER = pygame.image.load(os.path.join(IMAGE_FOLDER, "Player.png"))
IMG_ENEMY = pygame.image.load(os.path.join(IMAGE_FOLDER, "Enemy.png"))


#게임 화면 초기화
screen = pygame.display.set_mode(IMG_ROAD.get_size())

#게임 객체 만들기
#플레이어 초기 위치 계산하기
h = IMG_ROAD.get_width()//2
v = IMG_ROAD.get_height() - (IMG_PLAYER.get_height()//2)
#player 스프라이트 만들기
player = pygame.sprite.Sprite() #sprite가 클래스를 만드는 것
player.image = IMG_PLAYER
player.surf = pygame.Surface(IMG_PLAYER.get_size())
player.rect = player.surf.get_rect(center=(h,v))

#적
#적의 초기 위치 계산하기
hl = IMG_ENEMY.get_width()//1 #가장 왼쪽에 위치하는 값
#가장 오른쪽에 위치 하는 값
hr = IMG_ROAD.get_width() - (IMG_ENEMY.get_width()//2)
h = random.randrange(hl,hr)
v = 0

#적 스프라이트 만들기
enemy = pygame.sprite.Sprite()
enemy.image = IMG_ENEMY
enemy.surf = pygame.Surface(IMG_ENEMY.get_size())
enemy.rect = enemy.surf.get_rect(center=(h,v))

"""
스프라이트 : 컴퓨터 그래픽에서 큰 이미지 위에 놓인 2차원 이미지
스프라이트는 표시하거나 숨길 수도 있고
움직이거나 회전하거나 다양한 방식으로 변형할 수도 있음.
게임에서 애니메이션과 움직임 등을 만드는 데 필요한 핵심 요소

자동차는 움직이니까 스프라이트로 만든다.
"""

#배경 색상 설정
screen.fill(WHITE)

#메인게임 루프
while True:
    #이벤트 확인
    #응답해야할 이벤트들을 리스트 형태로 반환하는데
    #이를 for 루프에 넣어 모든 이벤트를 대상으로 반복한다.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    #배경 이미지 그리기
    screen.blit(IMG_ROAD, (0,0))
    #플레이어 이미지 그리기
    screen.blit(IMG_PLAYER, player.rect)

    #키보드를 눌렀을 때
    keys = pygame.key.get_pressed()
    if keys[K_LEFT] and player.rect.left > 0:
        player.rect.move_ip(-moveSpeed,0)
    if keys[K_RIGHT] and player.rect.right <IMG_ROAD.get_width():
        player.rect.move_ip(moveSpeed,0)




    #적 이미지 그리기
    screen.blit(IMG_ENEMY, enemy.rect)

    #적을 아래쪽으로 움직이기
    enemy.rect.move_ip(0, moveSpeed)
    #move_ip : 스프라이트를 움직는 함수
    #(수평으로 움직이는 값, 수직으로 움직이는 값)

    if(enemy.rect.bottom>IMG_ROAD.get_height()):
        hl = IMG_ENEMY.get_width()
        hr = IMG_ROAD.get_width() - (IMG_ENEMY.get_width()//2)
        h = random.randrange(hl,hr)
        v = 0
        enemy.rect.center = (h,v)

    #충돌확인하기
    #player와 enemy의 스프라이트가 겹치는지를 확인
    #collide_rect() : 충돌 감지 함수
    if pygame.sprite.collide_rect(player, enemy):
        pygame.GameOver()


    #화면 업데이트
    pygame.display.update()
