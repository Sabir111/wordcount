from django.http import HttpResponse
from django.shortcuts import render
import operator


def homepage(request):
    return render(request, 'home.html',{'name':'Hi there...i am sabir'})

def count(request):
    data = request.GET['fulltextarea']
    wordlist= data.split()
    list_length = len(wordlist)

    worddictionary = {}

    for word in wordlist:
        if word in worddictionary:
            worddictionary[word] +=1
        else:
            worddictionary[word] =1

    sorted_list=sorted(worddictionary.items(),key = operator.itemgetter(1), reverse=True)
    return render(request, 'count.html',{'fulltext':data,'words':list_length,'worddictionary':sorted_list})

def about(request):
    return render(request, 'about.html')
