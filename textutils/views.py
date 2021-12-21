# self created
from django.http import HttpResponse
from django.shortcuts import render

# def index(request):
#     return HttpResponse('<a href="removepunc"> Remove Punc</a><br><a href="capfirst"> Cap First</a><br><a href="newlineremove"> new line remove</a><br>')

# index for templates
# render have 3 arguments the third one is dictionary
def index(request):
    pars = {"name": "PKC", "place": "Kateya"}
    return render(request, 'ind.html',pars)

# def about(request):
#     return HttpResponse("About page")

# def fb(request):
#     return HttpResponse('<a href="https://www.fb.com"> Facebook page</a>')

# def insta(request):
#     return HttpResponse('<a href="https://www.instagram.com"> Insta page</a>')

# for pipelines

def analyze_text(request):
    # getting the text
    txt = request.POST.get('text','default')
    check_box_response = request.POST.get('puncBox','off')
    check_box_response_char_count = request.POST.get('charCount','off')
    check_box_response_capitalize = request.POST.get('capitalize','off')
    check_box_response_extra_space_remover = request.POST.get('extraSpaceRemover','off')
    check_box_response_new_line_remover = request.POST.get('newLineRemover','off')

    
    # analyze the text
    if check_box_response == "on":
        cc = "!@#$%^&*()[]<>,./?|\;:"
        chr = ''
        for i in txt:
            # if i == " ":
            #     chr += "<span/>"
            #     continue
            # if i == '\n':
            #     chr += '<br/>'
                # continue
        # we don't need to do do above lines because <pre> tag in html format the output as it arrives
            if i not in cc:
                chr += i
        txt = ""
        txt = chr
        chr = ""
    # return HttpResponse('Hello <a href="/">back</a>')
    if check_box_response_capitalize == "on":
        for i in range(len(txt)):
            txt = txt[:i] + txt[i].upper() + txt[i+1:]

    if check_box_response_extra_space_remover == "on":
        chr = ''
        for i,j in enumerate(txt):
            if not (txt[i] == " " and txt[i+1] == " "):
                chr += j

        txt = chr
        chr = ""

    if check_box_response_new_line_remover == "on":
        chr = ""
        for i in txt:
            if i != "\n" and i != '\r':
                chr += i
        txt = chr
        chr = ""

    char_count = {}
    if check_box_response_char_count == "on":
        char_count = {}
        for i in txt:
            if i != " " and i != "\n":
                if i in char_count:
                    char_count[i] += 1
                else:
                    char_count[i] = 1
        # for i,j in d.items():
        #     opl += "{} is {} times\n".format(i,j)
        # print(char_count)
        # return render(request,'txtop.html',{"char_count": char_count})

    paras = {"analyzed_text" : txt, "char_count": char_count}
    return render(request,'txtop.html',paras)
    # return HttpResponse(txt + '<br><a href="/">back</a>')

# def capfirst(request):
#     return HttpResponse('Hello <a href="/">back</a>')

# def newlineremove(request):
#     return HttpResponse('Hello <a href="/">back</a>')

# def spaceremove(request):
#     return HttpResponse('Hello <a href="/">back</a>')

# def charcount(request):
#     return HttpResponse('Hello <a href="/">back</a>')