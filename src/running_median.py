import os
import string

WordCountList = list()

FileList = os.listdir('wc_input')
FileList.sort()

fout = open('wc_output/med_result.txt', 'w')

length = 0
for i in FileList:
	fin = open('wc_input/' + i, 'r')
	Lines = fin.readlines()
	fin.close()
	for j in Lines:
		Words = j.translate(None, string.punctuation).split(' ')
		for k in range(len(Words), 0, -1):
			if Words[k - 1] == '':
				del Words[k - 1]
		if len(Words) == 1 and Words[0] == '\n':
			WordCountList.insert(0, 0)
		else:
			WordCountList.append(len(Words))
			WordCountList.sort()
		length = length + 1

		if length % 2 == 0:
			fout.write(str((WordCountList[length / 2 - 1] + WordCountList[length / 2]) / 2.0) + '\n')
		else:
			fout.write(str(float(WordCountList[length / 2])) + '\n')

fout.close()
