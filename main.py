# # ################################ Task 0
# ''
## Write a function which will find all such numbers which are divisible by 7 but
## are not a multiple of 5  in range  from x to y (both included).
## The numbers obtained should be printed in a comma-separated sequence on a
## single line. Don't forget about function documentation
#
# ''

# def find(x, y):
#     result = []
#     for i in range(x,y+1):
#         if i % 7 == 0 and i % 5 != 0:
#             result.append(str(i))
#     return ",".join(result)
#
#
# print(find(1000,2101))

# ''
# # ################################ Task 1
## A website requires the users to input username and password to register.
## Create function to check the validity of password input by users.
## Using continue() or break().
## Following are the criteria for checking the password:
## 1. At least 1 letter between [a-z]
## 2. At least 1 number between [0-9]
## 3. At least 1 letter between [A-Z]
## 4. Minimum length of transaction password: 4
## 5. Maximum length of transaction password: 8
## You should to document your code by using python docstrings (google)
## Save result to *.txt file

import string

# def check(**kwargs):
#     password = ''
#     for i in kwargs.items():
#         if i[0] == 'haslo':
#             password = list(i[1])
#             break
#
#     a = False
#     b = False
#     c = False
#     d = False
#
#
#
#     for i in password:
#         if i.islower() and i.isalpha() :
#             a = True
#             break
#
#     for i in password:
#         if i.isdigit() :
#             b = True
#             break
#
#     for i in password:
#         if i.isupper() and i.isalpha() :
#             c = True
#             break
#
#     if len(password) >=4 and len(password) <= 8:
#         d = True
#
#     print(a,b,c,d)
#     if a and b and c and d:
#         return True
#     else:
#         return False
#
# print(check(login = 'maniek', haslo = 'Tajne1'))

################ Task 2
# Write a function which will find all such numbers which are divisible by 7 but
# are not a multiple of 5  in range  from x to y (both included).
# The numbers obtained should be printed in a comma-separated sequence on a
# single line.
# You should to document your code by using python docstrings
# (dokumentacja kodu styl google)
# Wykonaj na Lab6:  Don't forget to handle exceptions (obsłudze wyjątków)
# Save result to *.pkl file use picle package
#

# def find(x, y):
#     result = []
#     for i in range(x,y+1):
#         if i % 7 == 0 and i % 5 != 0:
#             result.append(str(i))
#     return ",".join(result)
#
#
# print(find(1000,2101))


################ Task 3
## Create function with multiple arguments (x1,x2,...,xn) that accepts a sequence of
## comma-separated numbers from console and returns:
## x1^x1  if number of input parameters equals 1 than y = x1^x1
## x1^x1, x2^x2 if number of input parameters equals 2
## x1^x1, x2^x2, x3^x3 if number of input parameters equals 3
## ....
## x1^x1, ... , x99^x99 if number of input parameters equals 99
## if number of input parameters equals greater than 100 will display an error message.
## Requirements:
## Name of input parameters:
## You should to document your code by using python docstrings (google)
###############

# def fun(*args):
#     list1 = []
#     for i in args:
#         if i < 100:
#             list1.append(i*i)
#         else:
#             print("Error")
#
#     return list1
#
# print(fun(1,2,3,4,5,6,7,8,9,0))

################ Task 4
## Create function with multiple arguments (x1,x2,...,xn) that accepts a sequence of
## comma-separated numbers from console and returns:
## x1^x1  if number of input parameters equals 1 than y = x1^x1
## x1^x1, x2^x2 if number of input parameters equals 2
## x1^x1, x2^x2, x3^x3 if number of input parameters equals 3
## ....
## x1^x1, ... , x99^x99 if number of input parameters equals 99
## if number of input parameters equals greater than 100 will display an error message.
## Requirements:
## Use: dynamic variable name (exec() or globals() or locals())
## Name of input parameters: x1, x2, ..., xn
## You should to document your code by using python docstrings (google)
## Wykonaj na Lab6:  Don't forget to handle exceptions (obsłudze wyjątków)
###############

# def fun(*args):
#     list1 = []
#     if len(args) > 100:
#         return "Error"
#
#     if len(args) == 0:
#         return ""
#
#     results = []
#     dynamic_namespace = {}
#
#     for index, value in enumerate(args, start=1):
#         var_name = f"x{index}"
#         dynamic_namespace[var_name] = float(value)
#         exec(f"res = {var_name} ** {var_name}", {}, dynamic_namespace)
#         results.append(str(dynamic_namespace['res']))
#
#     return ", ".join(results)
#
# print(fun(1,2,3,4,5))


########################## Task 5 ########################
## The first step,
## generate test data: create folder. Create 5 text files to this folder,
## each file contains more than 5 sentences.
## Filenames: Text1ID_ABC, Text2ID_405.txt, Text3ID_607.txt, Text4ID_ABC5.txt, Text5ID_DEF.txt
##
## Create function with multiple arguments that:
## a) print all file from folder
## b) if the file name contains 'ABC', count how many words in the text of file
## contain words with more than 3 letters
## Wykonaj na Lab6:  Next step, decorate this function, add the following functionality:
## a) the function will check how many files have 0 in the filename
## b) if the file has 0 in the filename then the function counts words in the text of the file
## c) if the filename contains 'EF.txt', then the function copy this file to
## 'DocumentLab5copy' directory

# import os
#
#
# def createFiles(folderName, files):
#     os.makedirs(folderName,exist_ok=True)
#
#     text = (
#         "To jest pierwsze zdanie w pliku. \n"
#         "To jest drugie zdanie w pliku. \n"
#         "To jest trzecie zdanie w pliku. \n"
#         "To jest czwarte zdanie w pliku. \n"
#         "To jest piąte zdanie w pliku. \n"
#         "To jest szóste zdanie w pliku. \n"
#     )
#
#     for file in files:
#         path = os.path.join(folderName, file)
#         with open(path, "w", encoding="utf-8") as f:
#             f.write(text)
#
#
# files = ["Text1ID_ABC.txt", "Text2ID_405.txt", "Text3ID_607.txt", "Text4ID_ABC5.txt", "Text5ID_DEF.txt"]
#
# createFiles("folder",files)
#
# def func(folderName, txt):
#     files = os.listdir(folderName)
#     for file in files:
#         print(file)
#
#         if txt in file:
#             path = os.path.join(folderName, file)
#             with open(path, "r", encoding="utf-8") as f:
#                 text = f.read()
#                 words = text.split()
#                 counter = 0
#                 for word in words:
#                     if len(word.strip(".,!?")) > 3:
#                         counter += 1
#                 print(counter)
#
# func("folder", "ABC")