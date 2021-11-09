from django.shortcuts import render
from gtts import gTTS
import os
def index(request):
    return render(request , "index.html" , {})


def converted(request):
    text = request.POST.get('text')
    myvoice = gTTS(text= text , lang= "en" , slow = True)
    voice = myvoice.save("audio\\voice .mp3")
    return render(request,"converted.html",{})