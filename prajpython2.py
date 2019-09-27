count = 0;  
word = "";  
maxCount = 0;  
words = [];  
   
#Opens a file in read mode  
file = open("test.txt", "r")  
      
#Gets each line till end of file is reached  
for line in file:  
    #Splits each line into words  
    string = line.lower().replace(',','').replace('.','').split(" ");  
    #Adding all words generated in previous step into words  
    for s in string:  
        words.append(s);  
   
#Determine the most repeated word in a file  
for i in range(0, len(words)):  
    count = 1;  
    #Count each word in the file and store it in variable count  
    for j in range(i+1, len(words)):  
        if(words[i] == words[j]):  
            count = count + 1;  
              
    #If maxCount is less than count then store value of count in maxCount  
    #and corresponding word to variable word  
    if(count > maxCount):  
        maxCount = count;  
        word = words[i];  
          
print("Most repeated word: " + word);  
file.close();  


test.txt: 

Python is a high-level, interpreted, interactive and object-oriented scripting language. Python is designed to be highly readable. It uses English keywords frequently where as other languages use punctuation, and it has fewer syntactical constructions than other languages.
Python is a MUST for students and working professionals to become a great Software Engineer specially when they are working in Web Development Domain.

Output:

Most repeated word: python

