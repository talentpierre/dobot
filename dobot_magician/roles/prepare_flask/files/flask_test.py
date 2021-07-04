from flask import Flask, render_template_string, request
from time import sleep
from gpiozero import LED
#import RPi.GPIO as GPIO


up = LED(4)
down = LED(23)
left = LED(24)
right = LED(25)

app = Flask(__name__)

#HTML Code

TPL = '''
<html>
    <head><title>Web Page Controlled Stepper</title></head>
    <body>
    <h2> Web Page to Control Stepper</h2>
        <img style="-webkit-user-select: none;margin: auto;background-color: hsl(0, 0%, 25%);" src="http://192.168.100.107:8081/">
        <form method="POST" action="doup">
            <h5> Up  </h5>
            <input type="submit" value="submit" />
        </form>

        <form method="POST" action="dodown">
            <h5> Down  </h5>
            <input type="submit" value="submit" />
        </form>

        <form method="POST" action="doleft">
            <h5> Left  </h5>
            <input type="submit" value="submit" />
        </form>

        <form method="POST" action="doright">
            <h5> Right  </h5>
            <input type="submit" value="submit" />
        </form>
    </body>
</html>


'''

@app.route("/")
def home():

    return render_template_string(TPL)


@app.route("/doup", methods=["POST"])
def up_action():
    down.off()
    up.on()

    return render_template_string(TPL)

@app.route("/dodown", methods=["POST"])
def down_action():
    up.off()
    down.on()

    return render_template_string(TPL)

@app.route("/doleft", methods=["POST"])
def left_action():
    right.off()
    left.on()

    return render_template_string(TPL)

@app.route("/doright", methods=["POST"])
def right_action():
    left.off()
    right.on()

    return render_template_string(TPL)

# Run the app on the local development server
if __name__ == "__main__":
    app.run(host="0.0.0.0")



