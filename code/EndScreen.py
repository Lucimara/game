from code.Const import WIN_WIDTH, WIN_HEIGHT, COR_BRANCA
from code.ScreenBase import ScreenBase

class EndScreen(ScreenBase):
    def __init__(self, window, background_path: str):
        super().__init__(background_path, window, COR_BRANCA, (WIN_WIDTH / 2 - 10, WIN_HEIGHT / 2 + 100))
        self.window = window
