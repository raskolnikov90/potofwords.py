from bs4 import BeautifulSoup
from bs4.element import Tag
import requests
from dateutil import parser
import random
import datefinder
from datetime import datetime
print(""""                                                                                
    .*///**,,,,,.              .,,*//((#(((((((((//**,,....                     
 ,*/((/       .*,,.              .,,,,.....,,,,,...                             
 ((              ,...          .,,,*,,,,///(*,,/ **.*....                       
 /            ,(/,            .,*/((((,.#######, ##(#(//**,..                   
                              ,*//*(((%####*###/,##(#(//***,,..                 
                        .   .,*// /((#%%%%% ####%%%##*//** ,,...                
 .                       ...,**/(%@@@@@@@&&%%##(((//(((/*,,,....                
   .                   ..,...  ............,,,,....               ,,            
 ....                    .//*.   .,***,,  /((#(/(*  .,*/*,,  *,.,/              
 ,,....                ,,*, .  .,****((/, . ,/. * ...,/ .      .,,,,.           
  ...,.,....,,..    .,..,, ....*//*.**(....  ,...  .,.(*. .,*.,,..,,.. ,        
      ..,,.....      //./***, .*/((,  ..    /*,,   . .*****/.....**,.,          
           ,*,      .(.,**.,,   ...,...   ,,//,.,,   . ,,,  .   .*//*,.         
           ....  . /,.****/*/((####(//, ,///(((///, .*//*/(////****,,,.,        
           **   . . ,***..*///,...   ....  . ,. .. ....     .... . .*,,**       
    ., ,  ,,   .. .,***,. .. ...,,.*/*,,/**(/..////,,*////*,..  ..  .**,*       
    ..  .      ., . */*,    . . ..   . ,**. .**/.*//*,. . .. .*...   ,,*   .    
               .,, .,*/ .. ...  .. ,/ //,*%&&,(&&& &%#,/.*...*,.  ...,,  .,.. . 
                 ,*,...,*,  ,.,..., ** .* ..,  .. (% #( *,..*,.   /..  .,,. .   
                ,,,.**,,*(,  **..   .,.*/* (#.&&,*/  * .   *,. . /,,,,,..  ,    
                    ,,,.*//,   #*...,. .,*////////*,..,**./., ../*,,..**.       
                 .      ,//,*,...%%(...**////*.**((//*,...,*,,*/ //*..          
              .,, .   ,   .#/*****.   . ..       ..,......,**,,*,,.  . ... ,..  
                 .*,, .,.   ,*****//*.    ..,. ,    .   ***,.*.,.. ,.,, ,,.     
                          ..  .,**,,,   .  ,,,,,  ... , ,. *...  .              
                     ..           *,,..,,*,.*.., ..,,,...*.    .. .,*,,,,.      
                         .,,///**,  .***. ,*,.  ,.   ,/*,   ,*...               
                               .   ,*,.,,,,. .... ..,,,.                        
                             ,,**/(#%&&%%%%%%%######((//**,,....                
                                    ........,,,....
                                    
__________       __    ________   _____   __      __                .___      
\______   \_____/  |_  \_____  \_/ ____\ /  \    /  \___________  __| _/______
 |     ___/  _ \   __\  /   |   \   __\  \   \/\/   /  _ \_  __ \/ __ |/  ___/
 |    |  (  <_> )  |   /    |    \  |     \        (  <_> )  | \/ /_/ |\___ \ 
 |____|   \____/|__|   \_______  /__|      \__/\  / \____/|__|  \____ /____  >
                               \/               \/                   \/    \/                            
""")

webpage = input('Enter website to grab info from. Example: http://company.com or http://socialmedia.com/personalprofile ')
if (webpage[-1] == '/'):
	webpage = webpage[0:-1]
if (webpage.count("http")==0):
	webpage = 'https://'+webpage

def leetspeak(word):
    word = word.replace('e','3')
    word = word.replace('E','3')
    word = word.replace('a','4')
    word = word.replace('A','4')
    word = word.replace('t','7')
    word = word.replace('T','7')
    word = word.replace('l','1')
    word = word.replace('L','1')
    word = word.replace('i','1')
    word = word.replace('I','1')
    word = word.replace('s','5')
    word = word.replace('S','5')
    word = word.replace('o','0')
    word = word.replace('O','0')
    return word
    
def specialcharacters(word):
    word = word.replace('a','@')
    word = word.replace('A','@')
    word = word.replace('s','$')
    word = word.replace('S','$')
    word = word.replace('o','0')
    word = word.replace('O','0')
    word = word.replace('i','!')
    word = word.replace('I','!')
    word = word.replace('1','!')
    word = word.replace('1','!')
    return word
def mixed(word):
    word = specialcharacters(word)
    word = leetspeak(word)
    return word
    
def shuffler(word):
    finalword = ''
    for i in range(0,len(word)):
        ranposition = random.randint(0, len(word)-1)
        finalword = finalword + word[ranposition]
    return finalword
    
def reverse(word):
    finalword = ''
    for i in range(0,len(word)):
        finalword = finalword + word[len(word) - (i+1)]
    return finalword

def get_html(url):
	try:
		#open with GET method
		resp = requests.get(url, timeout=2)
	    	#http_respone 200 means OK status
		if resp.status_code==200:
			print("Successfully opened the web page")
			soup = BeautifulSoup(resp.text,'html.parser')
			return soup.get_text()
		else:
			return "Error"
	except:
		return 'Failed connection'

htmlpage = get_html(webpage)
commonsubs = ["about", "info", "contact","blog","blogs","posts","faq","friends","groups","about_work_and_education","about_places","about_family_and_relationships", "recent-activity/all/","recent-activity", "people","employees"]



subdoms = input("Attempt directory busting? Example: webpage.com will be added adresses like webpage.com/about. Y/n? ")
if(subdoms == 'y' or  subdoms == 'Y' or subdoms == 'yes' or subdoms == 'Yes'):
	indepth = input('Wanna explore directories in depth? 100 directories? May take a lot of time Y/n  ')
	if(indepth == 'y' or  indepth == 'Y' or indepth == 'yes' or indepth == 'Yes'):
		dirdepth = get_html('https://raw.githubusercontent.com/rbsec/dnscan/master/subdomains-100.txt')
		dirdepth = dirdepth.split()
		for dirs in dirdepth:
			commonsubs.append(dirs)

if(subdoms == 'y' or  subdoms == 'Y' or subdoms == 'yes' or subdoms == 'Yes'):
	for subs in commonsubs:
		resp = requests.get(webpage+"/"+subs, timeout=2)
		if resp.status_code==200:
			htmlpage = htmlpage + get_html(webpage+"/"+subs)
			print(webpage+"/"+subs+" Added")

morewebsites = input("Do you wanna add another website. Y/n?  ")
while morewebsites == 'y' or morewebsites == 'yes' or morewebsites == 'Y' or morewebsites == 'Yes':
	webpage2 = input('Enter website to grab info from. Example: http://company.com or http://socialmedia.com/personalprofile ')
	if (webpage2.count("http")==0):
		webpage2 = 'https://'+webpage2
	htmlpage = htmlpage + get_html(webpage2)
	print(webpage2 + " info found an added")
	morewebsites = input("Do you wanna add another website. Y/n?  ")


suffixes = ["2020", "2021", "2023","123","2022","1234","xxx", "1", "$","qwerty","66","1122",'321','420','69','one','One','admin','7','77',
'1995','58','1996','1987','1994','1988','1985','1983','1992','1982','1984','1986','2000','987','989','000','98','96','00','87','76','79','99','75','64','11','23','25','0','777','66','07','001','999','666','111','10','35','abc','ABC','&','4ever','my','love','mylove','lover','king','queen','destroyer','horny','cock','pussy','holy']
connectors = ["-", ".","_","/","!","@",'#','$','&','+','^',':']
suffixes = suffixes + connectors

datelist = datefinder.find_dates(htmlpage)
#Will find dates in the text
for dates in datelist:
    dates = str(dates)
    dates = dates.replace('-','')
    suffixes.append(dates[0:4])
    suffixes.append(dates[4:8])
    suffixes.append(dates[2:4])

#adding top 500 suffixes
topsuffix = get_html("https://raw.githubusercontent.com/raskolnikov90/ComplexPassAnalysisAndWordlists/main/tops/topsuffixes.txt")
topsuffix = topsuffix.split()
suffixes = suffixes + topsuffix

#removing duplicates in suffixes
suffixes = [*set(suffixes)]

unnecessary = ['error',',','.',"'","index",'-','/','@',':']

for words in unnecessary:
	htmlpage = htmlpage.lower().replace(words, " ")
	
wordlist = htmlpage.split()
common = []
for words in wordlist:
    for duplicates in common:
        if(duplicates == words):
            common.remove(duplicates)
    if(htmlpage.count(words) >= 3 and len(words) >= 2):
        common.append(words)
        wordlist.remove(words)
    else:
        wordlist.remove(words)
with open("commonwordsinpage.txt","w") as file:
	for words in common:
	    file.write(words+"\n")
	print("commonwordsinpage.txt created, added "+ str(len(common))+ " most common words")
	    
leastcommon = []
for words in wordlist:
    for duplicates in leastcommon:
        if(duplicates == words):
            leastcommon.remove(duplicates)
    if(htmlpage.count(words) <= 2 and len(words) >= 2):
        leastcommon.append(words)
        wordlist.remove(words)
    else:
        wordlist.remove(words)
with open("leastcommonwords.txt","w") as file:
	for words in leastcommon:
	    file.write(words+"\n")
	print("leastcommonwords.txt created, added "+ str(len(leastcommon))+ " least common words")
	
phrases = wordlist
passphrases = []
for i in range(0, len(phrases)):
    if i+1 < len(phrases):
        if passphrases.count(phrases[i]+phrases[i+1] and common.count(phrases) > 0) == 0:
            passphrases.append(phrases[i]+phrases[i+1])
            passphrases.append(phrases[i].capitalize()+phrases[i+1].capitalize())
        if i+2 < len(phrases):
            if passphrases.count(phrases[i]+phrases[i+1]+phrases[i+2] and common.count(phrases) > 0) == 0:
                passphrases.append(phrases[i]+phrases[i+1]+phrases[i+2])
                passphrases.append(phrases[i].capitalize()+phrases[i+1].capitalize()+phrases[i+2].capitalize())
with open("passphrases.txt","w") as file:
	for words in passphrases:
	    file.write(words+"\n")
	print("passphrases.txt created, added "+ str(len(passphrases))+ " phrases")

shufflingoptions = input("""What you wanna do now?
1-Add capitalization, prefixes, suffixes and rules to words. Example: blah into blah2020, Blah123, B!@h123.
2-Randomly combine common and least common words found. Example: words blah and bleh into blah@bleh or Blah.Bleh
3-Do both
""")

if(int(shufflingoptions) == 1 or int(shufflingoptions) == 3):
	with open("finalwordlist.txt","w") as file:
		for words in common:
			file.write(words+"\n")
			file.write(words.capitalize()+"\n")
			file.write(leetspeak(words)+"\n")
			file.write(specialcharacters(words)+"\n")
			file.write(mixed(words)+"\n")
			words = words.capitalize()
			file.write(leetspeak(words)+"\n")
			file.write(specialcharacters(words)+"\n")
			file.write(mixed(words)+"\n")
			file.write(shuffler(words)+"\n")
			file.write(reverse(words)+"\n")
			words = words.upper()
			file.write(words+"\n")
			words = words.lower()
			for suffix in suffixes:
				file.write(words+suffix+"\n")
				file.write(words.capitalize()+suffix+"\n")
				file.write(suffix+words+"\n")
				file.write(suffix+words.capitalize()+"\n")
				file.write(leetspeak(words)+suffix+"\n")
				file.write(specialcharacters(words)+suffix+"\n")
				file.write(mixed(words)+suffix+"\n")
				file.write(shuffler(words)+suffix+"\n")
				file.write(reverse(words)+suffix+"\n")
				file.write(suffix+leetspeak(words)+"\n")
				file.write(suffix+specialcharacters(words)+"\n")
				file.write(suffix+mixed(words)+"\n")
				file.write(suffix+shuffler(words)+"\n")
				file.write(suffix+reverse(words)+"\n")
				words = words.capitalize()
				file.write(leetspeak(words)+suffix+"\n")
				file.write(specialcharacters(words)+suffix+"\n")
				file.write(mixed(words)+suffix+"\n")
				file.write(shuffler(words)+suffix+"\n")
				file.write(reverse(words)+suffix+"\n")
				file.write(suffix+leetspeak(words)+"\n")
				file.write(suffix+specialcharacters(words)+"\n")
				file.write(suffix+mixed(words)+"\n")
				file.write(suffix+shuffler(words)+"\n")
				file.write(suffix+reverse(words)+"\n")
				words = words.upper()
				file.write(words+suffix+"\n")
				file.write(suffix+words+"\n")
				words = words.lower()
		print("added suffixes, prefixes and variations to wordlist and saved as finalwordlist.txt")
	with open("finalwordlist.txt","r") as file:
		print(str(len(file.readlines())) + " words")
		
	with open("finalwithleastcommon.txt","w") as file:
		for words in leastcommon:
			file.write(words+"\n")
			file.write(words.capitalize()+"\n")
			file.write(leetspeak(words)+"\n")
			file.write(specialcharacters(words)+"\n")
			file.write(mixed(words)+"\n")
			words = words.capitalize()
			file.write(leetspeak(words)+"\n")
			file.write(specialcharacters(words)+"\n")
			file.write(mixed(words)+"\n")
			file.write(shuffler(words)+"\n")
			file.write(reverse(words)+"\n")
			words = words.upper()
			file.write(words+"\n")
			words = words.lower()
			for suffix in suffixes:
				file.write(words+suffix+"\n")
				file.write(words.capitalize()+suffix+"\n")
				file.write(suffix+words+"\n")
				file.write(suffix+words.capitalize()+"\n")
				file.write(leetspeak(words)+suffix+"\n")
				file.write(specialcharacters(words)+suffix+"\n")
				file.write(mixed(words)+suffix+"\n")
				file.write(shuffler(words)+suffix+"\n")
				file.write(reverse(words)+suffix+"\n")
				file.write(suffix+leetspeak(words)+"\n")
				file.write(suffix+specialcharacters(words)+"\n")
				file.write(suffix+mixed(words)+"\n")
				file.write(suffix+shuffler(words)+"\n")
				file.write(suffix+reverse(words)+"\n")
				words = words.capitalize()
				file.write(leetspeak(words)+suffix+"\n")
				file.write(specialcharacters(words)+suffix+"\n")
				file.write(mixed(words)+suffix+"\n")
				file.write(shuffler(words)+suffix+"\n")
				file.write(reverse(words)+suffix+"\n")
				file.write(suffix+leetspeak(words)+"\n")
				file.write(suffix+specialcharacters(words)+"\n")
				file.write(suffix+mixed(words)+"\n")
				file.write(suffix+shuffler(words)+"\n")
				file.write(suffix+reverse(words)+"\n")
				words = words.upper()
				file.write(words+suffix+"\n")
				file.write(suffix+words+"\n")
				words = words.lower()
		print("added suffixes, prefixes and variations to least common wordlist and saved as finalwithleastcommon.txt")
	with open("finalwithleastcommon.txt","r") as file:
		print(str(len(file.readlines())) + " words")
	with open("finalwithpassphrases.txt","w") as file:
		for words in passphrases:
			file.write(words+"\n")
			file.write(leetspeak(words)+"\n")
			file.write(specialcharacters(words)+"\n")
			file.write(mixed(words)+"\n")
			file.write(words.upper()+"\n")
			file.write(shuffler(words)+"\n")
			file.write(reverse(words)+"\n")
			for suffix in suffixes:
				file.write(words+suffix+"\n")
				file.write(suffix+words+"\n")
				file.write(leetspeak(words)+suffix+"\n")
				file.write(specialcharacters(words)+suffix+"\n")
				file.write(mixed(words)+suffix+"\n")
				file.write(shuffler(words)+suffix+"\n")
				file.write(reverse(words)+suffix+"\n")
				file.write(suffix+leetspeak(words)+"\n")
				file.write(suffix+specialcharacters(words)+"\n")
				file.write(suffix+mixed(words)+"\n")
				file.write(suffix+shuffler(words)+"\n")
				file.write(suffix+reverse(words)+"\n")
				
				file.write(words.upper()+suffix+"\n")
				file.write(suffix+words.upper()+"\n")
		print("added suffixes, prefixes and variations to passphrases wordlist and saved as finalwithpassphrases.txt")
	with open("finalwithpassphrases.txt","r") as file:
		print(str(len(file.readlines())) + " words")
		
if(int(shufflingoptions) == 2 or int(shufflingoptions) == 3):
	connectors.append("")
	with open("randomcombinations.txt","w") as file:
		for i in range(0, 200000):	
			file.write(random.choice(common)+random.choice(connectors)+random.choice(leastcommon)+"\n")
			file.write(random.choice(common).capitalize()+random.choice(connectors)+random.choice(leastcommon)+"\n")
			file.write(random.choice(common).capitalize()+random.choice(connectors)+random.choice(leastcommon).capitalize()+"\n")
			file.write(random.choice(common)+random.choice(connectors)+random.choice(leastcommon).capitalize()+"\n")
			
			file.write(random.choice(leastcommon)+random.choice(connectors)+random.choice(common)+"\n")
			file.write(random.choice(leastcommon).capitalize()+random.choice(connectors)+random.choice(common)+"\n")
			file.write(random.choice(leastcommon).capitalize()+random.choice(connectors)+random.choice(common).capitalize()+"\n")
			file.write(random.choice(leastcommon)+random.choice(connectors)+random.choice(common).capitalize()+"\n")
				
		print("randomly combined words and saved as randomcombinations.txt")
	with open("randomcombinations.txt","r") as file:
		print(str(len(file.readlines())) + " words")
		
