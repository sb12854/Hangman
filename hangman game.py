import random 
import string 

def printmatches (word,x):
    y = len(word)
    z = [" "] *y 
    i = 0 
    while i<y:
        if word[i] == x: 
            z[i] = x 
        else:
            z[i] = " "  
        i+=1

    return (z)

def append(string,chars): ##append list to a string
    q = 0
    ##d=0
    while q < len(string): 
        if string[q] == " " and chars[q] != " ":
            string[q] = chars[q]
      ##      d+=1
        q+=1
    return string  ##THIS MUST HAVE A RETURN STATEMENT, ELSE IT IS NONETYPE!!!
    ##return d ##ALTERNATIVE IS TO RETURN STRING 

def convertlist(x):
    q = " "
    a = 0
    ##x= list(x) 
    while (a < len(x)):
        q+=x[a]
        a+=1
    return (q) 

x = random.randint(0,55899)
try:
    f = open('words.txt', 'r')
    s = " "
    s = f.readline()

    L = s.split() 
     
    word = L[x]

    f.close()

except IOError:
    print('file not found')

q=0
 
current = [" "] * len(word)  
c = 0
char = " " 
while char != word and q < 3:
    print "Enter a letter"
    char = raw_input (" ")  
    ##current.append(printmatches(word,char)) 
    append(current, printmatches(word,char)) 
    str = (append(current, printmatches(word,char))) ##CAN'T REMOVE BRACKETS, ELSE INTERPRETS AS CONTINUATION OF BRACKETED REGION 
    ##c+=append(current, printmatches(word,char))
##    if (c == len(word)):
##        print 'Congratulations, you have won'
##        break  
    if (str == list (word)):  ##an ALTERNATIVE
        print word 
        print 'Congratulations, you have won'
        break 
    if printmatches(word,char) == [" "]*len(word):    
        print "You have ", (2-q), " guesses left"   
        q+=1 
    if (q == 3):
        print "The word was ", word 
        print "Game over" 
    print ' '.join(current) ##this is like string (list) cast      
