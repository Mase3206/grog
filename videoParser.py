import yaml, settings

rawSettings, prettySettings = settings.getSettings(False)
videoOutputArgs = ['-e', '', '--encoder-preset', 'veryslow', '--encoder-tune', 'animation', '--encoder-profile', 'main', '--encoder-level', 'auto', '-q', '18', '-r', '23.976', '--cfr', ]
pictureOutputArgs = ['-w', '', '-h', '', '--crop-mode', 'none', '--auto-anamorphic']
filterOutputArgs = ['--no-comb-detect', '--no-deinterlace', '--no-decomb', '--no-detelecine', '-8', 'y-spatial=0:cb-spatial=0:cr-spatial=0:y-temporal=8:cb-temporal=8:cr-temporal=8', '--no-chroma-smooth', '--no-unsharp', '--no-lapsharp', '--no-deblock', '--no-grayscale']
fetchedSettings = []


def getVideoCommand():
	fetchedSettings = []

	fetchedSettings.append(rawSettings['Encoder'])

	for i in range(len(fetchedSettings)):
		outputArgs[i*2+1] = fetchedSettings[i]
	
	return outputArgs
