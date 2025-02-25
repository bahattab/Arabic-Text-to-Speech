from flask import Flask, request, send_file
from gtts import gTTS
import os

app = Flask(__name__)

@app.route('/tts', methods=['POST'])
def text_to_speech():
    data = request.json
    text = data.get("text", "")
    
    if not text:
        return {"error": "No text provided"}, 400

    # Convert text to speech
    tts = gTTS(text=text, lang="ar")
    filename = "output.mp3"
    tts.save(filename)

    return send_file(filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
