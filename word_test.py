sample_memo = '''
Milt, we're gonna need to go ahead and move you downstairs into storage B. We have some new people coming in, and we need all the space we can get. So if you could just go ahead and pack up your stuff and move it down there, that would be terrific, OK?
Oh, and remember: next Friday... is Hawaiian shirt day. So, you know, if you want to, go ahead and wear a Hawaiian shirt and jeans.
Oh, oh, and I almost forgot. Ahh, I'm also gonna need you to go ahead and come in on Sunday, too...
Hello Peter, whats happening? Ummm, I'm gonna need you to go ahead and come in tomorrow. So if you could be here around 9 that would be great, mmmk... oh oh! and I almost forgot ahh, I'm also gonna need you to go ahead and come in on Sunday too, kay. We ahh lost some people this week and ah, we sorta need to play catch up.
'''
import re
re.sub('[^a-z0-9 ]+',' ', sample_memo.lower()).strip()

data=sample_memo.split()
dic={}
word='ahead'
distance=2

if distance > 0:

    for i in range(len(data)):
        if word == data[i]:
            if data[i+1] not in dic:
                dic[data[i+1]] = 1
            else:
                dic[data[i+1]] +=1
                
    total_number=sum(dic.values()) #sum total number appear
   
    for k in dic.keys(): #change number to percentage
        dic[k]= round( dic[k]*1.0 / total_number, 2)
   
# TODO: Repeat the above process--for each distance beyond 1, evaluate the words that
# might come after each word, and combine them weighting by relative probability
# into an estimate of what might appear next.

if distance > 1:
    
    dic_list=[]
    
    for second_wrd in dic.keys():
        
        dic2={}
        
        for i in range(len(data)):
            if second_wrd == data[i]:
                if data[i+1] not in dic2:
                    dic2[data[i+1]] = 1
                else:
                    dic2[data[i+1]] +=1
                    
        total_number=sum(dic2.values()) #sum total number appear
   
        for k in dic2.keys(): #change number to percentage
            dic2[k]= round( (dic2[k]*1.0 / total_number) * dic[second_wrd], 2)
            print dic2[k]
            
        dic_list.append(dic2)

    final_dic={}
    maximum_pr=0
    #find the most likelihood word
    for alist in dic_list:
        for key_value in alist.keys():
            
            if key_value not in final_dic: 
                final_dic[key_value]=alist[key_value]
                if maximum_pr < final_dic[key_value]:
                    maximum_pr = final_dic[key_value]
                    res= key_value
            else:
                final_dic[key_value] += alist[key_value]
                if maximum_pr < final_dic[key_value]:
                    maximum_pr = final_dic[key_value]
                    res= key_value
        
            
        

print res
