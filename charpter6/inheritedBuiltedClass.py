class NamedList(list):
	def __init__(self, a_name):
		list.__init__([]) #调用基类的初始化函数
		self.name = a_name

		
johney = NamedList('John Paul Jones')
print(type(johney)) #<class '__main__.NamedList'>
print(dir(johney))  #dir() show the names in the module namespace
'''
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__module__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'name', 'pop', 'remove', 'reverse', 'sort']
''' 

johney.append('Bass Player')
johney.extend(['Composer', 'Arranger', 'Musician'])
print(johney)      #['Bass Player', 'Composer', 'Arranger', 'Musician']
print(johney.name) #John Paul Jones

for attr in johney:#NamedList类似于列表，能够使用列表的地方，它也能被使用
    print(johney.name + " is a " + attr + ".")