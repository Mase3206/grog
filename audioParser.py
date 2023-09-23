import yaml, reformat, settings

global environment
rawSettings, prettySettings = settings.getSettings(False)
environment = rawSettings['Environment']


"""if environment == 'Unix':
		# code
	elif environment == 'Windows':
		# code
	else:
		raise ValueError('Environment variable set to illegal value in `settings.yml`. Only "Windows" and "Unix" are accepted values.')"""


if __name__ == '__main__':
	print('\nThis program is not meant to be run directly. Please instead call the functions within this program from another.\nExiting...\n')
	exit(0)


with open('profiles/audio.yml', 'r') as file1:
	defaultAudio = yaml.safe_load(file1)



def getAudioTrackParams(trackNumber):
	trackList = ['Track', str(trackNumber)]
	track = ' '.join(trackList)
	out = []
	out.append(defaultAudio[track]['Track'])
	out.append(defaultAudio[track]['Codec'])
	out.append(defaultAudio[track]['Bitrate'])
	out.append(defaultAudio[track]['Mixdown'])
	out.append(defaultAudio[track]['Name'])

	return out

def combineArgs(lst,argument):
	temp = []
	for i in range(len(lst)):
		temp.append(lst[i][argument])
	return temp


def getAudioTrackCommand(totalTracks):
	outputArgs = ['-a','','-E','','-B','','-6','','-A','']
	rawArgs = []
	
	# add track params sublist to rawArgs list
	for i in range(totalTracks):
		rawArgs.append(getAudioTrackParams(i+1))

	"""# grab all related arguments `i` from each sublist of rawArgs, add to a new sublist in groupedArgs
	for i in range(len(rawArgs[0])):
		groupedArgs.append(combineArgs(rawArgs,i))
	
	# convert all list items to strings
	for i in range(len(groupedArgs)):
		for j in range(len(groupedArgs[0])):
			groupedArgs[i][j] = str(groupedArgs[i][j])"""

	# combine each sublist of related arguments into one string separated by a comma
	zippedArgs = reformat.lst2str(rawArgs)
	
	# put groupedArgs items into the correct place in outputArgs
	for i in range(len(zippedArgs)):
		outputArgs[i*2+1] = zippedArgs[i]

	return outputArgs

#print(getAudioTrackCommand(3))