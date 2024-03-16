from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

ground = Entity(model="plane", texture='grass', scale=(2000,1,2000), collider="mesh")

playerModel = Entity(model="dodge.obj")

player = FirstPersonController( model = playerModel, scale=.5, collider='box')

player.speed = 7

camera.z = -7

app.run()
