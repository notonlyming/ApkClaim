import os

# 获取所有包名
os.system('adb shell pm list packages > app.txt')

# 打开并分割得包名
with open('app.txt', 'r', encoding='utf-8') as f:
    appStr = f.read()
appPackeageNames = list(map(lambda line: line.split(':')[1], appStr.split('\n')[:-1]))

# 清空输出的地址文件
with open('namePrintInfo.txt', 'w', encoding='utf-8') as f:
    f.write('')

# 获取所有包所在路径并追加到文件
nameNumber = len(appPackeageNames)
backspaceNumber = 25
for i in range(nameNumber):
    print("{}get path of :{}/{}".format('\r' * backspaceNumber, i+1, nameNumber), end='')
    os.system('adb shell pm path ' + appPackeageNames[i] + '>> namePrintInfo.txt')

# 提取出用户包所在的路径
with open('namePrintInfo.txt', 'r', encoding='utf-8') as f:
    allOutputLines = f.read().split('\n')

# 过滤得到所有用户目录app，即假设package:/data/app/下的是用户app。过滤完毕后去掉开头的package:
allUsrAppPaths = list(map(lambda line: line.split(':')[1], filter(lambda line: line.startswith('package:/data/app/'), allOutputLines)))
# 将包名提出来，组成字典，方便重命名默认为base.apk的apk文件
allUsrAppPathsDict = dict(zip(map(lambda path: path.split('/')[3].split('-')[0], allUsrAppPaths), allUsrAppPaths))

for packageName in allUsrAppPathsDict:
    if not os.path.exists('apk'):
        os.mkdir('apk')
    thisPath = allUsrAppPathsDict[packageName]
    os.system('adb pull {} apk/{}'.format(thisPath, packageName+'.apk' if thisPath.endswith('base.apk') else ''))