import pygame 
import psutil as ps 
import  sys
pygame.init()
screen = pygame.display.set_mode([320, 150])
pygame.display.set_caption('Live Cpu Usage')
def text(Fnt,size,txt,clr,corx,cory):
    font = pygame.font.Font(Fnt,size)
    txt = font.render(txt,True,clr)
    screen.blit(txt,(corx,cory))
while True:
    screen.fill((0,0,0))
    text('TarrgetAcademyRegular-ABEx.otf',30,str(ps.cpu_percent(interval=0.200)),(192,192,192),100,50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    pygame.display.update()
