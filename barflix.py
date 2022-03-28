# Print lyrics through console using Genius API
from lyricsgenius import Genius
import sys
from rofi import Rofi

# Use rofi to input the name of the song
def get_song_name():
    if sys.platform == 'linux' and len(sys.argv) == 1:
        return Rofi().text_entry('Song:')
    elif len(sys.argv) == 2:
        return sys.argv[1]
    else:
        return input("Song: ")

GENIUS_ACCESS_TOKEN = "OWfF26DSXEnhebfEWbolND_okE-oc0BSTzsbBcx34rIYmbgwVj6PqnhET9rfZNL4"
genius = Genius(GENIUS_ACCESS_TOKEN)
song = genius.search_song(get_song_name())

# Print song name
print(f"Result: {song.full_title}\n")

lyrics = song.lyrics
# Remove "Embed" and the number at the end of the lyrics
lyrics = lyrics.replace("Embed", "")
# Remove the three last digits at the end of the lyrics
lyrics = lyrics[:-3]
# Remove the first line of the lyrics
lyrics = "\n".join(lyrics.split("Lyrics")[1:])

print(lyrics)
