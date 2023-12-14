from pyray import *
from manager import *
from body import *

def main():
    
    init_window(800,800,"UwU")

    """ init-area (begin) """

    set_target_fps(manager.max_fps) # <- trava em 60 FPS para facilitar
    body_test = Body(
        '/home/knichian/Documents/1-active_interests/3-game_design/2-progression_journey/testing_playground/taty_quest/atempt3/resources/hero_128.png',
        Vector2(400, 400),
        True,
        10,
        None
    )

    """ init-area (end) """

    while not window_should_close(): # <- Game-Loop

        """ Update-area (begin) """
        manager.update()
        if manager.pause:
            pass
        else:
            body_test.update()
            pass

        """ Update-area (end) """

        
        """ Drawing-area (begin) """
        begin_drawing() # começa a editar o back buffer (desenha o proximo frame)
        clear_background(DARKGRAY) # <- limpa o ultimo frame com a cor especificada

        manager.draw()
        body_test.draw()
        
        end_drawing() # termina de editar o back buffer e passa para o front buffer  (exibe o desenhado frame)
        """ Drawing-area (end) """

    close_window()
    
    

if __name__ == "__main__":
    main()
