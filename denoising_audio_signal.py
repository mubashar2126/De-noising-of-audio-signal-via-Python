import matplotlib.pyplot as plt
import numpy as np
from scipy.io import wavfile
import scipy.signal as sig

def filter_audio(input_audio_file, output_audio_file, cutoff_freq=[800, 1200], order=5):
    # Load the noisy audio signal
    sample_rate, y = wavfile.read(input_audio_file)

    # Convert to mono if the audio has multiple channels
    if len(y.shape) > 1:
        y = y.mean(axis=1)

    # Define bandpass filter parameters
    nyquist = 0.5 * sample_rate
    normalized_cutoff = [freq / nyquist for freq in cutoff_freq]

    # Design the bandpass filter
    b, a = sig.butter(order, normalized_cutoff, btype='band')

    # Apply the bandpass filter to the noisy signal
    filtered_signal = sig.lfilter(b, a, y)

    # Save the filtered audio signal
    wavfile.write(output_audio_file, sample_rate, np.int16(filtered_signal))

    return filtered_signal

# Example usage:
input_audio_file = 'mixkit-dial-error-tone-2871.wav'  # Input your audio file
output_audio_file = 'mixkit-dial-error-tone-2871_output.wav'  # Output Audio file

#For ploting input audio and finding sampling rate
sample_rate, audio_data = wavfile.read('mixkit-small-group-cheer-and-applause-518.wav')
print("Sampling Rate of input signal:", sample_rate)

#For ploting output audio and finding sampling rate
filtered_signal = filter_audio(input_audio_file, output_audio_file)
sample_rate, filtered_signal = wavfile.read('mixkit-small-group-cheer-and-applause-518_output.wav')
print("Sampling Rate of output signal:", sample_rate)

# Plotting input signal
plt.figure(figsize=(8, 6))
plt.subplot(2, 1, 1)
plt.plot(audio_data)
plt.title('Noisy Audio Signal')
plt.xlabel('Time(s)')
plt.ylabel('Amplitude')

# Plotting output signal
plt.subplot(2, 1, 2)
plt.plot(filtered_signal)
plt.title('Filtered Audio Signal')
plt.xlabel('Time(s)')
plt.ylabel('Amplitude')

plt.tight_layout()
plt.show()