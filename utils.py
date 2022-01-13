
import librosa
import librosa.display
from IPython.display import Audio
import matplotlib.pyplot as plt


def plot_audio(audio_file):
    data, sr = librosa.load(audio_file)
    # plt.figure(figsize=(12,4))
    # librosa.display.waveplot(data)
    # plt.show()
    return data


def plot_stft(audio_file):
    data, sr = librosa.load(audio_file)
    stft = librosa.stft(data)
    stft_db = librosa.amplitude_to_db(abs(stft))
    # plt.figure(figsize=(14, 6))
    # librosa.display.specshow(stft_db, sr=sr, x_axis='time', y_axis='hz')
    # plt.colorbar()
    # plt.show()
    return stft_db, stft


def FFT(audio_file, window_size):
    data, sr = librosa.load(audio_file)
    freqs = librosa.fft_frequencies(sr=sr, n_fft=window_size)
    return freqs

