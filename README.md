# Pot of Words (Personalized password lists)
The forbidden spell to draw more passwords!

  Usually when pentesting using bruteforce attacks we use common password lists like rockyou.txt or SecLists, but if brute force attacks fail using those lists it may be easy to assume the target is using secure passwords but many times it is possible to guess their passwords by manualy doing deep reconnaissance and guessing some possible passwords out of it. What if we were able to automatize this deep recoinassance phase to get possible passwords? potofwords.py does this by grabbing common words in a webpage url you provide, creating common words lists and creating a password list by adding common special characters and suffixes to our findings(For example to the word shingeki will be added stuff and become Shingeki/123 making it more likely we may guess a possible password that uses that word)

Requires BeautifulSoup module, run the following command on your terminal or python interpreter:

pip install beautifulsoup4
