from django.shortcuts import render

# Create your views here.
def demo_page(request):

    if "session_timeout" in request.GET:
        return render(request, "frontendTemplates/demo_page.html", {"session_timeout": 1})

    return render(request, 'frontendTemplates/demo_page.html')