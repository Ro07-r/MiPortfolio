from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail

def formularioContacto(request):
    return render(request, 'formularioContacto.html')

#def portfolio(request):
    #return render(request, 'portfolio')

def contactar(request):
    if request.method == "POST":
        asunto = request.POST["txtAsunto"]        
        mensaje = request.POST["txtMensaje"] + " / Mail: " + request.POST["txtEmail"] # Mail para poder contactar
        email_desde = settings.EMAIL_HOST_USER
        email_para = ["lotierzorosalia@gmail.com"]
        send_mail(asunto, mensaje, email_desde, email_para, fail_silently=False)
        return render(request, "formularioContacto.html")
    else:
        return render(request, 'formularioContacto.html')