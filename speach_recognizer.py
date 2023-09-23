import speech_recognition as sr


class SpeechRecognizer:
    def __init__(self):
        pass
    def recognize_audio(self,audio_file):
        recognizer = sr.Recognizer()

        # Open the audio file and recognize speech
        with sr.AudioFile(audio_file) as source:
            audio_data = recognizer.record(source)
            text = recognizer.recognize_google(audio_data)
        return text