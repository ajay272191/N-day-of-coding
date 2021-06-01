#converting mp3 -> wav file
import subprocess
subprocess.call(['ffmpeg', '-i', 'audio.mp3','audio.wav'])
