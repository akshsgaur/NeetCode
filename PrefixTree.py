'''

Implement Trie (Prefix Tree)
Solved 
A prefix tree (also known as a trie) is a tree data structure used to efficiently store and retrieve keys in a set of strings. Some applications of this data structure include auto-complete and spell checker systems.

Implement the PrefixTree class:

PrefixTree() Initializes the prefix tree object.
void insert(String word) Inserts the string word into the prefix tree.
boolean search(String word) Returns true if the string word is in the prefix tree (i.e., was inserted before), and false otherwise.
boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.
Example 1:

Input: 
["Trie", "insert", "dog", "search", "dog", "search", "do", "startsWith", "do", "insert", "do", "search", "do"]

Output:
[null, null, true, false, true, null, true]

Explanation:
PrefixTree prefixTree = new PrefixTree();
prefixTree.insert("dog");
prefixTree.search("dog");    // return true
prefixTree.search("do");     // return false
prefixTree.startsWith("do"); // return true
prefixTree.insert("do");
prefixTree.search("do");     // return true


'''

#Creating a TrieNode to store a node's children and 
#a EndOfWord which will be False to see if it's a end of the word or not. 
#For example the e in Apple
class TrieNode():
    def __init__(self):
        self.children = {} 
        self.endOfWord = False



class PrefixTree:

    #Initalizing a Prefix Tree: 
    #The root of the Tree will be a TrieNode
    def __init__(self):
        self.root = TrieNode()
        
    # An Insert Function: Start with the self.root 
    # Go through each character in the word
    # If the word is not in the cur.children, add it to the cur.children by creating a trieNode
    # Once the TrieNode has been created, move on to the next letter by cur = cur.children[c]
    # Once the word has been inserted, mark the last letter as EndOfPoint
    def insert(self, word: str) -> None:
        cur = self.root
        for c in word: 
            if c not in cur.children: 
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfWord = True

    # Search Function: Start with the root 
    # Go through each letter of the word and check: 
    # if c is not in cur.children: 
    # If not, it is False
    # If it is, move on to the next character in the hashmap by cur = cur.children[c]
    # Return true only if cur is the endOfWord
    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            if c not in cur.children: 
                return False
            cur = cur.children[c]

        return cur.endOfWord 

        
    # Start with the root node
    # Go through each word in Prefix
    # if c is in not in cur.children: Return False
    # if it is, move on to the cur.children[c]
    # Return True if for loop reaches the end of the word. 
    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix: 
            if c not in cur.children: 
                return False
            
            cur = cur.children[c]
        
        return True
        