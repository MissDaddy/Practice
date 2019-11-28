
# coding: utf-8

# <div class="alert alert-block alert-info"><br>
#     <h2>4. Unstructured Data: Processing and Querying Texts</h2> <br>
#     <p>Here we'll learn how to open and write text files as well as how to clean them before matching patterns and extracting textual data.</p>
# </div>

# In[1]:


# First open the .txt file called 'The Tyger' which is a famous poem by William Blake. 
# Currently, there is his exhibition at Tate (https://www.tate.org.uk/whats-on/tate-britain/exhibition/william-blake-artist)

# The file should be in uploaded into your working folder.

file = open('Tyger.txt', 'r')

# 'r' indicates the mode of tackling files. In this case, it means 'read' the exisiting file. 
# The other modes are 'w' to write a new file and 'a' to append data to the exisiting file 
# This is storing the poem as 'file'.


# In[2]:


# Now we can use the file variable to read the content of the .txt files. The poem becomes one long string.

poem = file.read()

# Note that if you enter file.read() a second time, the text will be removed from the file. 
# You will need to enter file=open('') again to recreate the file.


# In[3]:


# Print out the content of the text file stored in the poem variable.

poem

# \n marks a new line.


# In[4]:


# Let's open the poem file again. This time let's use print() function to print out its content while reading the file.

file = open('Tyger.txt', 'r')
print(file.read())

# The new line entries \n are removed in favour of a more readable format.
#print(<NAME>.read ()) printes it in the original format.

# Th poem is currently one long string that we need to tokenise into single words we can lop through.


# In[5]:


# Data cleaning is the most important and time-consuming task in processing data.
# While working with natural language, you'll have to make all sorts of changes to texts before you can extract data from them.
# For example, you may want to remove characters like punctuation or apostrophe from abbreviations as in "can't".
# It may be also good to turn all text to lower cases so that we do not count 'could' and 'Could' as different words.

# You may use replace() method to do some cleaning in chain.
# Remove full stops, commas and ampersands, and turn all text to lower cases with lower()

plainPoem = poem.replace('.', '').replace(',', '').replace('?', '').replace('&', '').lower()

# the first argument says what is to be removed, the second argument says to replace the unwanted character with a space.


# Print our the poem variable to see whether the unwanted items are removed.

plainPoem


# In[25]:


# Let's get rid of the title and the author because these are a paratext rather than the main text.
# The simplest technique in this case would be to use the conditional statement
# In the conditional, use the string method startswith()to match the unwanted portion of the text


if plainPoem.startswith("the tyger by william blake"):
    new = plainPoem.replace("the tyger by william blake", '')

print(new)

# This works well if you have one or two items to remove.

# In more complex cases, use Regex (regular expressions)to match text segments that recur throughout the text.


# In[7]:


# To count and otherwise query words in a long string, you may wish to split that string into a list of words first.

wordList = new.split()
print(wordList)


# In[8]:


# The quickest way to count word frequencies is to import the Counter method from the collections module.
# But Counter works with lists. This is why we converted our string variable 'plainPoem' into the list 'wordList' as above.

from collections import Counter

wordCount = Counter(wordList)
wordCount

# The output though is the dictionary variable 'wordCount'.


# In[9]:


# Before we explore an alternative way of counting word frequencies, let's see how the list method count() works.
# You may pass a specific word as an argument to find out how many times it appears in the text. 

wordList.count('bright')


# In[10]:


# Try to count in the traditional way with loops.

myPoem = new.split()

# myPoem now is a list of short strings (words) that we get after breaking a long string (poem).

myPoem


# In[11]:


# We'll generate a dictionary where words are keys and their frequencies are values.

# Start with an empty dictionary and then iterate with the for loop through the myPoem list.
# We want to loop through each item in the list while counting and also add the count to each word.

wordDict1 = {}

for word in myPoem:
    wordDict1[word] = myPoem.count(word)

print(wordDict1)


# In[12]:


# The third way is similar to the previous one. Yet we'll use the get() method which works with dictionaries.

# Start with an empty dictionary and then iterate with the for loop througthe myPoem list again

wordDict2 = {}

for word in myPoem:
    wordDict2[word] = wordDict2.get(word, 0)+1

    
# wordDict2.get(word, 0) tells Python to look for the key 'word' in wordDict2. 
# If the key 'word' is not found, it returns 0. 
# Since this is the first time 'word' is passed through the loop, it is not found in wordDict2 yet
# So the get() method returns 0. 
# This 0 value is then added to the 1 present in the equation. 
# After the completion of the first loop using the 'word', we now have an entry in the dictionary like this: {'word': 1}    

wordDict2


# In[31]:


# As already mentioned, data cleaning is an essential part in data collection and analysis. 
# E.g. you may wish to remove stopwords from the text.  
# Stopwords are the most frequent words in any language, e.g. articles or pronouns in English
# Counting grammar words may not be valuable for literary analysis, though a lexicographer may find them fascinating.
# Stylommetry (aka authorship analysis) would be interested in counting both, for example.

# Let's define our own list of stopwords to be removed from the text before we analyze it.

stopWords = ['a', 'the', 'is', 'to', 'their', 'by', 'in', 'thy', 'and', 'with', 'who', 'he']

    
stopWords


# In[32]:


# Start with an empty list in which we will store the cleaned text

wordListClean = []

for w in wordList:
    if w not in stopWords:
        wordListClean.append(w)
        
print(wordListClean)
 
# Look at the poem and decide what other words you find to be insignificant or irrelevant to your analysis.

# Write a new or expanded stoplist and use it to clean this text once again. Print out the cleaned text.


# In[33]:


# Recount word frequencies in the newly cleaned text.

wordDict3 ={}

for word in wordListClean:
    wordDict3[word] = wordDict3.get(word, 0)+1
    
wordDict3


# In[34]:


# You can convert a dictionary into a list with items() methods.

listPoem = [ [k,v] for k, v in wordDict3.items() ]

listPoem


# ### Querying texts with Regex 

# In[17]:


# We can use regular expressions to match and extract the recurring textual data, e.g. phrases, collocations and the like.

# To use the regex tool, we need to import the re module. re = regular expressions.

import re

# Letter 'r' marks the regex pattern that needs to be matched in the text

phrase1 = re.findall(r"burning bright",plainPoem)

print(phrase1)


# In[18]:


# You might have noticed with the naked eye that 'what' is rather repetitive in The Tyger.
# Let's match them and extract.

# \b marks the boundaries of the word or words we want to match. In this case 'what'
# If we don't mark the boundaries, the regex will fetch any word that contains 'what' as 'what', 'whatever', 'whatsoever',etc
# \w+ means find any word that goes after 'what'

phrase2 = re.findall(r"\bwhat\b \w+", plainPoem)
phrase2


#You can add aditional \w+ , \w+ to retrieve the two words following 'what'


# In[19]:


# The search for patterns by prepositions might be rewarding.
# Let's explore what lexical words the preposition 'of' attracts in Blake's poem.

phrase3 = re.findall(r"\w+ \bof\b \w+", plainPoem)

# Tell out loud what the regex above does.

phrase3                


# In[20]:


# We may write several regex patterns to find words that end in some rhyme. 
# To find more than one word, use the vertical bar to say 'find this or that'
# If you know what rhyme/ending you want to fetch use \w+ for any word plus a particular ending, e.g. \w+ight

phrase4 = re.findall(r"\w+ight|\w+ire\b", plainPoem)

#Vertical bar means 'or'

phrase4


# In[36]:


# Finally, write a new file in which we'll save what we extracted.
# We'll use the same command as for the reading of files. Yet, the mode here should be 'w' ('write'). 
# Also give the name to the new file.

file = open('TygerPhrases.txt', 'w')

#w = 'write'

# This command has created an empty file in your working directory.

# Now use the file variable to write the content into that empty file called 'TygerPhrases'.
# Pass the variable phrase3 as the argument to tell the programme to save its content in this new file with the write() method.

# Remember that phrase3 is a list, while we need to save it as a string; hence use the conversion function as well. 

file.write(str(phrase3))

file.close()

#Last line must be included.
# Check it now in your directory.


# <div class="alert alert-block alert-success">
# <h2> Over to You!</h2>
# <ol>
# <li>In a code cell, write a regex that matches the phrases that contain the preposition 'of' as above. Yet this time you need to find phrases with one word preceding and two words following the preposition, e.g. '\w+ of \w+ \w+'. Store the matches in a variable and print it out.</li><br>
# <li>This time explore some sound patterns of this poem. In another code cell, write a regex that matches all wordforms that end with -ight and -ire. Store the matches in a new variable and print it out.</li><br>
# <li>In the third code cell, write the code that puts both variables together and writes them in a new .txt file.</li><br>
# <li>In the fourth code cell, write the code that reads in a text of your choosing. Then write a regex that matches some new patterns we haven't explored. And write the matches in another new .txt file. </li><br>
# </ol>
# </div>

# ### Below are a few references to  research that exemplifies how to use regex in various contexts:  
# 
# https://programminghistorian.org/en/lessons/understanding-regular-expressions  
# https://historicaltexts.jisc.ac.uk/help  
# http://www.themacroscope.org/?page_id=643  
# https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2656039/  
# http://ceur-ws.org/Vol-1267/LD4IE2014_Petrovski.pdf  
# https://essay.utwente.nl/73817/1/chenet_MA_EEMCS.pdf  
