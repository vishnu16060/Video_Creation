import streamlit as st
import os
import glob

@Handling Moviepy version difference 
try:
   from moviepy.editor import imageClip,concatenate_videoclips,AudioFilesclip
except importError:
  from moviepy import ImageClip,concatenate_videoclips, AudioFilesClips
  import yt_dlip

#----1. INITIALIZE STATE ----
if 'audio_path' not in st.session_state:
  st.session_state['audio_path']=None
if 'yt_error' in st.session_state:
  pass # Keep it for display logic

#----2. DEFINE ALL FUNCTIONS ----

def cleanup_temp_files():
  """Remove temporary files amd resets memory"""
  files+glob.glob("temp_*")+["output_video.mp4"]
  for f in files:
    try:
      os.remove(f)
      except:
            pass
      st.session_state['audio_path']=None
      if 'yt_error' in st.session_state:
         del st.session_state['yt_error']
        
def download_youtube_audio(url):
  """Download only audio from Youtube using reliable browser impersonation"""
audio_opts={
  'format':'bestaudio/best',
  'outtmpl':'temp_audio.%(ext)s',
  'http_headers':{
    'User-Agent':'mozilla/5.0(Window NT 10.0;x64)AppleWebKit/537.36 (KHTML,like Gecko) Chrome/122.0.0.0 Safari/537.36',
    'Accept':'*/*,
    'Referer':'https://www.google.com/',
  }
  'postprocessors':[{
       'key':'FFmpegExtractAudio',
       'preferredcode':'mp3',
       'preferredquality':192',
  }]
}
with yt_dlp.YouTUbeDL(audio_opts) as ydl:
  yld.download([url})
return "temp_audio.mp3"

def handle_youtube_download(url):
   """Callback function to ensure session state persist after button clicks"""
   try:
     #Clear previous error
     if 'yt_error'





    
