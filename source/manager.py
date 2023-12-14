from pyray import *
from gameobject import *
from player import *

class Manager: # administras os objetos para a parte de "update" e de "drawing"
    
    gameobject_update_queue: list[GameObject] = []
    gameobject_draw_queue: list[GameObject] = []
    hud_draw_queue = []
    max_fps: int = 60
    pause: bool = False
    debug: int = 2
    # camera: Camera2D = ...

    def update_pause(self):
        if is_key_pressed(KeyboardKey.KEY_P): # <- checa se o jogo pediu para ser pausado
            manager.pause = not manager.pause # <- pausa ou despausa o jogo
            pass

        if manager.debug >= 1:
            print('Pause: ', manager.pause) # debug: mostra estado da variavel pausa

    def update_gameobjects(self):
        for item in self.gameobject_update_queue:
                item.update()

    def update(self):

        self.update_pause()

        ## define comportamento quando pausado em relação a update
        if not manager.pause: # se despausado
            self.update_gameobjects()
            pass
        else: # se pausado
            
            pass

        pass

    def draw_map(self):
        pass

    def draw_from_camera_2d(self):
        pass
        
    def draw_hud(self):
        if not manager.pause:
            
            pass
        else:
            draw_text("Paused:",20,20,20,RAYWHITE)

    def draw(self):

        ## printa relativo a camera2d
        self.draw_map()
        self.draw_from_camera_2d()
    
        for item in manager.gameobject_draw_queue: 
            item.draw()
            pass
        pass

        self.draw_hud()

        ## printa a HUD na tela

manager = Manager() # <- Singleton