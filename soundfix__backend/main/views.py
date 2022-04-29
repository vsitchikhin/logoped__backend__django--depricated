from django.http import HttpResponse


def index(request):
  return HttpResponse('Hello world!')


def page(request):
  return HttpResponse('<h1>This is page)</h1>')


def main(requesrt):
  return HttpResponse('This is <h1>MAIN</h1> page')
