from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

if __name__ == '__main__':
    app = Ursina()

ground = Entity(model="circuit.obj", scale=5, collider="mesh")

playerModel = Entity(model="sphere")

player = FirstPersonController( model = playerModel, scale=.5, collider='box')

player.speed = 7

camera.z = -7

def input(key):
    if key == 'escape':
        sys.exit()

if __name__ == '__main__':
    app.run()