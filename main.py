# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from MusicGenreClass import MusiceGenre
import glob
from pydub import AudioSegment



def scanMusics():
    musicGenres = []
    musicGenres.append(MusiceGenre("Turkey", "./data/TUrkey", "./dataWav/TUrkey"))
    musicGenres.append(MusiceGenre("Kordi", "./data/Kordi", "./dataWav/Kordi"))
    musicGenres.append(MusiceGenre("Lori", "./data/Lori", "./dataWav/Lori"))
    musicGenres.append(MusiceGenre("Gilaki", "./data/Gilaki", "./dataWav/Gilaki"))
    for musicGenre in musicGenres:
        for file in glob.glob(musicGenre.path + "/*.mp3"):
            musicGenre.musics.append(file)
    return  musicGenres


def convert_MP3_To_Wav(musicGenres):
    for musicGenre in musicGenres:
        for music in musicGenre.musics:
            input = music
            output = music.replace("mp3", "wav")
            sound = AudioSegment.from_mp3(input)
            sound.export(output, format="wav")
            musicGenre.converted.append(output)
    return musicGenres


if __name__ == '__main__':
    musicGenres = scanMusics()
    musicGenres = convert_MP3_To_Wav(musicGenres)

