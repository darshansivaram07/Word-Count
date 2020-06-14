from django.shortcuts import render
import operator

def homepage(request):
  return render(request,'home.html')

def countspage(request):
  fulltext=request.GET['fulltext']
  wordlist=fulltext.split()
  worddictionary={}
  for word in wordlist:
    if word in worddictionary:
      worddictionary[word] +=1
    else:
      worddictionary[word]=1
  sortedwords=sorted(worddictionary.items(),key=operator.itemgetter(1),reverse=True)    
  return render(request,'count.html',{'fulltext':fulltext,'wordlist':len(wordlist),'worddictionary':sortedwords})

def aboutpage(request):
  return render(request,'about.html')