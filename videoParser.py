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
filterOutputArgs = ['', '', '', '', '', '', '--no-unsharp', '--no-lapsharp', '--no-deblock', '--no-grayscale']


def getVideoCommand():
	fetchedSettingsVideo = []
	fetchedSettingsPicture = []
	fetchedSettingsFilter = []
	fetchedSettingsHQDN3D = []
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
	if defaultVideo['Picture Settings']['Width'] != '':
		fetchedSettingsPicture.append(defaultVideo['Picture Settings']['Width'])
	else:
		fetchedSettingsPicture.append('')
	
	if defaultVideo['Picture Settings']['Height'] != '':
		fetchedSettingsPicture.append(defaultVideo['Picture Settings']['Height'])
	else:
		fetchedSettingsPicture.append('')

	fetchedSettingsPicture.append(defaultVideo['Picture Settings']['Crop Mode'])

	if defaultVideo['Picture Settings']['Anamorphic'] == 'auto':
		fetchedSettingsPicture.append('--auto-anamorphic')


	# Filter Output Args

	if defaultVideo['Filter Settings']['Denoise'] == 'hqdn3d':
		fetchedSettingsFilter.append('-8')
		# put the actual values here



	for i in range(len(fetchedSettings)):
		outputArgs[i*2+1] = fetchedSettings[i]
	
	return outputArgs
