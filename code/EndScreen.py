import pygame as pg
from code.Const import WIN_WIDTH, WIN_HEIGHT, COR_BRANCA
from code.TextUtils import draw_text

class EndScreen:
    def __init__(self, window, background_path: str):
        self.window = window
        self.surf = pg.image.load(background_path).convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self):
        while True:
            self.window.blit(self.surf, self.rect)

            # instrução
            draw_text(self.window,
                      "Press ESC or ENTER to return",
                      24,
                      COR_BRANCA,
                      (WIN_WIDTH / 2 - 330, WIN_HEIGHT / 2 - 270),
                      center=True)

            pg.display.flip()

            for event in pg.event.get():
                if event.type == pg.KEYDOWN:
                    if event.key in (pg.K_ESCAPE, pg.K_RETURN):
                        return True   # encerra e volta ao menu
                if event.type == pg.QUIT:
                    pg.quit()
                    quit()
