class my_Gen():
   current=0
def __init__(Self,first,last):
Self.first= first
Self.last= last

def __iter__(Self):
  return Self

def __next__(Self():
if my_Gen.current<Self.last:
num= my_Gen.current
my_gen.current+= 1
   return num
raise StopIteration

gen= my_Gen(0,100)
for i in gen:
print(i)