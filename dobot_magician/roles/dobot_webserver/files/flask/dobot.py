from flask import Flask, render_template, request, jsonify
from time import sleep
from gpiozero import LED
#import RPi.GPIO as GPIO
import sys
import os
sys.path.insert(0, os.path.abspath('.'))

from lib.dobot import Dobot

bot = Dobot('/dev/ttyUSB0')

print('Bot status:', 'connected' if bot.connected() else 'not connected')

pose = bot.get_pose()
print('Pose:', pose)


app = Flask(__name__)

@app.route("/")
def index():
    
    return render_template('index.html')

@app.route("/doup", methods=["POST"])
def up_action():
    print('Moving to absolute coordinate')
    bot.move_to_relative(0, 0, +10, 0)    
    return jsonify({'result' : 'success', 'member_number' : 'Up'})

@app.route("/dodown", methods=["POST"])
def down_action():
    print('Moving to absolute coordinate')
    bot.move_to_relative(0, 0,-10, 0)
    return jsonify({'result' : 'success', 'member_number' : 'Down'})
    
@app.route("/doleft", methods=["POST"])
def left_action():
    print('Moving to absolute coordinate')
    bot.move_to_relative(0, +20, 0, 0)
    return jsonify({'result' : 'success', 'member_number' : 'Left'})
    
@app.route("/doright", methods=["POST"])
def right_action():
    print('Moving to absolute coordinate')
    bot.move_to_relative(0, -20, 0, 0)
    return jsonify({'result' : 'success', 'member_number' : 'Right'})
    
@app.route("/doforward", methods=["POST"])
def forward_action():
    print('Moving to absolute coordinate')
    bot.move_to_relative(+10, 0, 0, 0)
    return jsonify({'result' : 'success', 'member_number' : 'Forward'})
    
@app.route("/dobackward", methods=["POST"])
def backward_action():
    print('Moving to absolute coordinate')
    bot.move_to_relative(-10, 0, 0, 0)
    return jsonify({'result' : 'success', 'member_number' : 'Backward'})

# Run the app on the local development server
if __name__ == "__main__":
    app.run(host="0.0.0.0")



