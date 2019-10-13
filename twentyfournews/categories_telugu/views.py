from django.http import HttpResponse
from django.shortcuts import render, redirect
from categories_telugu.models import Categories_telugu, News_telugu, Images_telugu, Videos_telugu, Reviews_telugu, Cms_telugu, Contacted_telugu
from categories_telugu.forms import ContactedteForm


# Create your views here.
def get_cat_title(order_id):
    return Categories_telugu.objects.get(home_Page_Order_1_to_5=order_id)


def index(request):
    banners = News_telugu.objects.filter(Banner_News=True).order_by('-id')
    popular = News_telugu.objects.filter(Popular_News=True).order_by('-id')[:5]
    latest = News_telugu.objects.filter().order_by('-id')[:5]
    news1 = News_telugu.objects.filter(Categories__in=Categories_telugu.objects.filter(home_Page_Order_1_to_5=1)).values('id', 'Categories_id', 'title', 'telugu_title', 'image', 'description', 'slug').order_by('-id')[:5]
    news2 = News_telugu.objects.filter(Categories__in=Categories_telugu.objects.filter(home_Page_Order_1_to_5=2)).values('id', 'Categories_id', 'title', 'telugu_title', 'image', 'description', 'slug').order_by('-id')[:5]
    news3 = News_telugu.objects.filter(Categories__in=Categories_telugu.objects.filter(home_Page_Order_1_to_5=3)).values('id', 'Categories_id', 'title', 'telugu_title', 'image', 'description', 'slug').order_by('-id')[:5]
    news4 = News_telugu.objects.filter(Categories__in=Categories_telugu.objects.filter(home_Page_Order_1_to_5=4)).values('id', 'Categories_id', 'title', 'telugu_title', 'image', 'description', 'slug').order_by('-id')[:5]
    news5 = News_telugu.objects.filter(Categories__in=Categories_telugu.objects.filter(home_Page_Order_1_to_5=5)).values('id', 'Categories_id', 'title', 'telugu_title', 'image', 'description', 'slug').order_by('-id')[:5]
    news1_title = get_cat_title(1)
    news2_title = get_cat_title(2)
    news3_title = get_cat_title(3)
    news4_title = get_cat_title(4)
    news5_title = get_cat_title(5)
    header = Categories_telugu.objects.filter(Enable=True)
    contact = Cms_telugu.objects.get(id=1)
    return render(request, "categories_telugu/index.html",
                  {'banners': banners, 'popular': popular, 'latest': latest, 'news1': news1, 'news2': news2, 'news3': news3,
                   'news4': news4, 'news5': news5, 'news1_title': news1_title, 'news2_title': news2_title,
                   'news3_title': news3_title, 'news4_title': news4_title, 'news5_title': news5_title, 'header': header, 'contact': contact})


def telugudetail(request, slug):
    q = News_telugu.objects.filter(slug__iexact=slug).values('id', 'Categories_id', 'title', 'telugu_title', 'image', 'description', 'video', 'slug')
    if q.exists():
        q = q.first()
    else:
        return HttpResponse('<h1>Post Not Found</h1>')

    popular = News_telugu.objects.filter(Popular_News=True).order_by('-id')[:5]
    latest = News_telugu.objects.filter().order_by('-id')[:5]
    related = News_telugu.objects.filter(Categories__in=Categories_telugu.objects.filter(id=q['Categories_id'])).order_by('-id')[:3]
    cat = Categories_telugu.objects.get(id=q['Categories_id'])
    header = Categories_telugu.objects.filter(Enable=True)
    contact = Cms_telugu.objects.get(id=1)
    return render(request, "categories_telugu/news-detail.html", {'post': q, 'popular': popular, 'latest': latest, 'related': related, 'cat': cat, 'header': header, 'contact': contact})


def telugucategory(request, id):
    q = News_telugu.objects.filter(Categories_id=id).values('id', 'Categories_id', 'title', 'image', 'description', 'slug').order_by('-id')
    popular = News_telugu.objects.filter(Popular_News=True).order_by('-id')[:5]
    latest = News_telugu.objects.filter().order_by('-id')[:5]
    header = Categories_telugu.objects.filter(Enable=True)
    cat = Categories_telugu.objects.get(id=id)
    contact = Cms_telugu.objects.get(id=1)
    return render(request, "categories_telugu/cat.html", {'popular': popular, 'latest': latest, 'header': header, 'post': q, 'cat': cat, 'contact': contact})


def telugugallery(request):
    q = Images_telugu.objects.all().order_by('-id')
    popular = News_telugu.objects.filter(Popular_News=True).order_by('-id')[:5]
    latest = News_telugu.objects.filter().order_by('-id')[:5]
    header = Categories_telugu.objects.filter(Enable=True)
    contact = Cms_telugu.objects.get(id=1)
    return render(request, "categories_telugu/gallery.html", {'popular': popular, 'latest': latest, 'header': header, 'post': q, 'contact': contact})


def teluguvideos(request):
    q = Videos_telugu.objects.all().order_by('-id')
    popular = News_telugu.objects.filter(Popular_News=True).order_by('-id')[:5]
    latest = News_telugu.objects.filter().order_by('-id')[:5]
    header = Categories_telugu.objects.filter(Enable=True)
    contact = Cms_telugu.objects.get(id=1)
    return render(request, "categories_telugu/videos.html", {'popular': popular, 'latest': latest, 'header': header, 'post': q, 'contact': contact})


def telugureviews(request):
    q = Reviews_telugu.objects.all().order_by('-id')
    popular = News_telugu.objects.filter(Popular_News=True).order_by('-id')[:5]
    latest = News_telugu.objects.filter().order_by('-id')[:5]
    header = Categories_telugu.objects.filter(Enable=True)
    contact = Cms_telugu.objects.get(id=1)
    return render(request, "categories_telugu/reviews.html", {'popular': popular, 'latest': latest, 'header': header, 'post': q, 'contact': contact})


def telugucontactus(request):
    latest = News_telugu.objects.filter().order_by('-id')[:6]
    header = Categories_telugu.objects.filter(Enable=True)
    contact = Cms_telugu.objects.get(id=1)
    return render(request, "categories_telugu/contact.html", {'latest': latest, 'header': header, 'contact': contact})


def telugucms(request, id):
    popular = News_telugu.objects.filter(Popular_News=True).order_by('-id')[:5]
    latest = News_telugu.objects.filter().order_by('-id')[:5]
    header = Categories_telugu.objects.filter(Enable=True)
    contact = Cms_telugu.objects.get(id=1)
    terms = Cms_telugu.objects.get(id=id)
    return render(request, "categories_telugu/cms.html", {'popular': popular, 'latest': latest, 'header': header, 'terms': terms, 'contact': contact})


def tesend(request):
    if request.method == "POST":
        form = ContactedteForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('/contactus')
    else:
        latest = News_telugu.objects.filter().order_by('-id')[:6]
        header = Categories_telugu.objects.filter(Enable=True)
        contact = Cms_telugu.objects.get(id=1)
        return render(request, "categories_telugu/contact.html", {'latest': latest, 'header': header, 'contact': contact})