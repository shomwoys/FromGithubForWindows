from django import http, template

def home(request):
    return http.HttpResponse('Hello World!')
  

def index(request):
    t = template.loader.get_template('index.html')
    c = template.Context({'var':'context var'})
    return http.HttpResponse(t.render(c))