from django.shortcuts import render


def index(request):
    return render(request, 'app/index.html')


def about(request):
    return render(request, 'app/about.html')


def portfolio_work(request):
    return render(request, 'app/portfolio-work.html')


def work_details(request):
    return render(request,'app/work_details.html')


def services(request):
    return render(request, 'app/services.html')


def elements(request):
    return render(request, 'app/elements.html')


def contact(request):
    return render(request, 'app/contact.html')


def blog(request):
    return render(request, 'app/blog.html')


def single_blog(request):
    return render(request, 'app/single-blog.html')
