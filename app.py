ffrom flask import Flask, request, Response, redirect
from twilio.twiml.voice_response import VoiceResponse, Dial, Say
import os

app = Flask(__name__)

@app.route("/start", methods=["POST"])
def start_call():
    # Vereenvoudigde versie zonder ElevenLabs API-aanroep
    response = VoiceResponse()
    response.say("Verbinding wordt gemaakt met een AI-assistent.", language='nl-NL')
    # Hier zou je je eigen werkende AI WebSocket setup koppelen
    return Response(str(response), mimetype='text/xml')

@app.route("/doorverbinden", methods=["POST"])
def doorverbinden():
    # Deze route wordt aangeroepen als AI zegt dat er moet worden doorverbonden
    response = VoiceResponse()
    response.say("Een ogenblikje, ik verbind u nu door naar een medewerker.", language='nl-NL')
    response.dial("0031884114114", caller_id="+31907010252180")
    return Response(str(response), mimetype='text/xml')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
