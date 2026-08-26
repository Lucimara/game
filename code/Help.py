
from code.Const import WIN_WIDTH, WIN_HEIGHT, COR_BRANCA
from code.ScreenBase import ScreenBase

class Help(ScreenBase):
    def __init__(self, window):
        super().__init__('help', window, COR_BRANCA, (WIN_WIDTH / 2, WIN_HEIGHT / 2 + 254))
        self.window = window
