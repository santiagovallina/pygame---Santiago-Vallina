import pygame as pg

from models.constantes import (
    ALTO_VENTANA, ANCHO_VENTANA, FPS
)
from models.player.main_player import Jugador
from models.villian.main_villian import Villian


screen = pg.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
pg.init()
clock = pg.time.Clock()


back_img = pg.image.load('./assets/img/background/estadio.jpg')
back_img = pg.transform.scale(back_img, (ANCHO_VENTANA, ALTO_VENTANA))




juego_ejecutandose = True

player = Jugador(0, 0, frame_rate=70, speed_walk=20, speed_run=30)
villano = Villian(0, 0, frame_rate=70, speed_walk=20, speed_run=30)


while juego_ejecutandose:
    
    #print(delta_ms)
    lista_eventos = pg.event.get()
    for event in lista_eventos:
        match event.type:
            # case pg.KEYDOWN:
            #     # if event.key == pg.K_SPACE:
            #     #     player.shoot_laser(True)
            case pg.QUIT:
                print('Estoy CERRANDO el JUEGO')
                juego_ejecutandose = False
                break
        
    
    lista_teclas_presionadas = pg.key.get_pressed()
    if lista_teclas_presionadas[pg.K_RIGHT] and not lista_teclas_presionadas[pg.K_LEFT]:
        player.walk('Right')

    if lista_teclas_presionadas[pg.K_LEFT] and not lista_teclas_presionadas[pg.K_RIGHT]:
        player.walk('Left')

    if not lista_teclas_presionadas[pg.K_RIGHT] and not lista_teclas_presionadas[pg.K_LEFT]:
        player.stay()

    
    if lista_teclas_presionadas[pg.K_RIGHT] and lista_teclas_presionadas[pg.K_LSHIFT] and not lista_teclas_presionadas[pg.K_LEFT]:
        player.run('Right')
    if lista_teclas_presionadas[pg.K_LEFT] and lista_teclas_presionadas[pg.K_LSHIFT] and not lista_teclas_presionadas[pg.K_RIGHT]:
        player.run('Left')
    
    if lista_teclas_presionadas[pg.K_UP] :
        player.jump('Up')
    

    
    
    screen.blit(back_img, back_img.get_rect())
    delta_ms = clock.tick(FPS)
    player.update(delta_ms)
    player.draw(screen)
    villano.update(delta_ms)
    villano.draw(screen)
    pg.display.update()

pg.quit()