from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
    return render(request, "home.html")

def aboutme(request):
    return render(request, "aboutme")

def count(request):
    fulltext = request.GET["allofthetext"]

    wordlist = fulltext.split()
    wordcount = len(wordlist)

    dictionary = {}

    for x in wordlist:
        if x in dictionary:
            dictionary[x]+=1
        else:
            dictionary[x]=1


    orgdic = sorted(dictionary.items(), key=operator.itemgetter(1), reverse= True)


    return render(request, "count.html", {"fulltext":fulltext, "count":wordcount, "dictionary":orgdic})
