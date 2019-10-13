from django.http import HttpResponse
from django.shortcuts import render, redirect
from categories.models import Categories, News, Images, Videos, Reviews, Cms, Contacted
from categories.forms import ContactedForm


# Create your views here.
def get_cat_title(order_id):
    return Categories.objects.get(home_Page_Order_1_to_5=order_id)


def index(request):
    banners = News.objects.filter(Banner_News=True).order_by('-id')
    popular = News.objects.filter(Popular_News=True).order_by('-id')[:5]
    latest = News.objects.filter().order_by('-id')[:5]
    news1 = News.objects.filter(Categories__in=Categories.objects.filter(home_Page_Order_1_to_5=1)).values('id', 'Categories_id', 'title', 'image', 'description', 'slug').order_by('-id')[:5]
    news2 = News.objects.filter(Categories__in=Categories.objects.filter(home_Page_Order_1_to_5=2)).values('id', 'Categories_id', 'title', 'image', 'description', 'slug').order_by('-id')[:5]
    news3 = News.objects.filter(Categories__in=Categories.objects.filter(home_Page_Order_1_to_5=3)).values('id', 'Categories_id', 'title', 'image', 'description', 'slug').order_by('-id')[:5]
    news4 = News.objects.filter(Categories__in=Categories.objects.filter(home_Page_Order_1_to_5=4)).values('id', 'Categories_id', 'title', 'image', 'description', 'slug').order_by('-id')[:5]
    news5 = News.objects.filter(Categories__in=Categories.objects.filter(home_Page_Order_1_to_5=5)).values('id', 'Categories_id', 'title', 'image', 'description', 'slug').order_by('-id')[:5]
    news1_title = get_cat_title(1)
    news2_title = get_cat_title(2)
    news3_title = get_cat_title(3)
    news4_title = get_cat_title(4)
    news5_title = get_cat_title(5)
    header = Categories.objects.filter(Enable=True)
    contact = Cms.objects.get(id=1)
    return render(request, "categories/index.html",
                  {'banners': banners, 'popular': popular, 'latest': latest, 'news1': news1, 'news2': news2, 'news3': news3,
                   'news4': news4, 'news5': news5, 'news1_title': news1_title, 'news2_title': news2_title,
                   'news3_title': news3_title, 'news4_title': news4_title, 'news5_title': news5_title, 'header': header, 'contact': contact, 'contact': contact})


def detail(request, slug):
    q = News.objects.filter(slug__iexact=slug).values('id', 'Categories_id', 'title', 'image', 'description', 'video', 'slug')
    if q.exists():
        q = q.first()
    else:
        return HttpResponse('<h1>Post Not Found</h1>')

    popular = News.objects.filter(Popular_News=True).order_by('-id')[:5]
    latest = News.objects.filter().order_by('-id')[:5]
    related = News.objects.filter(Categories__in=Categories.objects.filter(id=q['Categories_id'])).order_by('-id')[:3]
    cat = Categories.objects.get(id=q['Categories_id'])
    header = Categories.objects.filter(Enable=True)
    contact = Cms.objects.get(id=1)
    return render(request, "categories/news-detail.html", {'post': q, 'popular': popular, 'latest': latest, 'related': related, 'cat': cat, 'header': header, 'contact': contact})


def category(request, id):
    q = News.objects.filter(Categories_id=id).values('id', 'Categories_id', 'title', 'image', 'description', 'slug').order_by('-id')
    popular = News.objects.filter(Popular_News=True).order_by('-id')[:5]
    latest = News.objects.filter().order_by('-id')[:5]
    header = Categories.objects.filter(Enable=True)
    cat = Categories.objects.get(id=id)
    contact = Cms.objects.get(id=1)
    return render(request, "categories/cat.html", {'popular': popular, 'latest': latest, 'header': header, 'post': q, 'cat': cat, 'contact': contact})


def gallery(request):
    q = Images.objects.all().order_by('-id')
    popular = News.objects.filter(Popular_News=True).order_by('-id')[:5]
    latest = News.objects.filter().order_by('-id')[:5]
    header = Categories.objects.filter(Enable=True)
    contact = Cms.objects.get(id=1)
    return render(request, "categories/gallery.html", {'popular': popular, 'latest': latest, 'header': header, 'post': q, 'contact': contact})


def videos(request):
    q = Videos.objects.all().order_by('-id')
    popular = News.objects.filter(Popular_News=True).order_by('-id')[:5]
    latest = News.objects.filter().order_by('-id')[:5]
    header = Categories.objects.filter(Enable=True)
    contact = Cms.objects.get(id=1)
    return render(request, "categories/videos.html", {'popular': popular, 'latest': latest, 'header': header, 'post': q, 'contact': contact})


def reviews(request):
    q = Reviews.objects.all().order_by('-id')
    popular = News.objects.filter(Popular_News=True).order_by('-id')[:5]
    latest = News.objects.filter().order_by('-id')[:5]
    header = Categories.objects.filter(Enable=True)
    contact = Cms.objects.get(id=1)
    return render(request, "categories/reviews.html", {'popular': popular, 'latest': latest, 'header': header, 'post': q, 'contact': contact})


def contactus(request):
    latest = News.objects.filter().order_by('-id')[:6]
    header = Categories.objects.filter(Enable=True)
    contact = Cms.objects.get(id=1)
    return render(request, "categories/contact.html", {'latest': latest, 'header': header, 'contact': contact})


def cms(request, id):
    popular = News.objects.filter(Popular_News=True).order_by('-id')[:5]
    latest = News.objects.filter().order_by('-id')[:5]
    header = Categories.objects.filter(Enable=True)
    contact = Cms.objects.get(id=1)
    terms = Cms.objects.get(id=id)
    return render(request, "categories/cms.html", {'popular': popular, 'latest': latest, 'header': header, 'terms': terms, 'contact': contact})


def send(request):
    if request.method == "POST":
        form = ContactedForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('/contactus')
    else:
        latest = News.objects.filter().order_by('-id')[:6]
        header = Categories.objects.filter(Enable=True)
        contact = Cms.objects.get(id=1)
        return render(request, "categories/contact.html", {'latest': latest, 'header': header, 'contact': contact})