from bs4 import BeautifulSoup
from bs4.element import Tag
import requests
from dateutil import parser

blocks = ["p", "h1", "h2", "h3", "h4", "h5", "blockquote", "div", "title"]

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

webpage = input('Enter website to grab info from. Example: company.com or socialmedia.com/personalprofile ')
if (webpage[-1] == '/'):
	webpage = webpage[0:-1]
	


def get_html(url):
	#open with GET method
	resp = requests.get(url)
    	#http_respone 200 means OK status
	if resp.status_code==200:
		print("Successfully opened the web page")
		soup = BeautifulSoup(resp.text,'html.parser')
		return soup.get_text()
	else:
		return "Error"

htmlpage = get_html(webpage)
commonsubs = ["about", "info", "contact","blog","blogs","posts","faq","friends","groups","about_work_and_education","about_places","about_family_and_relationships", "recent-activity/all/","recent-activity", "people","employees"]
subdoms = input("Attempt gathering from subdomains? Example: webpage.com will be added adresses like webpage.com/about. Y/n? ")

if(subdoms == 'y' or  subdoms == 'Y' or subdoms == 'yes' or subdoms == 'Yes'):
	for subs in commonsubs:
		if(get_html(webpage+"/"+subs) != "Error"):
			htmlpage = htmlpage + get_html(webpage+"/"+subs)
			print(webpage+"/"+subs + " info found an added")

suffixes = ["2020", "2021", "2023","123","2022","1234","xxx", "1", "$","qwerty","66","1122",'321','420','69','one','One','admin']
connectors = ["-", ".","_","/","!","@",'#','$']

datelist = htmlpage.split()
#Will find dates in the text
for dates in datelist:
    if(len(dates)>2 and htmlpage.count(dates) > 1):
        if(dates[2]=="/"):
            daymonth = dates[0:5]
            suffixes.append(daymonth.replace("/", ""))
        if(dates[2]=="/" and dates[5]=="/"):
            suffixes.append(dates[:10].replace("/", ""))
            justyear = dates[5:10]
            suffixes.append(justyear.replace("/", ""))
            if(len(justyear) > 4):
                justyear = justyear[3:5]
                suffixes.append(justyear.replace("/", ""))
        if(dates[2]=="-"):
            daymonth = dates[0:5]
            suffixes.append(daymonth.replace("-", ""))
        if(dates[2]=="-" and dates[5]=="-"):
            suffixes.append(dates[:10].replace("-", ""))
            justyear = dates[5:10]
            suffixes.append(justyear.replace("-", ""))
            if(len(justyear) > 4):
                justyear = justyear[3:5]
                suffixes.append(justyear.replace("-", ""))

#removing duplicates in suffixes
suffixes = [*set(suffixes)]

#removing unnecesary words
unnecessary = [" is"," are"," the", " of", " they", " them", " she", " he", " these", " what", " when"," where"," who"," is", " no", " yes", " good", " bad", " a ", " this", "This ", " up ", " one ", " time ", '"', ':', '(', ')', " you'll ", " comments ", " point ", " by ", "support", " hours ", " hour ", "minutes", "seconds", "first", "second", " third ", "information", " user ", " my ", " which ", "terms", "privacy", "entries", " don't ", " doesn't ", " should ", " shouldn't ", ",", " discussion ", " login ", " store ", " forum ", " discuss ", ". ", "could", "couldn't", " public ", " rights ", "search", " general ", " layout ", " since ", " options ", " before ", " after ", " going ", " please ", " let's ", " however ", " check ", " comes ", " engagement ", "today ", "authentication", " though ", " provide ", ' while ', ' and ', '...', ' including ', ' includes ', ' findings ', ' finding ', 'about']

for words in unnecessary:
	htmlpage = htmlpage.lower().replace(words, " ")


wordlist = htmlpage.split()
common = []
for words in wordlist:
    for duplicates in common:
        if(duplicates == words):
            common.remove(duplicates)
    if(htmlpage.count(words) >= 3 and len(words) > 4):
        common.append(words)
        wordlist.remove(words)
    else:
        wordlist.remove(words)
with open("commonwordsinpage.txt","w") as file:
	for words in common:
	    file.write(words+"\n")
	print("commonwordsinpage.txt created, added "+ str(len(common))+ " words")
	    



addsuffixes = input("Add capitalization and suffixes to words? Example: blah into blah2020, Blah123. Y/n? ")

if(addsuffixes == 'y' or  addsuffixes == 'Y' or addsuffixes == 'yes' or addsuffixes == 'Yes'):
	with open("finalwordlist.txt","w") as file:
		for words in common:
			file.write(words+"\n")
			file.write(words.capitalize()+"\n")
			for suffix in suffixes:
				file.write(words+suffix+"\n")
				file.write(words.capitalize()+suffix+"\n")
				for connector in connectors:
					file.write(words+connector+suffix+"\n")
					file.write(words.capitalize()+connector+suffix+"\n")
		print("added suffixes to worlist and saved as finalwordlist.txt")
	with open("finalwordlist.txt","r") as file:
		print(str(len(file.readlines())) + " words")
		
		
