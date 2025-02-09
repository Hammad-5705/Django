from django.http import HttpResponse

def Fx(request):
    return HttpResponse('''Facebook: <a href="https://www.fb.com">Facebook </a><br>
                        Whatsapp:  <a href="https://www.Whatsapp.com">Whatsapp </a><br>
                        Youtube:   <a href="https://www.Youtube.com">Youtube </a><br>''')
                    