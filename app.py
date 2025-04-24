from flask import Flask, request, Response
from twilio.twiml.voice_response import VoiceResponse, Dial

app = Flask(__name__)

# Voeg deze regel toe om 404 niet te krijgen op de root route
@app.route("/", methods=["GET"])
def home():
    return "Flask is up and running"

@app.route("/doorverbinden", methods=["POST"])
def doorverbinden():
    response = VoiceResponse()
    response.say("Een ogenblikje, ik verbind u nu door naar een medewerker.", language='nl-NL')
    response.dial("0031884114114", caller_id="+3197010252180")  # Je Twilio-nummer
    return Response(str(response), mimetype='

