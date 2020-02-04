from CoordSystem import *
import time

FPS = 60

def main():
    coordsys = CoordSystem(400, 500)
    
    running = True
    #thx alex from stackoverflow
    previousFrame = time.time()
    while running:
        currentFrame = time.time()
        dt = currentFrame - previousFrame
        sleepTime = 1./FPS - dt 
        if sleepTime > 0:
            time.sleep(sleepTime)
        lastFrameTime = currentFrame
        
        running = not coordsys.checkUserKeyClose()
        #game_logic(dt)

    coordsys.close()


def game_logic(dt):
    print("this is printing at 60 fps")


if __name__ == '__main__':
    main()
