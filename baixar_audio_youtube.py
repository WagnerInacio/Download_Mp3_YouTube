from pytube import YouTube
import moviepy.editor as mp
import re
import os

# Digite o link do video e o local que deseja salvar o mp3
link = input("Enter the link of the video you want to download: ")
path = input("Enter the directory where you want to save the file: ")
yt = YouTube(link)

# Comeca o Download
print("Downloading...")
ys = yt.streams.filter(only_audio=True).first().download(path)
print("Download Complete!")

# Converte para mp3
print('Converting file...')
for file in os.listdir(path):
    if re.search('mp4', file):
        mp4_path = os.path.join(path, file)
        mp3_path = os.path.join(path, os.path.splitext(file)[0]+'.mp3')
        new_file = mp.AudioFileClip(mp4_path)
        new_file.write_audiofile(mp3_path)
        os.remove(mp4_path)
print('Success!')
