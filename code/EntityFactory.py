from code.Backgound import Background
from code.Const import WIN_WIDTH


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str):
        match entity_name:
            case 'Level1BG':
                list_bg = []
                for i in range (10):
                    list_bg.append(Background(f'Level1BG{i}', (0,0)))
                    list_bg.append(Background(f'Level1BG{i}', (WIN_WIDTH, 0)))
                return list_bg
        return None

