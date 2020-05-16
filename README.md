# CSE-3313--HW06
This is the coding assignment for Homework 6 for CSE3313 (Introduction to Signal Processing), there are 2 coding assignment questions for this assignment - the first one is **Noise Removal using FFT** and the second is **Image Processing**


## Purpose for first coding question: Noise Removal using FFT
Learn how to display the spectrum of an audio file and how changing some of thespectrum components can be used to remove noise from an audio file.  
Sometimes we wish to identify frequencies, or range of frequencies, present in a signal and alter their amplitude. For this we can produce the DFT of a signal.  
 We will write a program that reads an audio file that contains noise and use the DFTto remove the noise.


### Process for first coding question: Noise Removal using FFT
* Read from file *P_9_2.wav* which is a wav file that contains a piece of music that has been corrupted with noise.  

To remove the noise we will:  
* Apply the FFT `np.fft.fft()` function to the signal
* Find the index of the midpoint of the FFT values
* Choose an offset and then set the values in the range of midpoint ± offset to 0. Make sure that the number of values on each side of the midpoint that you change are the same.
* (We assume that N is even)
* Create a new, cleaned signal by applying the inverse FFT (see np.fft.ifft()) to the modified FFT values.
* Create two subplots, side-by-side. The left plot will be the magnitude of the FFT values from the original audio file. The right plot will be the magnitude of the FFT values after removing the noise frequencies.
* Note: Since our process will create some non-real values, we will use the real part of the `ifft()` function return.
* Finally we write the result into a file called *cleanMusic.wav*


## Purpose for second coding question: Image Processing
*  Learn to use correlation to find an image within another image.
* Gain more experience with image preprocessing. 

We sometimes wish to find a signal within a larger signal. This is particularly challenging in the presence of noise. One approach to solving this is to find the cross-correlation of the smaller signal to the larger signal, where the largest correlation value represents the best fit.  
An applicaton of this is in image processing when we wish to locate a small image within a larger image. This process is called *template matching*.

### Process for second coding question: Image Processing
* In order to perform template matching we will use the `match_template()` function in the library *skimage.feature*. The image we are searching for is *ERBwideColorSmall.jpg* and the template being searched for is *ERBwideTemplate.jpg*.
* Once we find the  location within the larger image that the template best matches,  
  i. We replace that block of pixels in the larger image with zeros. That is, once you find the smaller image within the larger image, make that block of pixels black.  
  ii. Display the new image with the black box in its own figure window.  
