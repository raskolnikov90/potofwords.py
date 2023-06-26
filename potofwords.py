from bs4 import BeautifulSoup
from bs4.element import Tag
import requests
from dateutil import parser
import random

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


def get_html(url):
	try:
		#open with GET method
		resp = requests.get(url, timeout=5)
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


subdoms = input("Attempt gathering from subdomains? Example: webpage.com will be added adresses like webpage.com/about. Y/n? ")
if(subdoms == 'y' or  subdoms == 'Y' or subdoms == 'yes' or subdoms == 'Yes'):
	indepth = input('Wanna explore directories in depth? 100 directories? Y/n  ')
if(indepth == 'y' or  indepth == 'Y' or indepth == 'yes' or indepth == 'Yes'):
	dirdepth = get_html('https://raw.githubusercontent.com/rbsec/dnscan/master/subdomains-100.txt')
	dirdepth = dirdepth.split()
	for dirs in dirdepth:
		commonsubs.append(dirs)

if(subdoms == 'y' or  subdoms == 'Y' or subdoms == 'yes' or subdoms == 'Yes'):
	for subs in commonsubs:
		if(get_html(webpage+"/"+subs) != "Failed connection" or get_html(webpage+"/"+subs).count("404") < 1):
			htmlpage = htmlpage + get_html(webpage+"/"+subs)
			print(webpage+"/"+subs)

morewebsites = input("Do you wanna add another website. Y/n?  ")
while morewebsites == 'y' or morewebsites == 'yes' or morewebsites == 'Y' or morewebsites == 'Yes':
	webpage2 = input('Enter website to grab info from. Example: http://company.com or http://socialmedia.com/personalprofile ')
	if (webpage2.count("http")==0):
		webpage2 = 'https://'+webpage2
	htmlpage = htmlpage + get_html(webpage2)
	print(webpage2 + " info found an added")
	morewebsites = input("Do you wanna add another website. Y/n?  ")


suffixes = ["2020", "2021", "2023","123","2022","1234","xxx", "1", "$","qwerty","66","1122",'321','420','69','one','One','admin','7','77',
'1995','58','1996','1987','1994','1988','1985','1983','1992','1982','1984','1986','2000','987','989','000','98','96','00','87','76','79','99','75','64','11']
connectors = ["-", ".","_","/","!","@",'#','$']

datelist = htmlpage.split()
#Will find dates in the text
for dates in datelist:
    if(len(dates) > 2 and htmlpage.count(dates) > 1):
        if(dates[2]=="/"):
            daymonth = dates[0:5]
            suffixes.append(daymonth.replace("/", ""))
        if(dates[2]=="/" and len(dates) > 6 and dates[5] =="/"):
            suffixes.append(dates[:10].replace("/", ""))
            justyear = dates[5:10]
            suffixes.append(justyear.replace("/", ""))
            if(len(justyear) > 4):
                justyear = justyear[3:5]
                suffixes.append(justyear.replace("/", ""))
        if(dates[2]=="-"):
            daymonth = dates[0:5]
            suffixes.append(daymonth.replace("-", ""))
        if(dates[2]=="-" and len(dates) > 6 and dates[5]=="-" ):
            suffixes.append(dates[:10].replace("-", ""))
            justyear = dates[5:10]
            suffixes.append(justyear.replace("-", ""))
            if(len(justyear) > 4):
                justyear = justyear[3:5]
                suffixes.append(justyear.replace("-", ""))

#removing duplicates in suffixes
suffixes = [*set(suffixes)]

#filtering unnecesary common words
unnecessary = ['error']

maybetoocommon = get_html('https://gist.githubusercontent.com/deekayen/4148741/raw/98d35708fa344717d8eee15d11987de6c8e26d7d/1-1000.txt')
maybetoocommon = maybetoocommon.lower().split()

for toocommon in maybetoocommon:
	unnecessary.append(' '+toocommon+' ')

for words in unnecessary:
	htmlpage = htmlpage.lower().replace(words, " ")


wordlist = htmlpage.split()
common = []
for words in wordlist:
    for duplicates in common:
        if(duplicates == words):
            common.remove(duplicates)
    if(htmlpage.count(words) >= 3 and len(words) >= 4):
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
    if(htmlpage.count(words) <= 2 and len(words) >= 4 and len(words) <= 14):
        leastcommon.append(words)
        wordlist.remove(words)
    else:
        wordlist.remove(words)
with open("leastcommonwords.txt","w") as file:
	for words in leastcommon:
	    file.write(words+"\n")
	print("leastcommonwords.txt created, added "+ str(len(leastcommon))+ " least common words")
	    


shufflingoptions = input("""What you wanna do now?
1-Add capitalization and suffixes to words. Example: blah into blah2020, Blah123.
2-Randomly combine common and least common words found. Example: words blah and bleh into blah@bleh or Blah.Bleh
3-Do both
""")

if(int(shufflingoptions) == 1 or int(shufflingoptions) == 3):
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
		print("added suffixes to wordlist and saved as finalwordlist.txt")
	with open("finalwordlist.txt","r") as file:
		print(str(len(file.readlines())) + " words")
		
	with open("finalwithleastcommon.txt","w") as file:
		for words in leastcommon:
			file.write(words+"\n")
			file.write(words.capitalize()+"\n")
			for suffix in suffixes:
				file.write(words+suffix+"\n")
				file.write(words.capitalize()+suffix+"\n")
				for connector in connectors:
					file.write(words+connector+suffix+"\n")
					file.write(words.capitalize()+connector+suffix+"\n")
		print("added suffixes to least common wordlist and saved as finalwithleastcommon.txt")
	with open("finalwithleastcommon.txt","r") as file:
		print(str(len(file.readlines())) + " words")
if(int(shufflingoptions) == 2 or int(shufflingoptions) == 3):
	connectors.append("")
	with open("randomcombinations.txt","w") as file:
		for i in range(0, 2500):	
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
				
		
