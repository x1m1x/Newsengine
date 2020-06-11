from django.shortcuts import redirect

def redirect_news(request):
    return redirect('articles_list_url', permanent=True)
