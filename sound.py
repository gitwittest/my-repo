from celery import Celery
from play_audio import myplay

mycel_app = Celery('sound',broker='redis://localhost:6379/0')

@mycel_app.task
def firstTest(name):
	f = open(name,'a')
	f.write('hi')
	f.close
	print 'done'
	
@mycel_app.task
def playTrack(path):
        myplay(path)
	print 'done'
	

@mycel_app.task
def first(name):
	print 'done'+name

if __name__ == '__main__':
	firstTest('hello.txt')		
