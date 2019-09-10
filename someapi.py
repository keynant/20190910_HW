import os
import psutil


class FileOps:
    def countFiles(path, findDuplicates=True):
        count = []
        for dirpath, dirnames, filenames in os.walk(path):
            for file1 in filenames:
                count.append(str(file1).lower())
        if findDuplicates:
            return len(count)
        if not findDuplicates:
            return len(set(count))


class ProcessOps:
    progDict = {'Notepad': (1,"c:\\windows\\system32\\notepad.exe"), 'Paint': (2,'mspaint.exe'),
                "Calculator": (3,'calc.exe'), "Firefox": (4,r'C:\Program Files (x86)\Mozilla Firefox\firefox.exe')}
    def startProg():
        """
        Starts a program by name (like a command prompt).
        works only on PATH enabled processes (like notepad for notepad.exe)
        :return: Returns False if program was not launched, otherwise None
        """
        name = input('please enter a program name(only works on \'path\' enabled programs): ')
        for proc in psutil.process_iter():
            if name.lower() == os.path.splitext(proc.name())[0].lower():
                return False
        os.startfile(str(name) + '.exe')

    def __startProgFromNum(path):
        """
        Receives a number from startProgByNum().
        Checks if the selected program runs in the process list, and if not - runs it.
        :return: returns True if the program was exectured, False if it exists already in the process list.
        """
        ls1 = set()
        for proc in psutil.process_iter():
            ls1.add(proc.name())
        if not path.split('\\')[-1] in ls1:
            print("Running selected program...")
            os.startfile(path)
            return True
        else:
            print("Program already running...")
            return False  # <-- + ^   use these to tell the call if the program started or not.

    def startProgByNum(num):
        """
        Receives a number, and sends the correct path to __startProgFromNum().
        :return: return is a pass-through of the value from __startProgFromNum()
        """
        result = False
        if num == 0:
            return True
        elif num == 1:
            result = ProcessOps.__startProgFromNum(ProcessOps.progDict['Notepad'][1])
            return result
        elif num == 2:
            result = ProcessOps.__startProgFromNum(ProcessOps.progDict['Paint'][1])
            return result
        elif num == 3:
            result = ProcessOps.__startProgFromNum(ProcessOps.progDict['Calculator'][1])
            return result
        elif num == 4:
            result = ProcessOps.__startProgFromNum(ProcessOps.progDict['Firefox'][1])
            return result
        elif num == 9:
            ProcessOps.printProgList()
            return False
        else:
            print('Invalid choice, please select a number from the list.')
            return False

    def printProgList():
        print("Program List:")
        print("0. Exit")
        for k,v in ProcessOps.progDict.items():
            print(f'{v[0]}. {k}')
        print ("9. Print list again")


def main():
    a = FileOps.countFiles('C:\ZBRUSH_TEMP')
    # print(a)
    a = FileOps.countFiles('C:\ZBRUSH_TEMP', False)
    # print(a)
    ProcessOps.printProgList()
    progRun = False
    while progRun == False:
        progRun = ProcessOps.startProgByNum(int(input('Please select a program: ')))


if __name__ == "__main__":
    main()
