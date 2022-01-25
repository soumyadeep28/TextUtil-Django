#self made file
from string import punctuation
from django.http import HttpResponse, response
from django.shortcuts import render


def index(request) :
    
    response = render(request , 'index.html'  )
    return response

def analyze(request):
    text = request.GET.get('mytext' ,'blank')
    punchuationoption = request.GET.get('removepunc' , 'off')
    allcapsoption = request.GET.get('allcaps' , 'off')
    allsmalloption = request.GET.get('allsmall' , 'off')
    removelineoption = request.GET.get('removeline' , 'off')
    removespaceoption = request.GET.get('removespace' , 'off')
    charcountoption = request.GET.get('charcount' , 'off')

    if punchuationoption == 'on' :
        allpunch = '''!{},|\<>?/,.'-+[];'''  
        purpose = "Remove Punchuation"
        analyzed = ""
        for charcter  in text :
            if charcter not in allpunch :
                analyzed += charcter 
        
        analyzeddata = analyzed 
        context ={
            "purpose" : purpose ,
            "rawdata" : text,
            "analyzed_text" : analyzeddata
        }
    elif allcapsoption == 'on':
        analyzeddata = text.upper()
        purpose = 'All capital'
        context ={
            "purpose" : purpose ,
            "rawdata" : text,
            "analyzed_text" : analyzeddata
        }
    elif allsmalloption == 'on':
        analyzeddata = text.lower()
        purpose = 'All capital'
        context ={
            "purpose" : purpose ,
            "rawdata" : text,
            "analyzed_text" : analyzeddata
        }
    elif removelineoption == 'on' :
        purpose = "Remove New Line"
        analyzed = ""
        for charcter  in text :
            if charcter != "\n" :
                analyzed += charcter 
        
        analyzeddata = analyzed 
        context ={
            "purpose" : purpose ,
            "rawdata" : text,
            "analyzed_text" : analyzeddata
        }
    elif removespaceoption == 'on' :
        purpose = "Remove Extra space"
        analyzed = ""
        for index ,charcter  in enumerate(text) :
            if charcter == " " and text[index+1] == " ":
                pass
            else:
                analyzed += charcter 
        
        analyzeddata = analyzed 
        context ={
            "purpose" : purpose ,
            "rawdata" : text,
            "analyzed_text" : analyzeddata
        }
    elif charcountoption == 'on' :
        purpose = "char counter Not Length counter"
        count =0
        for char in text :
            if char == " " or char == "\n":
                print(char)
                count += 1 
        count = len(text) - count
        context ={
            "purpose" : purpose ,
            "rawdata" : text,
            "analyzed_text" : count
        }
    else:
        return HttpResponse("<h2> GO back you have entered wrong</h2> <br> <a href='/'> Press to go back </a>")

    response = render(request , 'analyze.html' , context )
    return response




def readfile(request):
    with open('request.txt' , 'r') as file :
        text = file.read()
    response = HttpResponse(text)
    return response

def task1 (resposne) :
    response = HttpResponse("<h1> Task 1 by code with harry </h1> <hr> <a href='http://facebook.com'>Facebookurl </a>")
    return response