import parselmouth

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set()

def plot_pitch(pitch):
    pitch_values = pitch.selected_array['frequency']
    # replace unvoiced samples by NaN to not plot
    # pitch_values[pitch_values==0] = np.nan
    # plt.plot(pitch.xs(), pitch_values,'o', markersize=5, color='w')
    # plt.plot(pitch.xs(), pitch_values,'o', markersize=4)
    
    avg_pitch = np.mean(pitch_values)

    plt.plot(pitch.xs(), pitch_values, label = 'Pitch')
    plt.axhline(y=avg_pitch, color='r', linestyle='-', label = 'Avg Pitch')
    # plt.plot(pitch.xs(), pitch_values,'o', markersize=4)

    plt.grid(True)
    plt.ylim(0, pitch.ceiling/2)
    plt.ylabel("Pitch in Hz")
    plt.xlabel("time in seconds")

filename = '0_obama.wav'
snd = parselmouth.Sound(filename)

pitch = snd.to_pitch()

print(pitch)

plt.figure()

plot_pitch(pitch)
plt.xlim([snd.xmin, snd.xmax])
plt.title('Pitch Contour')
plt.show()