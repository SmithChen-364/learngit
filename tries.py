#tries for search words
#tries类
class tries:
    #根节点root
    root=None
    #添加方法
    def add(self,word):
        #如果没有根节点，则将第一个单词的第一个字符添加为根节点，
        #如果有根节点，从第一个字符开始添加节点
        if(not self.root):
            self.root=self.add_element(word,0,self.root)
            self.root.parentNode=self.triesNode("root")
        else:
            self.add_element(word,0,self.root)
    def addList(self,wordlist):
        if(len(wordlist)==0):
            print("invalid list you input")
        else:
            for item in wordlist:
                self.add(item)
    def add_element(self,word,index,current):
        if(current==None):
            current=self.triesNode(word[index])
        if(word[index]<current.getChar()):
            current.leftNode=self.add_element(word,index,current.leftNode)
            current.leftNode.parentNode=current
        elif(word[index]>current.getChar()):  
            current.rightNode=self.add_element(word,index,current.rightNode)
            current.rightNode.parentNode=current
        else:
            if(index==len(word)-1):
                current.setFreq(current.getFreq()+1)
                return current
            current.middleNode=self.add_element(word,index+1,current.middleNode)
            current.middleNode.parentNode=current
        return current        
    def delete(self,word):
        isExist=self.search(word)
        if(isExist):
            isExist.setFreq(0)
    def printAll(self):
        self.printAllNode(self.root,[])
    def printPrefix(self,word):
       self.add(word)
       prefix=self.search(word)
       if(prefix.getFreq()>1):
           print(word)
       self.printAllNode(prefix.middleNode,list(word[:-1]))
       prefix.setFreq(prefix.getFreq()-1)
    def printAllNode(self,_currentNode,storage):
        if(_currentNode==None):
            return 
        if(_currentNode.parentNode.middleNode is _currentNode):
            storage.append(_currentNode.parentNode.getChar())
        if(_currentNode.getFreq()!=0):
            storage.append(_currentNode.getChar())
            print("".join(storage))
            storage.pop()
        self.printAllNode(_currentNode.leftNode,storage)
        self.printAllNode(_currentNode.middleNode,storage)
        self.printAllNode(_currentNode.rightNode,storage)
        if(_currentNode.parentNode.middleNode is _currentNode):
            storage.pop()
        
    def search(self,word):
        i=0
        currentNode=self.root
        parentNode=None
        Freq=0
        while(i<len(word)):
            if(currentNode==None):
                break
            if(word[i]>currentNode.getChar()):
                currentNode=currentNode.rightNode
            elif(word[i]<currentNode.getChar()):
                currentNode=currentNode.leftNode
            else:
                Freq=currentNode.getFreq()
                parentNode=currentNode
                currentNode=currentNode.middleNode
                i=i+1
        if(i==len(word) and (not Freq==0)):
            print(word+" is in it ")
            print("%d times recorded!"%Freq)
            return parentNode
        else:
            print(word+" is not in it")
            return None


    class triesNode:
        leftNode=rightNode=middleNode=None
        char=None
        parentNode=None
        freq=0
        def __init__(self,char):
            self.char=char
        def setFreq(self,freq):
            self.freq=freq
        def getFreq(self):
            return self.freq
        def getChar(self):
            return self.char



person=tries()
person.addList(["shell","she","shelter","salad","sho","sh"])
print("printALL")
person.printAll()
print("printPrefix")
person.printPrefix("she")
