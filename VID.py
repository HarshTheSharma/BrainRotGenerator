import moviepy.editor as mp
import os
class Video:
    def __init__(self, fileSelect):
        self.fileSelect = fileSelect

    def AddVideo(self):
        video = mp.VideoFileClip("vid" + str(self.fileSelect) + ".mp4")
        audio = mp.AudioFileClip("temp1.wav")
        # Get the duration of the audio file
        audio_duration = audio.duration

        # Loop the video until the audio is complete
        while video.duration < audio_duration:
            video = mp.concatenate_videoclips([video, video])

        # Set the audio of the video
        final = video.set_audio(audio)
        final = final.subclip(0, audio_duration)
        # Write the final video file
        final.write_videofile("BrainRot.mp4")
        os.remove("temp1.wav") 
        return 0