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
    name  = ''
    dob   = ''
    times = [] 
    def _init(self, a_name, a_dob = None, a_times=[]):
        self.name  = a_name
        self.dob   = a_dob
        self.times = a_times
    def top3(self):
        return (sorted(set([sanitize(item) for item in self.times]))[0:3])
        
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
print(james.name + "'s fastest three times are: " + str(james.top3()))
