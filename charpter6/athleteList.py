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
    
class AthleteList(list):
    def __init__(self, a_name, a_dob = None, a_times=[]):
        list.__init__([]) #变化1
        self.name  = a_name
        self.dob   = a_dob
        self.extend(a_times) #变化2
    def top3(self):
        #变化3 self 不是 self.times
        return (sorted(set([sanitize(item) for item in self]))[0:3]) 
    def add_time(self, time_value):
        self.append(time_value)
    def add_times(self, list_time):
        self.extend(list_time)
    def add_dob(self, a_dob):
        self.dob = a_dob
    
def getCoachData(fileName):
    try:
        os.chdir('F:\\GitHub\\python\\bookShare')
        with open(fileName) as openedFile :
            data = openedFile.readline()
            listedData = data.strip().split(',')
            return (AthleteList(listedData.pop(0), listedData.pop(0), listedData)) 
    except IOError as ioErr:
        print('File Error: ' + str(ioError))
        return None

sarah = getCoachData('sarah2.txt')
print(sarah.name + "'s fastest three times are: " + str(sarah.top3()))        
vera = AthleteList('Vera Vi')
vera.add_time('1.31')
vera.add_dob('2001-3-12')
vera.add_times(['2-22', '1-21', '2:22'])
print(vera.name + "'s fastest three times are: " + str(vera.top3()))

