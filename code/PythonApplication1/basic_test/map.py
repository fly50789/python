from functools import reduce 
def main():
    print("start")
    listitem=[1,2,3,4,5,6,7] 
    #without map
    print(listitem)
    templist=[]
    for item in listitem:
        templist.append(item**2)
    print(templist)
    #map
    templist2=list(map(lambda x:x*2,listitem))
    print(templist2)
    #filter
    templist3=list(filter(lambda x:x%2==0,listitem))
    print(templist3)

    #without reduce
    sum=0
    for item in listitem:
        sum+=item
    print(sum)
    #withreduce
    sum1=reduce(lambda x,y:x+y,listitem)
    print(sum1)

if __name__=='__main__':main()
