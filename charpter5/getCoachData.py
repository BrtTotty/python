import os
def sanitize(time_string):
    if '-' in time_string:
        spliter = '-'
    elif ':' in time_string:
        spliter = ':'
    else:
        return (time_string)
    (mins,secs) = time_string.split(spliter)
    return (mins + '.' + secs)

def get_coach_data(fileName):
    try:
        os.chdir('F:\\GitHub\\python\\charpter5')
        with open(fileName) as openedFile :
            data = openedFile.readline()
            listData = data.strip().split(',')
        return (sorted(set([sanitize(eachItem) for eachItem in listData]))[0:3])
    except IOError as ioErr:
        print('File Error: ' + str(ioError))
        return None

james = get_coach_data('james.txt')
julie = get_coach_data('julie.txt')
mikey = get_coach_data('mikey.txt')
sarah = get_coach_data('sarah.txt')
print("james fastest three times: ", james)
print("james fastest three times: ", mikey)
print("james fastest three times: ", julie)
print("james fastest three times: ", sarah)
        
