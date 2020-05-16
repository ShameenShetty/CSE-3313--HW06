"""
    Name:   Shameen Shetty
    ID:     1001429743
"""

import numpy as np
import soundfile as sf
import matplotlib.pyplot as plt

def processFile(fn, offset) :
    # Reading from the .wav file and getting the data and sampleRate
    data, sampleRate = sf.read(fn)
    
    # We apply Fast Fourier Transform to the original data
    FFT_Signal = np.fft.fft(data)
    
    midPoint = int(len(FFT_Signal) / 2)

    # Here we are setting the values in the range of midpoint ± offset to 0
    for i in range(offset):
        after = midPoint + i
        before = midPoint - i

        FFT_Signal[after] = 0
        FFT_Signal[before] = 0

    # creating a new, cleaned signal by applying inverse FFT to modified FFT_Signal
    cleaned_Signal = np.fft.ifft(FFT_Signal)

    FFT_magnitude = []
    cleaned_FFT_magnitude = []

    # We are taking the magnitudes of the two arrays, because originally they are in complex form a+ib
    # which will not plot properly.
    for i in range(len(FFT_Signal)):
        FFT_magnitude.append(np.linalg.norm(FFT_Signal[i]))
        cleaned_FFT_magnitude.append(np.linalg.norm(cleaned_Signal[i]))

    # getting the real values from the array
    realArray = cleaned_Signal.real
    # finally we write cleanMusic.wav using the real part of the cleaned Signal and the sampleRate
    #  we got from the original audio.
    sf.write('cleanMusic.wav', realArray, sampleRate)

    # Plotting the 2 arrays side by side, hence 1 row and 2 cols.
    fig, axs = plt.subplots(nrows=1, ncols=2)
    axs[0].plot(FFT_magnitude)
    axs[1].plot(cleaned_FFT_magnitude)

    plt.show()


##############  main  ##############
if __name__ == "__main__":
    filename = "P_9_2.wav"
    offset = 12300 # original offset of 123 was too low, 12300 works properly (1230 is still not enough)

    # this function should be how your code knows the name of
    #   the file to process and the offset to use
    processFile(filename, offset)
