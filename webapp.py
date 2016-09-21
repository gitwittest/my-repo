from flask import Flask
from sound import *

app = Flask(__name__)

@app.route('/')
def home() :
	return 'Welcome home' , 200
	
	
@app.route('/task')
def homeT() :
	firstTest.delay('hello.txt')
	return 'Task starting in the background' , 200

@app.route('/mysic')
def sound() :
	playTrack.delay('/home/pi/my.mp3')
	return 'playing ...' , 200
	
if __name__ == '__main__':
	app.run(debug=True)
