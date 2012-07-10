
import re
import sys

def pychaos(filename):
    f = open(filename,'rU')
    text = f.read()
    f.close()
    d = {}
    dnew = {}
    array = range(101)
    del array[0]
    listran = re.findall(r'[\w.]+ war',text)
    i = 1        
    for ele in listran:
        d[i] = ele
        i = i + 1
    
    newlist = []
    years = []
    b = ['war','killed','virus','disaster','riot','destroy','damage','devastate','death','earthquake','tsunami','deadly','catastrophe','Earthquake','War','Tsunami','Hurricane','Cyclone']
    for ele in b:
        found = re.search(ele,text)
        if found:
            nsearchUT1 = re.search(r'..+ %s ..+'%(ele),text)
            nsearchUT2 = re.search(r'%s ..+'%(ele),text)
            nsearchUT3 = re.search(r' ..+ %s'%(ele),text)
            if nsearchUT1:
                newlist.append(nsearchUT1.group())
            elif nsearchUT2:
                newlist.append(nsearchUT2.group())
            elif nsearchUT3:
                newlist.append(nsearchUT3.group())
    
    
    for ele in newlist:
        foundnow = re.search(r'\d\d\d\d',ele)
        if foundnow:
            if not foundnow.group() == '.':
                years.append(foundnow.group())

    years = sorted(years)
    nwyears = []
    j=0
    for j in range(len(years)):
        if not j == 15:
            if not years[j] == years[j+1]:
                nwyears.append(years[j])
            else:
                continue
        else:
            nwyears.append(years[15])
               
                
    print "The Years of Calamities according to the data from 1980 onwards"
    for ele in nwyears:
        print ele
    
    return

     
    
def main():
    pychaos(sys.argv[1])

if __name__ == '__main__':
    main()
      
