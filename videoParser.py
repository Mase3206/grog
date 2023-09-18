import yaml, settings

rawSettings, prettySettings = settings.getSettings(False)
outputArgs = ['-e', '']
fetchedSettings = []


def getVideoCommand():
	fetchedSettings = []

	fetchedSettings.append(rawSettings['Encoder'])

	for i in range(len(fetchedSettings)):
		outputArgs[i*2+1] = fetchedSettings[i]
	
	return outputArgs
