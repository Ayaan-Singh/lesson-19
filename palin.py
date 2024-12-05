l1=[]
print()
def match (words):
    ctr=0
    lst = []
    for word in words:
        if len(word) > 1 and word [0] == word[-1]:
         ctr += 1
        lst.append(word)
    print ("list of words with first and last charecter same \n",lst) 
    return ctr
count = match  (["mom","cat","dog","1221","1212", "tank", "teapot" ,"tit","tat"])
print ("num of words with first and last letters same",count)

