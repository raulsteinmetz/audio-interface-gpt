from playsound import playsound

def play_audio(file_path):
    playsound(file_path)

def example_usage():
    play_audio('../gpt.mp3')

if __name__ == '__main__':
    example_usage()
