from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings
from openai import OpenAI

client = OpenAI(api_key=settings.OPENAI_APIKEY)
# Create your views here.


def ask_openai(message):
    response = client.completions.create(
        model="tts-1",
        prompt=message,
    )
    print(response)
    answer = response.choices[0].text.strip()
    
    return answer


def chatbot(request):
    if request.method == "POST":
        message = request.POST.get("message")
        response = ask_openai(message)
        return JsonResponse({"message": message, "response": response})
    return render(request, "chatbot.html")
