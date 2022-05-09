import sys
sys.setrecursionlimit(10**6)

from collections import deque, defaultdict

class Node(object):
    def __init__(self, key):
        self.key = key
        self.is_terminal = False
        self.child_num = 0
        self.children = {}
        
    def search(self, string):
        node = self
        for char in string:
            if char == '?':
                return node.child_num
            else:
                if char in node.children:
                    node = node.children[char]
                else:
                    return 0
                    
        if node.is_terminal:
            return 1
        return 0
            
    def set_child_num(self):
        node = self
        if node.is_terminal:
            return 1
        
        num = 0
        for child in node.children:
            num += node.children[child].set_child_num()
        node.child_num = num
        return node.child_num

class Trie(object):
    def __init__(self):
        self.head = Node(None)
    
    def insert(self, string):
        node = self.head
        for char in string:
            if char not in node.children:
            	node.children[char] = Node(char)
            node = node.children[char]
        node.is_terminal = True
    
    def search(self, string):
        return self.head.search(string)
    
    def set_child_num(self):
        self.head.set_child_num()
        
    def traverse(self, node, level):
        ret = 0
        if level == 1:
            for child in node.children:
                c_node = node.children[child]
                if c_node.is_terminal:
                    ret += 1
                    
            return ret
                
        for child in node.children:
            c_node = node.children[child]
            ret += self.traverse(c_node, level-1)
            
        return ret

def solution(words, queries):
    root = dict()
    rev_root = dict()
    
    for word in words:
        l = len(word)
        
        if l not in root:
            root[l] = Trie()
            rev_root[l] = Trie()
            
        root[l].insert(word)
        rev_root[l].insert(word[::-1])
    
    for num in root:
        root[num].set_child_num()
    
    for num in rev_root:
        rev_root[num].set_child_num()
        
    answer = []
    for query in queries:
        l = len(query)
        if l not in root:
            answer.append(0)
        elif query[0] == '?':
            query = query[::-1]
            answer.append(rev_root[l].search(query))
        else:
            answer.append(root[l].search(query))
                      
    return answer