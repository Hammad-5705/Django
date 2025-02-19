from django.http import HttpResponse
from django.shortcuts import render
 

def Fx(request): 
    return render(request, "boot.html")


from django.http import HttpResponse  
from django.shortcuts import render  

def analyze(request):  
    djtext = request.POST.get("txt", "Text Didn't found")  
    final_result = djtext  
    rempunc = request.POST.get("rempunc", "off")  
    Capatlize = request.POST.get("Capatlize", "off")  
    Newline_remover = request.POST.get("Newline_remover", "off")  
    Space_remover = request.POST.get("Space_remover", "off")  
    Char_counter = request.POST.get("Char_counter", "off")  

    dct = {"rempunc": rempunc, "Capatlize": Capatlize, "Newline_remover": Newline_remover, "Space_remover": Space_remover}  
    func = {"rempunc": frempunc, "Capatlize": fCapatlize, "Newline_remover": fNewline_remover, "Space_remover": fSpace_remover}  

    raw_purpose = []  
    cntr = 0  
     
    for i, j in dct.items():  
        if j == "on":  
            final_result = func[i](final_result)  
            raw_purpose.append(i)  
            cntr += 1  
    

    if cntr == 0 and not (Char_counter == "on"):  
        data = {"Purpose": "Selected Nothing", "solved": f"404 Error"} 
        return render(request, "analyze.html",data)  

    purpose = "\n".join(raw_purpose)

    if Char_counter == "on":  
        no = fChar_counter(final_result)
        purpose=f"{purpose} Count Characters"
        data = {"Purpose": purpose, "solved": f"{final_result}", "no": f"Total Characters {no}"}  
    else:  
        data = {"Purpose": purpose, "solved": final_result}  

    return render(request, "analyze.html", data)
            

def frempunc(djtext):
    fnal_result=""
    punc = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''  
    result = []  

    for char in djtext:  
        if char not in punc:  
            result.append(char)  
        
    fnal_result = ''.join(result)     
    return str(fnal_result)
    

def fCapatlize(djtext):
    fnal_result=""
    for char in djtext:
        fnal_result= fnal_result + char.title()
                


    return str(fnal_result)
        

def fNewline_remover(djtext):    
    lines = djtext.splitlines()  
    result = [line for line in lines if line.strip()]
    return "\n".join(result)




def fSpace_remover(djtext):
    fnal_result = ""  

    for index, char in enumerate(djtext):
        if (char == " " and index < len(djtext) - 1 and djtext[index + 1] == " "):  
            pass
        else:
            fnal_result += char

    return str(fnal_result)



def fChar_counter(djtext):
    fnal_result=len(djtext)
    return f"{fnal_result}"












# def Analyze(request):
#     final_result=""
#     djtext= request.GET.get("txt","Text Didn\'t found")
#     rempunc= request.GET.get("rempunc","off")
#     Capatlize= request.GET.get("Capatlize","off")
#     Newline_remover=request.GET.get("Newline_remover","off")
#     Space_remover=request.GET.get("Space_remover","off")
#     Char_counter=request.GET.get("Char_counter","off")



#     if rempunc=="on":
    
#         punc = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''  
#         result = []  

#         for char in djtext:  
#             if char not in punc:  
#                 result.append(char)  
        
#         final_result = ''.join(result)   
#         data = {"Purpose": "Remove Punctuations", "solved": final_result}  


#         return render(request,"analyze.html",data)
    

#     elif Capatlize=="on":

#         for char in djtext:
#             final_result= final_result + char.title()
        
#         data = {"Purpose": "Capatilize", "solved": final_result} 
#         return render(request,"analyze.html",data)
    

#     elif Newline_remover=="on":

#         for index , char in enumerate(djtext):
#             if not(djtext[index]=="\n" and djtext[index+1]=="\n"):
#                final_result= final_result + char
                

#         data = {"Purpose": "Remove Newlines", "solved": final_result} 
#         return render(request,"analyze.html",data)




#     elif Space_remover=="on":
#         final_result = ""  

#         for index, char in enumerate(djtext):
#             if (char == " " and index < len(djtext) - 1 and djtext[index + 1] == " "):  
#                 pass
#             else:
#                 final_result += char

#         data = {"Purpose": "Remove Extra Spaces", "solved": final_result} 
        
#         return render(request,"analyze.html",data)



#     elif Char_counter=="on":
#         final_result=len(djtext)
#         data = {"Purpose": "Count Characters", "solved": final_result} 
#         return render(request,"analyze.html",data)


#     else:
#         return HttpResponse("ERROR")












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