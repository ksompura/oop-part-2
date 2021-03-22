#"model" data from spotify playlist into a dictionary
playlist = {
	"title": "80s Rock Anthems", "creator": "Spotify",
	"song": [
	{"title":"You Shook Me All Night Long", "artist":["AC/DC"], "duration":3.5},
	{"title":"You Spin Me Round (Like a Record)", "artist":["Dead or Alive"], "duration":3.4},
	{"title":"Everbody Wants To Rule The World", "artist":["Tears For Fears"], "duration":4.2}]
}

#Print song titles of the playlist
for song in playlist['song']:
	print(song['title'])

#Find total duration
total_length = 0

for song in playlist['song']:
	total_length += song['duration']

print(total_length)