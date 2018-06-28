import subprocess
import sys

subprocess.run(['./ffmpeg/bin/ffmpeg', '-i', 'ffmpeg/bin/video-test.mp4','-r', '5/1' ,'ffmpeg/bin/frames/%03d.png'])