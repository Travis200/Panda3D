import sys
import platform
import winsound


print("hello")


print( 1, sys.version )
print( 2, platform.python_implementation())
print( 3, sys.executable)

from math import pi, sin, cos

from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from direct.actor.Actor import Actor

class MyApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        # Load the environment model.
        self.scene = self.loader.loadModel("models/environment")
        #         # Reparent the model to render.
        self.scene.reparentTo(self.render)
        # Apply scale and position transforms on the model.
        self.scene.setScale(0.25, 0.25, 0.25)
        self.scene.setPos(-8, 42, 0)

        # This is how loaded the panda sound. I got this by manipulating the code
        # found on the panda3d website (https://www.panda3d.org/manual/?title=Loading_and_Playing_Sounds_and_Music)
        self.pandaSound = self.loader.loadSfx("panda_sound_2.wav")
        # Add the spinCameraTask procedure to the task manager.
        self.taskMgr.add(self.spinCameraTask, "SpinCameraTask")
        self.taskMgr.add(self.audio, "Panda Sound")
        # Load and transform the panda actor.
        self.pandaActor = Actor("models/panda-model",
                                {"walk": "models/panda-walk4"})
        self.pandaActor.setScale(0.005, 0.005, 0.005)
        self.pandaActor.reparentTo(self.render)
        # Loop its animation.
        self.pandaActor.loop("walk")

    # Define a procedure to move the camera.
    def spinCameraTask(self, task):
        angleDegrees = task.time * 6.0
        angleRadians = angleDegrees * (pi / 180.0)
        self.camera.setPos(20 * sin(angleRadians), -20.0 * cos(angleRadians), 3)
        self.camera.setHpr(angleDegrees, 0, 0)
        return Task.cont
    #This is how I got the panda sound to play constantly (not just once)
    def audio(self, task):
        if self.pandaSound.status() != self.pandaSound.PLAYING:
            self.pandaSound.play()
        return Task.cont

app = MyApp()
app.run()
