from pyray import *


class Sprite:
    
    def __init__(self, image: str, destination: Vector2, rotation: float) -> None:
        """ inicia sem source """
        self.image = load_texture(image)
        self.source = Rectangle(0, 0, self.image.width, self.image.height)
        self.destination = Rectangle(destination.x, destination.y, self.image.width, self.image.height)
        self.origin = Vector2((self.image.width/2), (self.image.height/2))
        self.rotation = rotation
        self.color = RAYWHITE
        pass

    def draw(self) -> None:
        draw_texture_pro(self.image, self.source, self.destination, self.origin, self.rotation, self.color)
        pass

    pass