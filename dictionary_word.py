string="I am a machine learning engineer"

sp_string=string.split( )

dic_str={}

for i in range(len(sp_string)):
    dic_str[sp_string[i]]=0

for st_fact in sp_string: 
    if st_fact in dic_str:
        dic_str[st_fact]+=1
               
maximum_key = max(dic_str, key=dic_str.get)
print maximum_key    

maximum_value = max(dic_str.values())  
print maximum_value   

#pop dictionary
dic_str.pop(maximum_key)


#add key and value
dic_str.update({'k':1})
           
two_array=[]

for i in range(3):
    two_array[i]=[]
    for j in range (5):
        two_array[i].append(j)       
