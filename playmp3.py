from pygame import mixer
def musicplay(file,stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play() 
    while True:
        a=input("Write stop to stop music\n")
        mixer.music.stop()
        break
if __name__=='__main__':
    musicplay("water.mp3","stop")
