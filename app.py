import speech_recognition as sr
import sounddevice as sd
import wavio as wv
import os

if ~os.path.isdir('files') :
    os.mkdir('files')

filename = "./files/audio1.wav"
freq = 44100
duration = 10
recording = sd.rec(int(duration * freq),
                   samplerate=freq, channels=2)
sd.wait()
wv.write(filename, recording, freq, sampwidth=2)


r = sr.Recognizer()


with sr.AudioFile(filename) as source:
    audio_data = r.record(source)
    text = r.recognize_sphinx(audio_data)
    print(text)
