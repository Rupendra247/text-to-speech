# test to speech library
# pip install gTTS
from gtts import gTTS

text = "Hello everyone, welcome to the test to speech library using gTTS in Python. This library allows you to convert text into speech easily."

# Create a gTTS object
tts = gTTS(text=text, lang='en')    

tts.save("voice.mp3")  # Save the speech to a file

print("audio saved")