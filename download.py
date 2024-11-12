from yt_dlp import YoutubeDL

# Create an audio downloader instance
audio_downloader = YoutubeDL({'format': 'bestaudio'})

while True:
    try:
        print('Youtube Downloader'.center(40, '_'))
        
        # Prompt user for the video URL
        URL = input('Enter the URL of the video: ')
        
        # Extract audio from the URL
        audio_downloader.download([URL])
        print("Audio has been successfully downloaded.")

    except Exception as e:
        print(f"Couldn't download the audio. Error: {e}")

    # Prompt user for the next action
    while True:
        try:
            option = int(input('\n1. Download again \n2. Exit\n\nOption here: '))
            if option in [1, 2]:
                break  # exit the inner loop if valid option is entered
            else:
                print("Please enter a valid option (1 or 2).")
        except ValueError:
            print("Invalid input. Please enter a number (1 or 2).")

    if option == 2:
        print("Exiting the program.")
        break

