# Pot of Words (Personalized password lists)
The forbidden spell to draw more passwords!

![PotofWords](https://github.com/raskolnikov90/potofwords.py/assets/44821234/16d53a7f-80ba-4085-ad6e-7504bd343388)

  Usually when pentesting using bruteforce attacks we use common password lists like rockyou.txt or SecLists, but if brute force attacks fail using those lists it may be easy to assume the target is using secure passwords but many times it is possible to guess their passwords by manualy doing deep reconnaissance and guessing some possible passwords out of it. What if we were able to automatize this deep recoinassance phase to get possible passwords? potofwords.py does this by grabbing common words in a webpage url you provide, creating common words lists and creating a password list by adding common special characters and suffixes to our findings(For example to the word shingeki will be added stuff and become Shingeki/123 making it more likely we may guess a possible password that uses that word)

Update 6/23/2023: Pot of words also now creates least common words list, added the option of randomly combine common and least common words (Example: sonic and mario will be randomly combined into sonicmario or Mario.Sonic)

Update 6/25/2023: Now with the ability of more in depth directory fuzzing and the option to add more websites, better filtering of too common words that do not give interesting password lists, added more common suffixes (Those where got doing statistical analisys to public common password wordlist to see the most common suffixes) 

Requires BeautifulSoup module, run the following command on your terminal or python interpreter:

```
pip install beautifulsoup4
pip install python-dateutil
```

Using Pot of words examples:
![image](https://github.com/raskolnikov90/potofwords.py/assets/44821234/37868421-d890-4742-8f0a-7ad9fca4ab0e)

![image](https://github.com/raskolnikov90/potofwords.py/assets/44821234/9f19915c-f5ac-4aa5-9742-94edbad1c872)



