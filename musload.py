import os
import re
import urllib2

directory = 'Output'

def findLink(song):
	print song
	query_string = 'search_query=' + song.replace(' ', '+')
	url = 'http://www.youtube.com/results?' + query_string
	h = urllib2.urlopen(url).read()
	r = re.findall(r'href=\"\/watch\?v=(.{11})', h)
	return 'http://www.youtube.com/watch?v=' + r[0]

def download(songs):
	for i in range(len(songs)):
		song = findLink(songs[i])
		print "sudo youtube-dl -citk " + song
		os.system("sudo youtube-dl -cit " + song)

def main():
	songs = []
	f = open('input.txt')
	while True:
		song = f.readline().strip()
		if song == '':
			break
		songs.append(song)
	f.close()
	if not os.path.exists(directory):
		os.makedirs(directory)
		os.chmod(directory, 0777)
	os.chdir(directory)
	download(songs)

if __name__ == "__main__":
	main()
