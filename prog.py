from someapi import FileOps, ProcessOps
from statapi import StatApi


path = 'C:\ZBRUSH_TEMP'
StatApi.checkSize(path)
countDup = FileOps.countFiles(path)
countNoDup = FileOps.countFiles(path,False)
print(f'{path} has {countDup} files, {countNoDup} if you remove the duplicate names')

print('')
ProcessOps.printProgList()
progRun = False
while progRun == False:
    progRun = ProcessOps.startProgByNum(int(input('Please select a program: ')))

