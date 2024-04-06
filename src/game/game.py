from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

if __name__ == '__main__':
    app = Ursina()

ground = Entity(model="map.obj", scale=1, collider="mesh")

playerModel = Entity(model="sphere")

player = FirstPersonController( model = playerModel, scale=.5, collider='box')

player.speed = 7

camera.z = -7


if __name__ == '__main__':
    app.run()