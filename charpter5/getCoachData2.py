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
        with open(fileName) as openedFile :
            data = openedFile.readline()
            listedData = data.strip().split(',') 
            return ({'NAME' : listedData.pop(0),
                     'DOB'  : listedData.pop(0),
                     'TIMES': sorted(set([sanitize (Item) for Item in listedData]))[0:3]})
    except IOError as ioErr:
        print('File Error: ' + str(ioError))
        return None
        
os.chdir('F:\\GitHub\\python\\bookShare')
james = get_coach_data('james2.txt')
julie = get_coach_data('julie2.txt')
mikey = get_coach_data('mikey2.txt')
sarah = get_coach_data('sarah2.txt')

print(james['NAME'] + "'s fastest three times are: ", james['TIMES'])
print(julie['NAME'] + "'s fastest three times are: ", julie['TIMES'])
print(mikey['NAME'] + "'s fastest three times are: ", mikey['TIMES'])
print(sarah['NAME'] + "'s fastest three times are: ", sarah['TIMES'])