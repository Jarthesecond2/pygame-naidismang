"""Game_stats"""
class GameStats():
    """Kontrolli mängu statistikat"""
    
    
    def __init__(self):
        """Installeeri statistikad"""
        self.game_active = False
        self.reset_stats()
        
    
    def reset_stats(self):
        """Installeeri skoor, mis saab muutuda mängu ajal"""
        self.score = 0
        self.level = 1
        self.bonus = 0