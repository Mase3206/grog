import yaml, settings

# EXPECTED OUTPUT
# ["-i", "disks/c1d1.iso", "-t", "3", "-c", "1-6", "-o", "Episodes/Season-1/C1D1T3_S1E1 - Tourist Trapped.mkv", "-f", "av_mkv", "-m"]

if __name__ == '__main__':
	print('\nThis program is not meant to be run directly. Please instead call the functions within this program from another.\nExiting...\n')
	exit(0)



global fileFormat, fileExtension, environment
with open('profiles/defaultVideo.yml', 'r') as file2:
	defaultVideo = yaml.safe_load(file2)
fileFormat = defaultVideo['Summary']['Format']
fileExtension = defaultVideo['Summary']['Extension']

rawSettings, prettySettings = settings.getSettings(False)
environment = rawSettings['Environment']


"""if environment == 'Unix':
		# code
	elif environment == 'Windows':
		# code
	else:
		raise ValueError('Environment variable set to illegal value in `settings.yml`. Only "Windows" and "Unix" are accepted values.')"""


def makeDiskName(episode):
	if environment == 'Unix':
		# Unix file path
		diskName = ['disks/c', episode[0], 'd', episode[1], '.iso']
		return ''.join(diskName)
	elif environment == 'Windows':
		# Windows file path
		diskName = ['disks\\c', episode[0], 'd', episode[1], '.iso']
		return ''.join(diskName)
	else:
		raise ValueError('Environment variable set to illegal value in `settings.yml`. Only "Windows" and "Unix" are accepted values.')
	



	


def makeFileName(episode, episodeData):
	episodeFileName = [rawSettings['Episode Output Directory'], '/Season-', episodeData['Season'], '/C', episode[0], 'D', episode[1], 'T', episode[2], '_S', episodeData['Season'], 'E', episodeData['Episode'], ' - ', episodeData['Name'], fileExtension]


	# make sure all elements are strings
	for i in range(len(episodeFileName)):
		episodeFileName[i] = str(episodeFileName[i])

	return ''.join(episodeFileName)


def joinArgs(episodeData, sortedListEpisodeData):
	defaultArgs = ['-i', '', '-t', '', '-c', '', '-o', '', '-f', '']
	newArgs = defaultArgs
	
	for i in range(len(sortedListEpisodeData)):
		newArgs[i*2+1] = sortedListEpisodeData[i]
	
	if episodeData['Keep Chapters'] == True:
		newArgs.append('-m')
	
	return newArgs


def getEpisodeInformation(episode):
	with open(makeEpisodeFile(episode), 'r') as file1:
		episodeInformation = yaml.safe_load(file1)
	
	trackNumber = ['Title-', episode[2]]
	trackNumber = ''.join(trackNumber)
	
	episodeData = {
		'Name': episodeInformation[trackNumber]['Name'],
		'Aired': episodeInformation[trackNumber]['Aired'],
		'Season': episodeInformation[trackNumber]['Season'],
		'Episode': episodeInformation[trackNumber]['Episode'],
		'Chapters': episodeInformation[trackNumber]['Chapters'],
		'Keep Chapters': episodeInformation[trackNumber]['Keep Chapters'],
		'Audio': episodeInformation[trackNumber]['Audio'],
		'Video': episodeInformation[trackNumber]['Video'],
		'Subtitles': episodeInformation[trackNumber]['Subtitles'],
		'Rip': episodeInformation[trackNumber]['Rip']
	}

	if episodeData['Rip'] == False:
		return False

	sortedListEpisodeData = [makeDiskName(episode), episode[2], episodeData['Chapters'], makeFileName(episode, episodeData), fileFormat]
	
	return joinArgs(episodeData, sortedListEpisodeData)


def makeEpisodeFile(episode):
	fileTemplate = ['cases', ['/case', ''], ['/disk', ''], '.yml']
	
	for i in range(2):
		fileTemplate[i + 1][1] = episode[i]
		fileTemplate[i + 1] = ''.join(fileTemplate[i + 1])
	
	return ''.join(fileTemplate)


def getEpisodeCommand(episode): # [case, disk, title]
	for i in range(3):
		episode[i] = str(episode[i])

	return getEpisodeInformation(episode)
