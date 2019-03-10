import wave
import numpy as np




def open_wave(fn):
    '''Returns a tuple of sync_samples, data_samples, and sample_rate.'''
    wavefile = wave.open(fn, 'r')
    raw_data = wavefile.readframes(wavefile.getnframes())
    samples = np.fromstring(raw_data, dtype=np.int16)
    # try to use 128-bit float for the renormalization


    normed_samples = samples / np.float128(np.iinfo(np.int16).max)


    sync_samples = normed_samples[0::2]
    data_samples = normed_samples[1::2]


    # Need to invert these to match Matlab code for some reason


    return sync_samples, data_samples, wavefile.getframerate(), wavefile.getnchannels()




def convert_to_time_scale(signal, fs):
    '''
    Assume one dimensional signal
    fs: framerate
    signal: data_samples
    '''
    return np.linspace(0, np.floor(len(signal)/fs), num=len(signal))




def get_num_of_samples_per_pulse(Tp, fs):
    '''
    Tp: pulse time
    fs: sample freq
    '''
    return Tp * fs




# Can be used to create doppler vs. time plot data set here
def chunk_signal_by_time(signal, N):
    '''
    signal: data_samples
    N: # of samples per pulse


    @return: data_samples truncated for every N samples, samples/second
    '''
    sif = []
    indices = np.arange(0, len(signal), int(N))


    for i in range(len(indices)-1):
        sif.append(signal[indices[i]:indices[i+1]])
    return np.array(sif)




def obtain_dc_term(signal):
    return np.mean(signal)




def dbv(signal):
    return np.log10(np.abs(signal))
