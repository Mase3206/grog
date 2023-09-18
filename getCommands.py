import csv, yaml, audioParser, episodeParser, videoParser, settings


if __name__ == '__main__':
	print('\nThis program is not meant to be run directly. Please instead call the functions within this program from another.\nExiting...\n')
	exit(0)


def allEpisodes(numberOfEpisodes, episodeNumber):
	episodes = []
	episodeParameters = []
	audioParameters = []

	# set this for each series
	rawSettings, prettySettings = settings.getSettings(False)

	numberOfAudioTracks = int(rawSettings['Audio Track Quantity'])
	HandBrakeCLI_execLocation = rawSettings['HandBrakeCLI Executible Location']
	presetLocation = rawSettings['Preset Location']
	environment = rawSettings['Environment']


	# use dfferent paths for Windows/Unix
	if environment == 'Unix':
		# open csv of episodes to rip
		with open('Episodes/episode_list.csv', 'r') as csvfile1:
			episodeList = csv.reader(csvfile1, delimiter=',')

			for row in episodeList:
				episodes.append(row)
	elif environment == 'Windows':
		# open csv of episodes to rip
		with open('Episodes\\episode_list.csv', 'r') as csvfile1:
			episodeList = csv.reader(csvfile1, delimiter=',')

			for row in episodeList:
				episodes.append(row)
	else:
		raise ValueError('Environment variable set to illegal value in `settings.yml`. Only "Windows" and "Unix" are accepted values.')


	# assemble full command
	
	audioParameters = audioParser.getAudioTrackCommand(numberOfAudioTracks)
	episodeParameters = episodeParser.getEpisodeCommand(episodes[episodeNumber])
	videoParameters = videoParser.getVideoCommand()

	commandPrefix = [HandBrakeCLI_execLocation, '--preset-import-file', presetLocation]

	if episodeParameters != False:
		fullCommand = commandPrefix + audioParameters + episodeParameters + videoParameters
	else:
		fullCommand = False

	if __name__ == '__main__':
		print('\n', fullCommand, '\n')
	elif __name__ != '__main__':
		return fullCommand
