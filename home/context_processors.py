from wagtail.core.models import Page
from home.models import AboutPage, HomePage # Import your page models

def common_pages(request):
    try:
        about_page = AboutPage.objects.live().first()
    except AboutPage.DoesNotExist:
        about_page = None

    try:
        home_page = HomePage.objects.live().first()
    except HomePage.DoesNotExist:
        home_page = None


    return {
        'about_page': about_page,
        'home_page': home_page,

    }
