from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def analyze(request):
    # Get the text
    inputted_text = request.POST.get('text', 'default')

    # Check checkbox values
    remove_punctuation = request.POST.get('remove_punctuation', 'off')
    uppercase = request.POST.get('uppercase', 'off')
    newline_remover = request.POST.get('newline_remover', 'off')
    extra_space_remover = request.POST.get('extra_space_remover', 'off')
    number_remover = request.POST.get('number_remover', 'off')
    params = {}

    # Analyze the text
    if remove_punctuation == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in inputted_text:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': "Remove Punctuations", 'analyzed_text': analyzed}
        inputted_text = analyzed

    if uppercase == "on":
        analyzed = inputted_text.upper()
        params = {'purpose': "Change to Uppercase", 'analyzed_text': analyzed}
        inputted_text = analyzed

    if newline_remover == "on":
        analyzed = ""
        for char in inputted_text:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        params = {'purpose': "Remove Newline", 'analyzed_text': analyzed}
        inputted_text = analyzed

    if extra_space_remover == "on":
        analyzed = ""
        for index, char in enumerate(inputted_text):
            if not (inputted_text[index] == " " and inputted_text[index + 1] == " "):
                analyzed = analyzed + char
        params = {'purpose': "Remove Extra Space", 'analyzed_text': analyzed}
        inputted_text = analyzed

    if number_remover == "on":
        analyzed = ""
        numbers = '0123456789'
        for char in inputted_text:
            if char not in numbers:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Numbers', 'analyzed_text': analyzed}

    if remove_punctuation != "on" and uppercase != "on" and newline_remover != "on" and extra_space_remover != "on" \
            and number_remover != "on":
        return HttpResponse("Error!!!")
    return render(request, 'analyze.html', params)
