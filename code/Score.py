
from code.Const import WIN_WIDTH, WIN_HEIGHT, COR_LARANJA
from code.ScreenBase import ScreenBase

# Ainda não implementei score

class Score(ScreenBase):
    def __init__(self, window):
        super().__init__('score', window, COR_LARANJA, (WIN_WIDTH / 2, WIN_HEIGHT / 2 + 254))
        self.window = window

    def save(self, menu_opcao: str, player_score: list[int]):
        pass
    def show_score(self):
        pass