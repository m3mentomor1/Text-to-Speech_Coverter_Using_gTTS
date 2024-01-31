import os
from gtts import gTTS
from playsound import playsound

def text_to_speech(text):
    """
    Convert text to speech and play it directly.
    
    Args:
    - text (str): The text to convert to speech.
    """
    tts = gTTS(text=text, lang='en')
    tts.save("temp.mp3")    # Save to a temporary file
    print("\nPlaying audio...")
    playsound("temp.mp3")   # Play the temporary file
    os.remove("temp.mp3")   # Remove the temporary file after playing
    print("Audio playback complete.")

if __name__ == "__main__":
    text = input("Enter text: ")
    text_to_speech(text)
