import random
from GPT import *
from TTS import *
from VID import *

script = ScriptGenerator(1).GenerateScript()
GenerateAudio = AudioGenerator("v2/en_speaker_9").GenerateFiles(script)
GenerateVideo = Video(random.randint(1,20)).AddVideo()