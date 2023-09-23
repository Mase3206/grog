import csv, yaml, settings, audioParser, episodeParser, videoParser, filterParser
from audioParser import getAudioTrackCommand as audio
from episodeParser import getEpisodeCommand as episode
from videoParser import getVideoCommand as video
from filterParser import getFilterCommand as filtr
from dimensionParser import getDimensionCommand as dim





def allEpisodes(numberOfEpisodes, episodeNumber):
	episodes = []
	episodeParameters = []
	audioParameters = []

	# set this for each series
	rawSettings, prettySettings = settings.getSettings(False)

	numberOfAudioTracks = int(rawSettings['Audio Track Quantity'])
	HandBrakeCLI_execLocation = rawSettings['HandBrakeCLI Executible Location']
	environment = rawSettings['Environment']


	# open csv of episodes to rip
	with open(''.join([rawSettings['Episode Output Directory'], '/episode_list.csv']), 'r') as csvfile1:
		episodeList = csv.reader(csvfile1, delimiter=',')

		for row in episodeList:
			episodes.append(row)


	# assemble full command
	
	episodeParameters = episode(episodes[episodeNumber])
	if episodeParameters != False:
		fullCommand = audio(numberOfAudioTracks) + episodeParameters + video() + filtr() + dim()
	else:
		fullCommand = False

	return fullCommand


if __name__ == '__main__':
	#print('\nThis program is not meant to be run directly. Please instead call the functions within this program from another.\nExiting...\n')
	#exit(0)

	print('\n', allEpisodes(5, 3), '\n')