import yaml, reformat, settings

rawSettings, prettySettings = settings.getSettings(False)



if __name__ == '__main__':
	print('\nThis program is not meant to be run directly. Please instead call the functions within this program from another.\nExiting...\n')
	exit(0)


with open('profiles/audio.yml', 'r') as file1:
	defaultAudio = yaml.safe_load(file1)



def getAudioTrackParams(trackNumber: int):
	trackList = ['Track', str(trackNumber)]
	track = ' '.join(trackList)
	out = []
	out.append(defaultAudio[track]['Track'])
	out.append(defaultAudio[track]['Codec'])
	out.append(defaultAudio[track]['Bitrate'])
	out.append(defaultAudio[track]['Mixdown'])
	out.append(defaultAudio[track]['Name'])

	return out


def getAudioTrackCommand(totalTracks: int):
	outputArgs = ['-a','','-E','','-B','','-6','','-A','']
	rawArgs = []
	
	# add track params sublist to rawArgs list
	for i in range(totalTracks):
		rawArgs.append(getAudioTrackParams(i+1))

	# combine each sublist of related arguments into one string separated by a comma
	zippedArgs = reformat.group(rawArgs)
	
	# put groupedArgs items into the correct place in outputArgs
	for i in range(len(zippedArgs)):
		outputArgs[i*2+1] = zippedArgs[i]

	return outputArgs

#print(getAudioTrackCommand(3))