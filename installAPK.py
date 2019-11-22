import os

allAPKFileNames = os.listdir('apk')
allAPKFileNames = list(filter(lambda fileName: fileName.endswith('.apk'), allAPKFileNames))

print('----------------------')
for name in allAPKFileNames:
    print(name)
print('----------------------')

if input('install?(y/n): ') == 'y':
    APKNumber = len(allAPKFileNames)
    for index in range(APKNumber):
        print("{}/{}".format(index+1, APKNumber))
        os.system('adb install {}'.format('apk/' + allAPKFileNames[index]))