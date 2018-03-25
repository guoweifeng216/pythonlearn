def main():
    listWords=formListWords("Greeting.txt")
    freq=createFrequencyDictionary(listWords)
    displayWordCount(listWords,freq)
    dispalyMostCommonWords(freq)

def formListWords(filename):
    infile=open(filename)
    originalLine=infile.readline().lower()
    line=""
    for ch in originalLine:
        if ('a'<=ch<='z') or (ch==""):
            line +=ch
    lisWords=line.split()
    return lisWords

def createFrequencyDictionary(listWords):
    freq={}
    for word in listWords:
        freq[word]=0
    for word in listWords:
        freq[word]=freq[word]+1
    return freq

def displayWordCount(listWords,freq):
    print "The Greeting Address contains %d words"%len(listWords)
    print "The Greeting Address contains %d different words" % len(freq)

def dispalyMostCommonWords(freq):
    print "The most common words and theier frequencies are:"
    listMostCommonWords=[]
    for word in freq.keys():
        if freq[word]>=6:
            listMostCommonWords.append((word,freq[word]))
    listMostCommonWords.sort(key=lambda x:x[1],reverse=True)
    for item in listMostCommonWords:
        print ""+ item[0]+':'+item[1]
main()