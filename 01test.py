#TO DO -to delete extra spaces in the set strings
#this is a scrypt to transform juniper's "show|compare" output to the "set" view
#you are welcome to check and change whatever you want) 

import re
import sys

#a pattern(python's regular expression) to check that the string makes sence to be converted
pattern_edit = r"([\[edit]{5}|-|\+|\s)(.+)([}\]{;])"

#a pattern to delete extra spaces before the expression
pattern_spaces = r"\s[^\S]"

#a list to save each string and transform to set-string
acommand = []

#open a file with show|compare configuration
with open('r1-tln-tix-ee-gi-0-1-to-ge-2-2-0.txt','r') as f:
    #open every string from the file without "new string" symbol
    for n,line in enumerate(f, 1):
        line = line.rstrip('\n')
        first = re.search(pattern_edit, line)

        #to check that the string is worth working with
        if(first != None):
            #starting new list anr clear a list with previous configuration
            if ((first.group(1)=='[edit')):
                acommand.clear()

            #adding a new string to the list to make set string at the end, checking that the string should be saved into the list(have + or edit at
            #the begining and doesn't have ';' at the end)
            if ((first.group(1)=='[edit')or((first.group(1)=='+'))) and (first.group(3)!='}')and(first.group(3)!=';'):
                string_without_spaces = re.sub(pattern_spaces, '', first.group(2))
                acommand.append(' ' + string_without_spaces)

            #checking that the string the last in set group and the whole command should be printed with 'set' or 'delete' argument
            if (first.group(3)==';')and (first.group(1)=='+'):
                print('set', end='')
                for i in acommand:
                    print(i,end = '')
                string_without_spaces = re.sub(pattern_spaces, '', first.group(2))
                print (' ' + string_without_spaces)
            elif (first.group(3)==';')and (first.group(1)=='-'):
                print('delete', end='')
                for i in acommand:
                    print(i,end = '')
                string_without_spaces = re.sub(pattern_spaces, '', first.group(2))
                print (' ' + string_without_spaces)

