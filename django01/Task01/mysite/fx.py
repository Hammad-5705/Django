from django.http import HttpResponse
from django.shortcuts import render

from django.shortcuts import render  

def Fx(request): 
    return render(request, "home.html")

def analyze(request):
    djtext= request.GET.get("txt","Text Didn\'t found")
    rem= request.GET.get("rempunc","off")

    if rem=="on":
    
        punc = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''  
        result = []  

        for char in djtext:  
            if char not in punc:  
                result.append(char)  
        
        final_result = ''.join(result)   
        data = {"text": djtext, "solved": final_result}  


        return render(request,"analyze.html",data)
    
    else:
        return HttpResponse("ERROR")












def punc_remove(request):
    djtext = request.GET.get("txt", "Text Didn\'t Found")
    print(djtext)
    
    string = """
        <h2>Punctuation Remove</h2>
        <a href="http://127.0.0.1:8000/">Click here to go home</a>
    """
    
    return HttpResponse(string)

def Cap_first(request):
   string=HttpResponse('''
    Capatilize First <br>
                       <a href="http://127.0.0.1:8000/">Click here to go home <a/>
    ''')
   
   return string


def Newline_remover(request):
   string=HttpResponse('''
    Remove New Line  <br>
                       <a href="http://127.0.0.1:8000/">Click here to go home <a/>
    ''')
   
   return string

def Space_remover(request):
   string=HttpResponse('''
    Remove Space  <br>
                       <a href="http://127.0.0.1:8000/">Click here to go home <a/>
    ''')

   return string

def character_counter(request):
   string=HttpResponse('''
    Count Characters  <br>
                       <a href="http://127.0.0.1:8000/">Click here to go home <a/>
    ''')