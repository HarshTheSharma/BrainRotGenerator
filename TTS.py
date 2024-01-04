import os
from scipy.io.wavfile import write as write_wav
from pydub import AudioSegment
import nltk
import numpy as np

os.environ["CUDA_VISIBLE_DEVICES"] = "0"
os.environ["SUNO_USE_SMALL_MODELS"] = "1"
os.environ["SUNO_OFFLOAD_CPU"] = "1"
from bark.generation import (
    generate_text_semantic,
    preload_models,
)
from bark.api import semantic_to_waveform
from bark import generate_audio, SAMPLE_RATE
preload_models()

class AudioGenerator:
    def __init__(self, speaker):
        self.speaker = speaker

    def GenerateFiles(self, script):
        i = 1
        sentences = nltk.sent_tokenize(script)
        for sentence in sentences:
            filename = "temp" + str(i) + ".wav"
            audioArray = generate_audio(sentence, history_prompt=self.speaker)
            write_wav(filename, SAMPLE_RATE, audioArray)
            if i > 1:
                sound1 = AudioSegment.from_wav("temp1.wav")
                sound2 = AudioSegment.from_wav("temp2.wav")
                combinedSounds = sound1 + sound2
                combinedSounds.export("temp1.wav", format="wav")
                os.remove("temp2.wav") 
            i = 2
