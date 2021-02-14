from django.shortcuts import loader
from django.http import HttpResponse
import sys
import datetime as mydt
# Create your views here.


def index(request):
    r_string = ""
    r_string += str(datetime.datetime.now()) + "\n"
    for p in sys.path:
        r_string += p
        r_string += "\n"

    return HttpResponse("path used in project:\n"+r_string)


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)


def test(request):
    myVar = 23
    template = loader.get_template('polls/myHtml/test.html')
    context = {
        'latest_question_list': myVar,
    }
    return HttpResponse(template.render(context, request))

def test(request):
    now = mydt.datetime.now()
    html = "<html>" \
           "<body>It is now %s.</body>" \
           "</html>" % now
    return HttpResponse(html)
