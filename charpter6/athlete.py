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
    
class Athlete:
    def __init__(self, a_name, a_dob = None, a_times=[]):
        self.name  = a_name
        self.dob   = a_dob
        self.times = a_times
    def top3(self):
        return (sorted(set([sanitize(item) for item in self.times]))[0:3])
    def add_time(self, time_value):
        self.times.append(time_value)
    def add_times(self, list_time):
        self.times.extend(list_time)
    def add_dob(self, a_dob):
        self.dob = a_dob
    
def getCoachData(fileName):
    try:
        os.chdir('F:\\GitHub\\python\\bookShare')
        with open(fileName) as openedFile :
            data = openedFile.readline()
            listedData = data.strip().split(',')
            athlete = Athlete(listedData.pop(0), listedData.pop(0), listedData) 
        return athlete
    except IOError as ioErr:
        print('File Error: ' + str(ioError))
        return None
  
james = getCoachData('james2.txt')
julie = getCoachData('julie2.txt')
mikey = getCoachData('mikey2.txt')
sarah = getCoachData('sarah2.txt')
print(james.name + "'s fastest three times are: " + str(james.top3()))
print(julie.name + "'s fastest three times are: " + str(julie.top3()))
print(mikey.name + "'s fastest three times are: " + str(mikey.top3()))
print(sarah.name + "'s fastest three times are: " + str(sarah.top3()))

vera = Athlete('Vera Vi')
vera.add_time('1.31')
vera.add_dob('2001-3-12')
vera.add_times(['2-22', '1-21', '2:22'])
print(vera.name + "'s fastest three times are: " + str(vera.top3()))

