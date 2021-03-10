def my_function():
def my_function():
   print("Hello world")
  #arguments
def sum(x,y):
  a=x+y
  print ("The sum is",a)
sum(10,20)
sum(501,958)
#sum
def sum(x,y):
  a=x+y
  return a
print(sum(10,20))
#multiple def *args
def courses(*args):
 for subject in args:
   print(subject)
courses("Big Data", "CCNA","OOP2")
#key word arguments#
def courses(**kwargs):
   for key, value in kwargs.items():
     print("{}:{}".format(key,value))
courses(first='Big data', second='CCNA',third='HCIA')
#Default parameter value
def Kenya(County = "Mombasa"):
  print ("I am from" + County)
Kenya()
Kenya("Nairobi")
Kenya("Kiambu")
Kenya("Kisumu")
#passing a list as an argument
def my_function(food):
  for x in food:
    print(x)
fruits = ["apple","banana","cherry"]
my_function(fruits)