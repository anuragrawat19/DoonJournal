from django.shortcuts import render
from .models import ContactUs,ContentSection,Images,Article
from django.core.mail import send_mail



# Create your views here.


def home(request):
    template = 'index.html'
    # home_images = Images.objects.filter(active=2,slug='home-scroller')
    main_article = Article.objects.filter(active=2,main_home=True)
    recent_articles = Article.objects.filter(active=2).order_by('-id')[:4]

    if main_article:
        main_article = main_article.latest('id')


    return render(request,template,locals())

def about_us(request):
    template = 'about.html'
    return render(request,template)

def contact_us(request):
    template = 'contact.html'
    if request.method == "POST":
        data = request.POST
        print(data)
        name = data.get('name')
        phone = data.get('phone')
        email = data.get('email')
        message = data.get('message')
        ContactUs.objects.create(name=name,phone=phone,email=email,message=message)
        contact_msg = "Dear Doon Journal , "+ name + " has contacted you  please check the below details. "+" Phone - " + phone + " Email - " + email + " Details - " + message 
        send_mail('New Contact Request',contact_msg,email,['journal.doon@gmail.com'],fail_silently=False,)
        msg = "Thanks for Contacting us, Our team will reach out to you"
    return render(request,template,locals())

def commoncontentpage(request,slug):
    template = 'commoncontentpage.html'
    contents  = ContentSection.objects.filter(active=2,slug=slug)
    if contents:
        content = contents.latest('created')
    return render(request,template,locals())

def articledetail(request,slug):
    template = 'article_detaills.html'
    article  = Article.objects.get(slug=slug)
    recent_articles = Article.objects.filter(active=2).exclude(slug=slug).order_by('-id')[:8]
    return render(request,template,locals())