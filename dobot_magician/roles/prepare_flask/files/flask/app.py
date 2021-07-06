from flask import Flask, render_template, request, jsonify
from time import sleep
from gpiozero import LED
#import RPi.GPIO as GPIO


up = LED(4)
down = LED(23)
left = LED(24)
right = LED(25)

app = Flask(__name__)

@app.route("/")
def index():
    
    return render_template('index.html')

@app.route("/doup", methods=["POST"])
def up_action():
    
    return jsonify({'result' : 'success', 'member_number' : 'Up'})

@app.route("/dodown", methods=["POST"])
def down_action():
    
    return jsonify({'result' : 'success', 'member_number' : 'Down'})
    
@app.route("/doleft", methods=["POST"])
def left_action():
    
    return jsonify({'result' : 'success', 'member_number' : 'Left'})
    
@app.route("/doright", methods=["POST"])
def right_action():
    
    return jsonify({'result' : 'success', 'member_number' : 'Right'})
    
@app.route("/doforward", methods=["POST"])
def forward_action():
    
    return jsonify({'result' : 'success', 'member_number' : 'Forward'})
    
@app.route("/dobackward", methods=["POST"])
def backward_action():
    
    return jsonify({'result' : 'success', 'member_number' : 'Backward'})

# Run the app on the local development server
if __name__ == "__main__":
    app.run(host="0.0.0.0")



