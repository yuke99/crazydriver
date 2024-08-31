import sys
import pygame
from pygame.locals import*

#게임의 색상 정의하기
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)

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

#게임 화면 초기화
screen = pygame.display.set_mode((500,800))

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
    #화면 업데이트
    pygame.display.update()
