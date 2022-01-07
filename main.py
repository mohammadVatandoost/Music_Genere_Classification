from MusicGenreClass import MusiceGenre
import glob
from pydub import AudioSegment
import random
from utils import plot_audio, plot_stft, FFT


def scanMusics():
    musicGenres = []
    musicGenres.append(MusiceGenre("Turkey", "./data/TUrkey", "./dataWav/TUrkey"))
    musicGenres.append(MusiceGenre("Kordi", "./data/Kordi", "./dataWav/Kordi"))
    musicGenres.append(MusiceGenre("Lori", "./data/Lori", "./dataWav/Lori"))
    musicGenres.append(MusiceGenre("Gilaki", "./data/Gilaki", "./dataWav/Gilaki"))
    for musicGenre in musicGenres:
        for file in glob.glob(musicGenre.path + "/*.mp3"):
            musicGenre.musics.append(file)
            musicGenre.converted.append(file.replace("mp3", "wav"))
        random.shuffle(musicGenre.converted)

    return musicGenres


def convert_MP3_To_Wav(musicGenres):
    for musicGenre in musicGenres:
        for music in musicGenre.musics:
            input = music
            output = music.replace("mp3", "wav")
            sound = AudioSegment.from_mp3(input)
            sound.export(output, format="wav")
    return musicGenres


def split_train_test(musicGenres):
    X = []
    Y = []
    for musicGenre in musicGenres:
        X = X + musicGenre.converted
        Y.extend(musicGenre.name for _ in range(len(musicGenre.converted)))
    c = list(zip(X, Y))
    random.shuffle(c)
    X, Y = zip(*c)
    X_train = X[0: int(0.7*len(X))]
    X_test = X[int(0.7*len(X)):]
    Y_train = Y[0:int(0.7 * len(Y))]
    Y_test = Y[int(0.7 * len(Y)):]
    return X_train, Y_train, X_test, Y_test


if __name__ == '__main__':
    print("Scanning ")
    musicGenres = scanMusics()
    # musicGenres = convert_MP3_To_Wav(musicGenres)

    X_train, Y_train, X_test, Y_test = split_train_test(musicGenres)
    data = plot_audio(X_train[0])
    stft_db, stft = plot_stft(X_train[0])
    freqs = FFT(X_train, 1024)




