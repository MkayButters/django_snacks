from django.views.generic import TemplateView

# create views here

class HomeView(TemplateView):
    template_name = 'home.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'
