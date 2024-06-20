from transformers import pipeline
import pygame
import time

# Initialize sentiment analysis pipeline
sentiment_analysis = pipeline("sentiment-analysis")

# Emotion to song mapping with synonyms
emotion_to_song = {

    "happy": "E:/Users/Urooj Marvi/PycharmProjects/pythonProject/songs/Happy/bhudu sa mann .mp3",
    "enthusiasm": "E:/Users/Urooj Marvi/PycharmProjects/pythonProject/songs/Enthusiastic/y2mate.com - Badtameez Dil.mp3",
    "surprised": "E:/Users/Urooj Marvi/PycharmProjects/pythonProject/songs/Surprise/y2mate.com - What a wonderful world  Louis Armstrong  WhatsApp Status Instagram Story Twit.mp3",
    "confused": "E:/Users/Urooj Marvi/PycharmProjects/pythonProject/songs/Confusion or Anticipation/Kal Ho Naa Ho( Kal Ho Naa Ho ).mp3",
    "pressurize": "E:/Users/Urooj Marvi/PycharmProjects/pythonProject/songs/Pressurize/Kar Har Maidan Fateh .mp3",
    "motivated": "E:/Users/Urooj Marvi/PycharmProjects/pythonProject/songs/Motivation/Yeh Hosla.mp3",
    "fear": "E:/Users/Urooj Marvi/PycharmProjects/pythonProject/songs/fear/y2mate.com - Aankhen khuli ho ya ho band status  Black status video  whatsapp Status video.mp3",
    "love": "E:/Users/Urooj Marvi/PycharmProjects/pythonProject/songs/Love/Pehla Nasha Pehla Khumar.mp3",
    "neutral": "E:/Users/Urooj Marvi/PycharmProjects/pythonProject/songs/Neutral Mood/Bekhayali.mp3"
}
# "sad": "E:/Users/Urooj Marvi/PycharmProjects/pythonProject/songs/sad/Tum Hi Ho.mp3",
# Keyword dictionary for emotion detection
keyword_to_emotion = {
    "happy": ["happy", "joyful", "cheerful", "pleased"],
    "love": ["lovely", "romantic", "affection", "adoration"],
    "enthusiasm": ["enthusiastic", "excited", "eager", "passionate"],
    "surprised": ["surprised", "amazed", "astonished", "shocked"],
    "confused": ["confusion", "confused", "bewildered", "puzzled"],
    "pressurize": ["pressurize", "pressure", "stressed", "overwhelmed"],
    "motivated": ["motivated", "inspired", "determined", "driven"],
    "fear": ["fear", "fearful", "anxious", "terrified"],

}
#"sad": ["sad", "depressed", "melancholy"]
# "shameless": ["shameless", "shame", "guiltless", "unashamed"]

# Function to detect emotion based on user input
def detect_emotion(text):
    global emotion
    for emotion, keywords in keyword_to_emotion.items():
        #print(emotion)
        for keyword in keywords:
           # print(keyword)
            if keyword in text.lower():
                return emotion
                #print(emotion)
    return text # Default emotion if no keyword is found


# Function to play audio based on emotion
def play_audio(emotion):
    audio_file = emotion_to_song.get(emotion, "path/to/default_song.mp3")
    pygame.mixer.init()
    pygame.mixer.music.load(audio_file)
    pygame.mixer.music.play()

    # Wait for the audio to finish playing
    while pygame.mixer.music.get_busy():
        time.sleep(1)


# Main function to interact with the chatbot
def chatbot():
    print("Welcome to the Emotion-based Music Recommender!")
    while True:
        user_input = input("How are you feeling today? (Type 'quit' to exit): ")
        if user_input.lower() == 'quit':
            break

        else:
            emotion = detect_emotion(user_input)
            print(f"Detected emotion: {emotion}")

        play_audio(emotion)


# Run the chatbot
chatbot()
