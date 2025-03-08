import numpy as np
import matplotlib.pyplot as plt

import scipy.io.wavfile as wavfile
from scipy.io.wavfile import read

file_name = 'ascend_scale.wav'

samplerate, sound=read(file_name)

from scipy.io.wavfile import write

write("original_sound.wav", samplerate, sound.astype(np.int16)) # reescreve o áudio original


file=open("message.txt",'w')
np.savetxt(file,sound,delimiter=',', fmt='%d')
file.close()
