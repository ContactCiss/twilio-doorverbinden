from flask import Flask, request, Response
from twilio.twiml.voice_response import VoiceResponse, Dial

app = Flask(__name__)

@app.route("/doorverbinden", methods=["POST"])
def doorverbinden():
    response = VoiceResponse()
    # Dit bericht moet aan de beller worden verteld
    response.say("Een ogenblikje, ik verbind u nu door naar een medewerker.", language='nl-NL')
    
    # Het daadwerkelijke doorverbinden naar het juiste nummer
    response.dial("0031884114114", caller_id="+3197010252180")  # Twilio-nummer als caller_id
    return Response(str(response), mimetype='text/xml')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

print(f"POST-request ontvangen: {request.json}")
