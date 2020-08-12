# name = input("Enter your name")
# print("Hello",name)

# This first line is provided for you

# hrs = float(input("Enter Hours:"))
# rate = float (input("Enter rate:"))
# print("Pay:",hrs*rate)

# hrs = input("Enter Hours:")
# h = float(hrs)
# xx = input("Enter the Rate:")
# x = float(xx)
# if h <= 40:
#  	print( h  * x)
# elif h > 40:
# 	print(40* x + (h-40)*1.5*x)



# score = float(input("Enter Score: "))

# if score<=0.0:
#  print("A")

# elif(score<=0.9):
#  print("B")

# elif(score<=0.8):
#  print("C")

# elif(score<=0.7):
#  print("D")

# elif(score<=0.6):
#  print("F")

# else:
#  print("ERROR")


# def computepay(hrs,xx):
    
#     hrs = input("Enter Hours:")
#     h = float(hrs)
#     xx = input("Enter the Rate:")
#     x = float(xx)
#     if h <= 40:
#         print( h  * x)
#     elif h > 40:
#             print(40* x + (h-40)*1.5*x)
            
# computepay(h,x)            


# tot = 0 
# for i in [5, 4, 3, 2, 1] :
#     tot = tot + 1
# print(tot)

# friends = ['Joseph', 'Glenn', 'Sally']
# for friend in friends :
#      print('Happy New Year:',  friend)
# print('Done!')

# zork = 0
# for thing in [9, 41, 12, 3, 74, 15] :
#     zork = zork + thing
# print('After', zork)
# n = 5
# while n > 0 :
#     print(n)
# print('All done')

# smallest_so_far = -1
# for the_num in [9, 41, 12, 3, 74, 15] :
#    if the_num < smallest_so_far :
#       smallest_so_far = the_num
# print(smallest_so_far)

# n = 0
# while n > 0 :
#     print('Lather')
#     print('Rinse')
# print('Dry off!')


# largest = None
# smallest = None

# while True:
#     try:
#         num = input("Enter a number: ")
#         if num == 'done':
#             break
#         num = int(num)
#         if largest is None or num > largest:
#             largest = num
#         elif smallest is None or num < smallest:
#             smallest = num

#     except:
#         print("Invalid input")
#         continue

# print("Maximum is", largest)
# print("Minimum is", smallest)

# largest = None
# smallest = None

# while True:

#         num = input("Enter a number: ")
#         if num == 'done':
#             break
#         num = int(num)
#         if largest is None or num > largest:
#             largest = num
#         elif smallest is None or num < smallest:
#             smallest = num
     
#         else:
#             print("Invalid input")
#             continue

# print("Maximum is", largest)
# print("Minimum is", smallest)

# STRING
# int()
# float()
# variablename[startnum:endnum] stringslice
# str.lower()
# str.upper()
# str.replace(old,new[ ,count])
# str.capitalize()
# str.center(width[ , fillchar])
# str.endswith(suffix[ , start[ , end]])
# str.find(sub[ , start[ , end]])
# str
# str
# str
# str
# str
# str
# str


# data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
# pos = data.find('.')
# print(data[pos:pos+3])

# Use words.txt as the file name
# fname = input("Enter file name: ")
# fh = open(fname)
# for fx in fh:
#     fy = fx.strip()
#     print(fy)

# f= open("guru99.txt","w+")
# f.write("hello world")


# handle = open(filename,mode)    like write read w and r
# len()
# startswith("abdcd")
# rstrip() white space from right side 
# lstrip() white space from left side 
# stripped newline consider as white space
# .read()



# Use the file name mbox-short.txt as the file name

# fname = input("Enter file name: ")
# fh = open(fname)
# count = 0
# average = 0
# for line in fh:
#     if not line.startswith("X-DSPAM-Confidence:") : continue
#     average += float(line[20:-1].strip())
#     count = count + 1
#     #print(line)
    
# print("Average spam confidence:", (average/count))


#list
# .append()  for adding in list
# .sort()    for arrange in alphabetic order
# .split()   for convert string into list



# a = ['abd', 5, 'c']
# print(a[0])

# x = list()
# dir(x)

# fruit = 'Banana'
# fruit[0] = 'b'
# print(fruit)

fname = input("Enter file name: ")

fh = open(fname)
count = 0
for i in fh:
    fx = i.strip()
    fx = i.split()
    if i.startswith('From:'):
        print(fx[1])
        count = count + 1   
      

print("There were", count, "lines in the file with From as the first word")

fname = input("Enter file name: ")
fh = open(fname)

lst = list()

for line in fh:
    
    x = line.rstrip()
    y = x.split()
    for i in y:
       if i in lst:
            continue
            
       else:
                
          lst.append(i) 
    
    
lst.sort()    
print(lst)