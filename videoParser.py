import yaml, settings, filterParser

rawSettings, prettySettings = settings.getSettings(False)
fetchedSettings = []

with open('profiles/defaultVideo.yml', 'r') as file1:
	defaultVideo = yaml.safe_load(file1)


# Expected
# videoOutputArgs = ['-e', '', '--encoder-preset', 'veryslow', '--encoder-tune', 'animation', '--encoder-profile', 'main', '--encoder-level', 'auto', '-q', '18', '-r', '23.976', '--cfr', ]
# pictureOutputArgs = ['-w', '', '-h', '', '--crop-mode', 'none', '--auto-anamorphic']
# filterOutputArgs = ['--no-comb-detect', '--no-deinterlace', '--no-decomb', '--no-detelecine', '-8', 'y-spatial=0:cb-spatial=0:cr-spatial=0:y-temporal=8:cb-temporal=8:cr-temporal=8', '--no-chroma-smooth', '--no-unsharp', '--no-lapsharp', '--no-deblock', '--no-grayscale']

videoOutputArgs = ['-e', '', '--encoder-preset', '', '--encoder-tune', '', '--encoder-profile', '', '--encoder-level', '', '-q', '', '-r', '', '', ]
pictureOutputArgs = ['-w', '', '-h', '', '--crop-mode', '', '']
filterOutputArgs = ['', '', '', '', '', '', '', '', '', '', '']


def getVideoCommand():
	videoOutputArgs = ['-e', '', '--encoder-preset', '', '--encoder-tune', '', '--encoder-profile', '', '--encoder-level', '', '-q', '', '-r', '', '', ]
	pictureOutputArgs = ['--crop-mode', '', '']
	filterOutputArgs = ['', '', '', '', '', '', '', '', '', '', '']

	fetchedSettingsVideo = []
	fetchedSettingsPicture = []
	fetchedSettingsFilter = []
	outputArgs = []


	# Video Output Args
	fetchedSettingsVideo.append(defaultVideo['Video Settings']['Encoder'])
	fetchedSettingsVideo.append(defaultVideo['Video Settings']['Encoder Preset'])
	fetchedSettingsVideo.append(defaultVideo['Video Settings']['Encoder Tune'])
	fetchedSettingsVideo.append(defaultVideo['Video Settings']['Encoder Profile'])
	fetchedSettingsVideo.append(defaultVideo['Video Settings']['Encoder Level'])

	fetchedSettingsVideo.append(str(defaultVideo['Video Settings']['Constant Quality']))
	fetchedSettingsVideo.append(str(defaultVideo['Video Settings']['Framerate']))

	if bool(defaultVideo['Video Settings']['Constant Framerate']) == True:
		fetchedSettingsVideo.append('--cfr')
	else:
		fetchedSettingsVideo.append('')


	# Picture Output Args
	if defaultVideo['Picture Settings']['Width'] != 'auto':
		fetchedSettingsPicture.append(defaultVideo['Picture Settings']['Width'])
		pictureOutputArgs.append('-w')

	
	if defaultVideo['Picture Settings']['Height'] != 'auto':
		fetchedSettingsPicture.append(defaultVideo['Picture Settings']['Height'])
		pictureOutputArgs.append('-h')


	fetchedSettingsPicture.append(defaultVideo['Picture Settings']['Crop Mode'])

	if defaultVideo['Picture Settings']['Anamorphic'] == 'auto':
		fetchedSettingsPicture.append('--auto-anamorphic')



	# Filter Output Args

	# comb detect
	if bool(defaultVideo['Filter Settings']['Comb Detect']) == False:
		fetchedSettingsFilter.append('--no-comb-detect')

	# decomb
	if bool(defaultVideo['Filter Settings']['Decomb']) == False:
		fetchedSettingsFilter.append('--no-decomb')

	# deinterlace
	if bool(defaultVideo['Filter Settings']['Deinterlace']) == False:
		fetchedSettingsFilter.append('--no-deinterlace')

	# detelecine
	if bool(defaultVideo['Filter Settings']['Detelecine']) == False:
		fetchedSettingsFilter.append('--no-detelecine')

	# detelecine
	if bool(defaultVideo['Filter Settings']['Chroma Smoothing']) == False:
		fetchedSettingsFilter.append('--no-chroma-smooth')

	# detelecine
	if bool(defaultVideo['Filter Settings']['Sharpen']) == False:
		fetchedSettingsFilter.append('--no-unsharp')
		fetchedSettingsFilter.append('--no-lapsharp')

	# detelecine
	if bool(defaultVideo['Filter Settings']['Deblock']) == False:
		fetchedSettingsFilter.append('--no-deblock')

	# detelecine
	if bool(defaultVideo['Filter Settings']['Grayscale']) == False:
		fetchedSettingsFilter.append('--no-grayscale')

	# denoise
	if defaultVideo['Filter Settings']['Denoise'] == 'hqdn3d':
		fetchedSettingsFilter.append('-8')
		fetchedSettingsFilter.append(filterParser.hqdn3d(defaultVideo['Filter Settings']['Denoise Settings']['HQDN3D']))

	
	fetchedSettings.append(''.join(fetchedSettingsVideo))
	fetchedSettings.append(''.join(fetchedSettingsPicture))
	fetchedSettings.append(''.join(fetchedSettingsFilter))


	



	for i in range(len(fetchedSettings)):
		outputArgs[i*2+1] = fetchedSettings[i]
	
	return outputArgs

if __name__ == '__main__':
	print(getVideoCommand())