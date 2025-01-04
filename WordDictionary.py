class TrieNode: 
    def __init__(self):
        self.children = {}
        self.endofWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word: 
            if c not in cur.children: 
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endofWord = True

    def search(self, word: str) -> bool:
        #A Recursive function to go through each element of the list and to 
        #see if character is "." or not and then accordingly call the recursive call. 
        def dfs(j,root):
            #Starting point of the function where cur is the root 
            cur = root
            #Going through each element of the list from j to the end of the word
            for i in range(j,len(word)):
                #Setting it to the current character 
                c = word[i]
                #Checking if the character is a ".". If it is, it will then look at values, which is 
                #And then call recursively to check is it matches the pattern or not. If the recursive
                #function always returns a True, we can say that it was able to find a match, else False
                if c == ".": 
                    for child in cur.children.values(): 
                        if dfs(i+1, child):
                            return True
                    return False
                #Else function if the character is a a normal character and not a "."
                else: 
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]
            return cur.endofWord
        
        return dfs(0,self.root)
