

def hqdn3d(settings):
	hqdn3dSettings = ['y-spatial=', '', ':cb-spatial=', '', ':cr-spatial=', '', ':y-temporal=', '', ':cb-temporal=', '', ':cr-temporal=', '']

	spacial = settings['Spacial']
	temporal = settings['Temporal']

	for i in range(3):
		hqdn3dSettings[i*2+1] = str(spacial[i])
		hqdn3dSettings[i*2+7] = str(temporal[i])

	return ''.join(hqdn3dSettings)


if __name__ == '__main__':
	a = {
		'Spacial': [
			0,
			0,
			0
		],
		'Temporal': [
			8,
			8,
			8
		]
	}

	print(hqdn3d(a))