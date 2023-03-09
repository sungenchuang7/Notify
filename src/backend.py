import datetime
import speech_recognition as sr

# create a recognizer object
r = sr.Recognizer()

# use the default microphone as the audio source
with sr.Microphone() as source:
    # adjust for ambient noise
    r.adjust_for_ambient_noise(source)
    
    # keep listening until the user stops recording
    print("Speak something... (or press 'q' to stop recording)")
    audio = r.listen(source)
    while True:
        try:
            # recognize speech using Google Speech Recognition
            text = r.recognize_google(audio)

            # write the text to a file
            with open('./../transcription.txt', 'a') as f:
                for sentence in text.split('.'):
                    sentence = sentence.strip()
                    if sentence:
                        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        f.write(f"{timestamp} - {sentence}.\n")
                print("Transcription saved to transcription.txt file.")
                
        except sr.UnknownValueError:
            print("Could not understand audio.")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
        
        # check if the user wants to stop recording
        stop = input("Press 'q' to stop recording, or any other key to continue...")
        if stop.lower() == 'q':
            break
        
        print("Reached here")
        # listen for the next audio input
        print("Speak something... (or press 'q' to stop recording)")
        audio = r.listen(source)
