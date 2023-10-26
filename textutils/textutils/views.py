# I have created this file- Snehal
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def analyze(request):
    text_dj = request.POST.get("text", "default")  # Get text
    remove_punc = request.POST.get('remove_punc', 'off')
    full_caps = request.POST.get('full_caps', 'off')
    newline_remover = request.POST.get('newline_remover', 'off')
    space_remover = request.POST.get('space_remover', 'off')
    char_count = request.POST.get('char_count', 'off')
    print(text_dj)

    if remove_punc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in text_dj:
            if char not in punctuations:
                analyzed = analyzed + char

        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        text_dj = analyzed
        # return render(request, 'analyze.html', params)

    if (full_caps == "on"):
        analyzed = ""
        for char in text_dj:
            analyzed = analyzed + char.upper()

        params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        text_dj = analyzed
        # Analyze the text
        # return render(request, 'analyze.html', params)

    if (space_remover == "on"):
        analyzed = ""
        for index, char in enumerate(text_dj):
            if not (text_dj[index] == " " and text_dj[index + 1] == " "):
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        text_dj = analyzed
        # Analyze the text
        # return render(request, 'analyze.html', params)

    if (newline_remover == "on"):
        analyzed = ""
        for char in text_dj:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
            else:
                print("no")
        print("pre", analyzed)
        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}


    if (char_count == "on"):
        analyzed = 0
        for i in text_dj:
            analyzed = analyzed + 1
        params = {'purpose': 'Character count', 'analyzed_text': analyzed}

    if (remove_punc != "on" and newline_remover != "on" and space_remover != "on" and full_caps != "on" and char_count != "on"):
        return HttpResponse("please select any operation and try again")

    return render(request, 'analyze.html', params)


def about(request):
    return render(request, "about.html", )


def contact(request):
    return render(request, "contact.html", )
