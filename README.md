# Pot of Words (Personalized password lists)
The forbidden spell to draw more passwords!

![PotofWords1](https://github.com/raskolnikov90/potofwords.py/assets/44821234/0183ae79-e4b4-4056-8787-93705b837917)

  Usually when pentesting using bruteforce attacks we use common password lists like rockyou.txt or SecLists, but if brute force attacks fail using those lists it may be easy to assume the target is using secure passwords but many times it is possible to guess their passwords by manualy doing deep reconnaissance and guessing some possible passwords out of it. What if we were able to automatize this deep recoinassance phase to get possible passwords? potofwords.py does this by grabbing common words in a webpage url you provide, creating common words lists and creating a password list by adding common special characters and suffixes to our findings(For example to the word shingeki will be added stuff and become Shingeki/123 making it more likely we may guess a possible password that uses that word)

MAJOR UPDATE 8/6/2023:
-Pot of words will find most and least common words and add prefixes and suffixes, It will also add rules like variations of leetspeak, reverse the word and shuffle letters
-It will also create a passphrase list that combine 2 words and 3 words using phrases from the website you provide and also add them prefixes, suffixes and rules
-The suffix/prefix list was fully updated and expanded using the results from my analysis of complex passwords that can be found here: 
https://github.com/raskolnikov90/ComplexPassAnalysisAndWordlists
-It now incorporates the datefinder module in order to find dates in the websites you provide and use them as prefix and suffix

Requires BeautifulSoup, dateutil, datefinder and requests module, run the following command on your terminal or python interpreter:

```
pip install beautifulsoup4
pip install python-dateutil
pip install requests
pip install datefinder
```

Using Pot of words examples:
![PotofWords2](https://github.com/raskolnikov90/potofwords.py/assets/44821234/3ef5667c-935a-45e2-83a2-d4d3e8a49297)


![potofwordsample](https://github.com/raskolnikov90/potofwords.py/assets/44821234/86f2307e-6c05-4737-9086-5a4161897c07)


