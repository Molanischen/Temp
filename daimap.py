print "I will now count","Hello"
print "hens",5+6-7
print "It is greater?", 5>=2.0
print "try" , 5.0+2.4
a=1 
b=2
c=3
print c*(a/float(b))
#

#

cars=100
space_in_a_car=4.0
drivers=30
passengers=90
cars_not_driven=cars-drivers
cars_driven=drivers
carpool_capacity=cars_driven*space_in_a_car
average_passengers_per_car=passengers/cars_driven

print "There are" ,cars,"cars available."
print "There are only",drivers, "drivers available."
print "There will be", cars_not_driven,"empty cars today."
print "We can transport",carpool_capacity,"people today."
print "We have",passengers,"to carpool today."
print "We need to put about",average_passengers_per_car,"in each car."

#formant string %r %d %s 
my_name = 'Zed A. Shaw'
my_age = 35#not a lie
my_height = 74 #inches
my_weight = 180 #lbs
my_eyes = 'blue'
my_teeth = 'white'
my_hair = 'brown'

print "Let's talk about %s." % my_name
print "He's %d inches tall." % my_height
print "He's %d pounds heavy." % my_weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." %(my_eyes, my_hair)

#string and text
x="There are %d types of people." %10
binary="binary"
do_not= "don't"
y="Those who know %s and those who %s." %(binary , do_not)
print x
print y 
print "I said: %r." %x
print "I also said:'%s'." %y
w = 'this is...'
v = "a string."
print w+v

#more print
print "Mary had a little lamb."
print "Its fleece was white as %s." %'snow'
print "And everywhere that mary went."
print "."*10 
end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"
#watch that comma at the end, try removing it to see what happens
print end1 + end2 + end3 + end4 + end5 + end6,
print end7 + end8 + end9 + end10 + end11 + end12

#more print
formatter = "%r %r %r %r"

print formatter %(1,2,3,4)
print formatter %("one", "two","three","four") 
print formatter %(True, False, False, True)
print formatter %(formatter, formatter, formatter, formatter)
print formatter %(
"I had this thing.",
"That you could type up right.",
"But it didn't sing.",
"So I said goodnight."
)

#print print print
days = "Mon Tue Wed Thu Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

print "Here are the days:",days
print days
print "Here are the months:",months

print """
Actually.
Warning.
C.
EOFErro.
"""

#double back slash
print "I am 6'2\" tall"
print 'I am 6\'2" tall.'

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\a\\cat"

fat_cat = '''
I'll do a list:
\t* Cat food
\t* Fishes
\t* Catnip\n\t*Grass
'''

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

#question
pounds=100
kilograms=pounds*0.4536
print "change %d pounds into %f kilogram" %(pounds, kilograms)

#question raw_input
print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh",
weight = raw_input()

print "So, you're %r old, %r tall and %r heavy." %(age, height, weight)


#parameters variables modules
from sys import argv

script, first, second, third=argv

print "the script is called:",script
print "Your first variable is:",first
print "Your second variable is:",second
print "Your third variable is:",third

#argv raw_input
from sys import argv
script, user_name = argv
prompt = '>'
print "Hi %s, I'm the %s script." %(user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" %user_name
likes = raw_input(prompt)

print "Where do you live %s?" %user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print"""
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
"""%(likes, lives, computer )

#read files
from sys import argv
script,filename=argv
txt=open(filename)
print "Here's your file %r:" %filename
print txt.read()
print "Type the filename again:"
file_again=raw_input(">")
txt_again=open(file_again)
print txt_again.read()

#exe16 read and write file
from sys import argv
script,filename=argv
print "We are going to erase %r"%filename
print "If you dont want that,hit CTRL-C(^C)."
print "If you do want that, hit return."
raw_input("?")
print "Opening the file..."
target=open(filename,'w')

print "Truncating the file, Goodbye!"
target.truncate()
print "Now Iam going to ask you for three line."

line1=raw_input("line 1:")
line2=raw_input("line 2:")
line3=raw_input("line 3:")
print"Iam going to write these to this file."
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")


#target.write(line1+line2+line3) write in one line

print "And finally, We close it."
target.close()

txt=open(filename)
print txt.read()



#exe17 more exercise of file
from sys import argv
from os.path import exists

script,from_file,to_file=argv
print"Copying from %s to %s " %(from_file, to_file)

#we could do these two on one line , How?
input=open(from_file)
indata=input.read()

print"The input file is %d bytes long"%len(indata)

print"Does the output file exist? %r" %exists(to_file)
print"Ready, hit RETURN to continue, CTRL-C to abort."
raw_input
output=open(to_file,'w')
output.write(indata)

print"Alright, all done."
output.close()
input.close()

#exe18 function
#this one is like your scripts with argv
def print_two(*args):
 arg1,arg2=args
 print"arg1:%r,arg2:%r"%(arg1,arg2)

#ok,that *args is actually pointless, we can just do this
def print_two_again(arg1,arg2):
 print"arg1:%r,arg2:%r"%(arg1,arg2)

#this just takes one argument
def print_one(arg1):
 print "arg1:%r"%arg1

#this one takes no arguments
def print_none():
 print"I got nothin"

print_two("Zed","Shaw")
print_two_again("Zed","Shaw")
print_one("First!")
print_none()

#exe19 function and variables
def cheese_and_cracker(cheese_count,boxes_of_crackers):
 print"You have %d cheese!"%cheese_count
 print"You have %d boxes of crackers!"%boxes_of_crackers
 print"Man that's enough for a party!"
 print"Get a blanket.\n"

print"We can just give the function numbers directly:"
cheese_and_cracker(20,30)

print"OR, we can use variables from our script:"
amount_of_cheese=10
amount_of_crackers=50
cheese_and_cracker(amount_of_cheese,amount_of_crackers)

print"We can even do math inside too"
cheese_and_cracker(10+20,5+6)

print"And we can combine the two, variables and math"
cheese_and_cracker(amount_of_cheese+100,amount_of_crackers+1000)




#exe20 function and file
from sys import argv
script,input_file=argv

def print_all(f):
 print f.read()
 
def rewind(f):
 f.seek(0)
 
def print_a_line(line_count,f):
 print line_count,f.readline()
 
current_file=open(input_file)

print"First lets print the whole file:\n"
print_all(current_file)

print"Now lets rewind, kind of like a tape"
rewind(current_file)

print"Lets print three lines:"
current_line=1
print_a_line(current_line,current_file)

current_line=current_line+1
print_a_line(current_line,current_file)

current_line=current_line+1
print_a_line(current_line,current_file)



#function with return
def add(a,b):
 print "Adding %d+%d"%(a,b)
 return a+b

def substract(a,b):
 print"Sbustracting %d-%d"%(a,b)
 return a-b

def multiply(a,b):
 print"Multiplying %d*%d"%(a,b)
 return a*b 

def divide(a,b):
 print"Dividing %d / %f"%(a,b)
 return a/b

print"Lets do some math with just functions!"

age= add(30,5)

height = substract(78,4)

weight = multiply(90,2)

iq = divide(100,0.8)

print("Age:%d,Height:%d,Weight:%d,IQ:%f")%(age,height,weight,iq)

print"Here is a puzzle"
what=add(age,substract(height,multiply(weight,divide(iq,2))))
print"That becomes",what,"can you do it by hand?"


#exe24 more exercise
print"Lets practice everything"
print'You\'d need to know \'bout escapes with \\that do\n newlines and \t tabs.'
poem="""
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""
print "---------"
print poem
print "---------"

five= 10-2+3-6
print "This should be five:%s" %five 

def secret_formula(started):
 jelly_beans=started*500
 jars=jelly_beans/1000
 crates=jars/100
 return jelly_beans,jars,crates

start_point=10000
beans,jars,crates=secret_formula(start_point)
print"With a starting point of:%d"%start_point
print"We'd have %d beans,%d jars,%d crates."%(beans,jars,crates)
start_point=start_point/10
print"We can also do that this way."
print"We'd have %d beans ,%d jars , %d crates."%secret_formula(start_point)

#exe25
def break_words(stuff):
 """This function will break up words for us."""
 words=stuff.split(' ')
 return words
 
def sort_words(words):
 """Sorts the words."""
 return sorted(words)
 
def print_first_word(words):
 """Prints the first word after popping it off."""
 word=words.pop(0)
 print word
 
def print_last_word(words):
 """Prints the last word after popping it off"""
 word=words.pop(-1)
 print word
 
def sort_sentence(sentence):
 """Takes in a full sentence and returns the sorted words"""
 words=break_words(sentence)
 return sort_words(words)
 
def print_first_and_last_sorted(sentence):
 """Sorts the words then prints the firsr and last one."""
 words=sort_sentence(sentence)
 print_first_word(words)
 print_last_word(words)
 

 
 #exe 29 if
people = 20 
cats = 30
dogs = 15
if people < cats:
 print "Too many cats! The world is doomed!"
 
if people>cats:
 print "Not many cats! The world is saves!"
 
if people < dogs:
 print "The world is drooled on!"

if people > dogs:
 print "The world is dry!"
 
dogs +=5

if people >=dogs:
 print"People are greater than or equal to dogs."

if people==dogs:
 print"People are dogs"

 
#exe 30 if and else
people = 30 
cars = 40
buses = 15
if cars>people :
 print "We should take the cars!"
elif cars<people:
 print" We should not take the cars!"
else:
 print "We cannot decide."

if buses>cars:
 print"Thats too many buses."
elif buses<cars:
 print"Maybe we could take the buses."
else:
 print"We still cannot decide."

if people>buses :
 print"Alright, lets just take the buses."
else:
 print"Fine, lets stay home then."

 
