from pyray import *
from manager import manager
from gameobject import *
from sprite import *
from mind import *


class Body(GameObject):

    def __init__(self, sprite_path: str, position: Vector2, solid: bool, speed: int, mind: Mind) -> None:
        manager.gameobject_update_queue.append(self)
        manager.gameobject_draw_queue.append(self)
        self.sprite: Sprite = Sprite(sprite_path, position, 0)
        self.solid: bool = solid
        self.mind: Mind = mind
        self.speed: int = speed
        pass

    def move(self, x, y):
        self.sprite.destination.x += x
        self.sprite.destination.y += y
        pass

    def update(self):
        if is_key_down(KeyboardKey.KEY_W):
            self.move(0, (-self.speed))
        if is_key_down(KeyboardKey.KEY_S):
            self.move(0, (self.speed))
        if is_key_down(KeyboardKey.KEY_A):
            self.move((-self.speed), 0)
        if is_key_down(KeyboardKey.KEY_D):
            self.move((self.speed), 0)
        pass

    def draw(self):
        self.sprite.draw()
        pass

    pass