import random
import sys

import pygame as pg

delta = {
    pg.K_UP: (0, -1),
    pg.K_DOWN: (0, +1),
    pg.K_LEFT: (-1, 0),
    pg.K_RIGHT: (+1, 0)

}

def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((1600, 900))
    clock = pg.time.Clock()
    bg_img = pg.image.load("ex02/fig/pg_bg.jpg")
    kk_img = pg.image.load("ex02/fig/3.png")
    kk_img = pg.transform.rotozoom(kk_img, 0, 2.0)
    bb_img = pg.Surface((20,20))
    pg.draw.circle(bb_img, (255, 0, 0), (10, 10), 10)  #  赤い円を描く
    bb_img.set_colorkey((0, 0, 0))  #  黒い部分を削除する
    x, y = random.randint(0,1600), random.randint(0, 900)
    screen.blit(bb_img, [x, y])
    vx, vy = +1, +1
    bb_rect = bb_img.get_rect()  #rectクラスを定義
    bb_rect.center = x, y  # 中心位置をランダムに設定
    kk_rect = kk_img.get_rect()
    kk_rect.center = 900, 400
    tmr = 0

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return 0

        tmr += 1

        key_lst = pg.key.get_pressed()
        for k, mv in delta.items():
            if key_lst[k]:
                kk_rect.move_ip(mv)
        screen.blit(bg_img, [0, 0])
        screen.blit(kk_img, kk_rect)
        bb_rect.move_ip(vx, vy)
        screen.blit(bb_img, bb_rect)


        pg.display.update()
        clock.tick(1000)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()