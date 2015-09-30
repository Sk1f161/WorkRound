from urllib.request import urlopen
import json
import os
#os.mkdir('~/VKMusic')

## API запрос
## https://api.vk.com/method/'''METHOD_NAME'''?'''PARAMETERS'''&access_token='''ACCESS_TOKEN'''
#address = 'https://api.vk.com/method/audio.get?owner_id=17455416&access_token=b3e0c0902ccc2e57534bcd4cce7a766c195b53b7d944e7df9611cd3cdea019809703aa44f5fe4b108aa40'
address = 'https://api.vk.com/method/audio.search?q=%27Metallica%27&auto_complete=1&sort=2&count=10&access_token=b3e0c0902ccc2e57534bcd4cce7a766c195b53b7d944e7df9611cd3cdea019809703aa44f5fe4b108aa40'

data = urlopen(address)
decoded_response = data.read().decode()
final_data = json.loads(decoded_response)
songs = final_data['response'][1:]
for song in songs:
       song_artist = song['artist']
       song_title = song['title']
       song_url = song['url']
       #cached_song = urlopen(song_url).read()
       #if song_artist not in os.listdir('~/VKMusic'):
    #          os.mkdir('~/VKMusic/%s' %(song_artist))
     #  filename = '~/VKMusic/%s/%s.mp3' %(song_artist, song_title)
       #file = open(filename, 'wb')
       #file = open('vkmusic.m3u', 'a')
       print(song_title)
       #file.write(song_url + '\n')
       #file.close()
