class wordfrq:
    
    dic_str={}
    
    def __init__(self, str_text):
        self.str_text = str_text
        sp_string= self.str_text.split( )
               
        for i in sp_string:
            if i not in wordfrq.dic_str:
                wordfrq.dic_str[i]=1
            else:
                wordfrq.dic_str[i]+=1
    
    def maximum_wrd(self):
        for i in range(3): 
            j=i+1
            print "Max_%d" % j,  ": '", max(wordfrq.dic_str, key=wordfrq.dic_str.get), "' , frequency is ", max(wordfrq.dic_str.values())
            wordfrq.dic_str.pop(max(wordfrq.dic_str, key=wordfrq.dic_str.get))
   
             
dic_list=wordfrq("I am a machine learning engineer")
wordfrq("I am an engineer")
wordfrq("I have engineer")
wordfrq("Do machine learning engineer")

dic_list.maximum_wrd()
