from SwSpotify import spotify
import lyricsgenius
import requests
import shutil
import cv2
import numpy as np
from os import path



def getInfoFromSpotify():
	infos = spotify.current()
	return infos

def getLyricsFromGenius(infos):
	genius = lyricsgenius.Genius("aB69pIhzYcyDWRinNp2_dR_zHdJ9-S8gmvLT2linGvAnXdJkXOhV1S85Z9sBz-Y5")
	song = genius.search_song(infos[0], infos[1])
	return song.to_dict()

def downloadAlbumArt(url):
	home_path = path.dirname(path.realpath(__file__))
	r = requests.get(url, stream=True)
	if r.status_code == 200:
		with open(home_path[:-4] + 'Assets/cover.jpg', 'wb') as f:
			r.raw.decode_content = True
			shutil.copyfileobj(r.raw, f)

def blurThisImagePlease(file):
	img = cv2.imread(file)
	img = cv2.blur(img,(5,5))
	hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
	hsv[...,2]=hsv[...,2]*0.6
	img = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
	cv2.imwrite(file,img)
