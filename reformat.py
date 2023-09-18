def combineArgs(lst,argument):
	temp = []
	for i in range(len(lst)):
		temp.append(lst[i][argument])
	return temp


def lst2str(superlist):
	rawArgs = superlist
	groupedArgs = []
	zippedArgs = []
	
	rnge = len(superlist[0])

	# grab all related arguments `i` from each sublist of rawArgs, add to a new sublist in groupedArgs
	for i in range(len(rawArgs[0])):
		groupedArgs.append(combineArgs(rawArgs,i))
	
	# convert all list items to strings
	for i in range(len(groupedArgs)):
		for j in range(len(groupedArgs[0])):
			groupedArgs[i][j] = str(groupedArgs[i][j])

	# combine each sublist of related arguments into one string separated by a comma
	for i in range(len(groupedArgs)):
		zippedArgs.append(','.join(groupedArgs[i]))

	return zippedArgs


def dic2lstlst(dic):
	keys = list(dic.keys())
	values = list(dic.values())
	
	return list(map(list, zip(keys, values)))


def prettyList(lstlst):
	out = []
	for i in range(len(lstlst)):
		temp = []
		temp.append(str(lstlst[i][0]))
		temp.append("  =  ")
		temp.append(str(lstlst[i][1]))

		out.append(''.join(temp))

	return '\n'.join(out)


def prettyDic(dic, new):
	if new == True:
		return ''.join(['\nNew settings: \n', prettyList(dic2lstlst(dic))])
	else:
		return ''.join(['\nCurrent settings: \n', prettyList(dic2lstlst(dic))])
