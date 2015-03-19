import os
import string

WordList = list()

FileList = os.listdir('wc_input')

for i in FileList:
	fin = open('wc_input/' + i, 'r')
	Str = fin.read().lower().translate(None, string.punctuation).replace('\n', ' ')
	fin.close()
	WordList.extend(Str.split(' '))

WordList.sort()
while WordList[0] == '':
	WordList.remove('')

fout = open('wc_output/wc_result.txt', 'w')

count = 1
for i in range(1, len(WordList)):
	if WordList[i] == WordList[i - 1]:
		count = count + 1
	else:
		fout.write(WordList[i - 1] + '\t' + str(count) + '\n')
		count = 1
fout.write(WordList[i] + '\t' + str(count) + '\n')

fout.close()
