import speech_recognition as sr
import datetime

r = sr.Recognizer()
m= sr.Microphone()

def detect():
    print("A moment of silence, please...")
    with m as source: r.adjust_for_ambient_noise(source)
    print("Set minimum energy threshold to {}".format(r.energy_threshold))
    f = sr.AudioFile(r"C:/Users/158612/OneDrive - Arrow Electronics, Inc/Desktop/audio project")
    with m as source:
        print("Speak something...", datetime.datetime.now())
        # listen for audio input from the microphone
        start = datetime.datetime.now()
        audio_data_my = r.listen(source)
    # write the recorded audio to a WAV file
    print("recording the file....")
    with open("recorded_audio.wav", "wb") as f:
        f.write(audio_data_my.get_wav_data())

    # print(audio_data_my)

    # use the recognizer to transcribe the audio
    text = r.recognize_google(audio_data_my)
    print("sending data..", datetime.datetime.now())
    end = datetime.datetime.now()
    print("text:", text)
    print("starting time: ", start)
    print("ending time: ", end)
detect()



