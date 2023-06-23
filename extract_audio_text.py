import numpy as np
import pandas as pd
import urllib.parse as urlparse
from youtube_transcript_api import YouTubeTranscriptApi

from pytube import YouTube
from audio_utils import Download


# link = "https://www.youtube.com/watch?v=1OaWeQ6Sw1Y&ab_channel=TheObamaWhiteHouse"
# Download(link)

# choose one from these
# speaker names = [Barack Obama, Donuld Trump, Elon Musk, Tom Cruise]
speaker_name = "Donuld Trump"

# insert youtube link here
link = "https://www.youtube.com/watch?v=woXcIdbjrT8&ab_channel=KUSINews"

video_save_dir = "./output/" +  speaker_name + "/"

# yt = Download(link, video_save_dir)

#############  extract audio  ###########
yt_audio = Download(link, video_save_dir, only_audio = True)

# get titie yt.default_filename
# print(yt.default_filename)

########## download transcript #######
url_data = urlparse.urlparse(link)
query = urlparse.parse_qs(url_data.query)
video_id = query["v"][0]
print(video_id)

srt = YouTubeTranscriptApi.get_transcript(video_id)
print(srt)

text_file = video_save_dir + yt_audio.default_filename + '_text'
with open(text_file, "w") as f:
   
        # iterating through each element of list srt
    for i in srt:
        # writing each element of srt on a new line
        f.write("{}\n".format(i))