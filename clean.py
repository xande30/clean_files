import os, sys
from colorama import Fore

find_only = False
root_dir = os.getcwd() if len(sys.argv) == 1 else sys.argv[1]

found = removed = 0
for (thisDirLevel, subsHere, filesHere) in os.walk(root_dir):
    for filename in filesHere:
        if filename.endswith('.pyc'):
            fullname = os.path.join(thisDirLevel, filename)
            print('==>', fullname)
            if not find_only:
                try:
                    os.remove(fullname)
                    removed += 1
                except:
                    tipe, inst = sys.exc_info()[:2]
                    print('*' * 4, 'Failed:', filename, tipe, inst)
            found += 1
print(Fore.LIGHTGREEN_EX, 'Found', found, 'files, removed', removed)
