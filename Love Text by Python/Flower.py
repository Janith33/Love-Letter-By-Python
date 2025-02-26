
import time
from threading import Thread
import sys

lyrics = [
    ("I just wondering what reaction you will show...", 0.09),
    ("Don't be afraid.. just trust you and me....", 0.09),
    ("I am not going to uncomfortable yourself....", 0.09),
    ("If I can not be with you, I am always watch at You and keep you comfortable and safe..", 0.09),
    
   

]

delays = [0, 5.0, 11.0, 17.0, 20.8]

def animate_text(text, delay=0.1):
    """Prints text character by character with a delay."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def sing_lyric(lyric, delay, speed):
    """Delays for the given time, then prints the lyric."""
    time.sleep(delay)
    animate_text(lyric, speed)

def sing_song():
    """Creates and starts multiple threads to sing the song."""
    threads = []
    for i in range(len(lyrics)):
        lyric, speed = lyrics[i]  # Correctly unpack lyrics
        t = Thread(target=sing_lyric, args=(lyric, delays[i], speed))
        threads.append(t)
        t.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":  # Corrected module check
    sing_song()
