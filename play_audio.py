import pygame

def myplay(myaudio_path,times=1):
        fre = 22050
        si = 16
        ch = 2
        buf = 44100
        pygame.init()
        pygame.mixer.init()
	pygame.mixer.music.load(myaudio_path)
	pygame.mixer.music.play(times)
	while pygame.mixer.music.get_busy(): # if ommited no sound comes out
                pygame.time.Clock().tick(10)
	
def addQueue():
	pass

if __name__ == '__main__' :
        print 'start'
        myplay('/home/pi/my.mp3')
        print 'done'
