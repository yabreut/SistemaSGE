from csv import reader
from email import message
from nntplib import ArticleInfo
from django.contrib import messages
from django.views.generic import View
from .models import Blog

class AddArticleView(View):
    template_name = "add_blog.html"
    
    def get(self, request):
        ctx = {}
        return reader(request, self.template_name, ctx)
    
    def post(self, request):
        try:
            article = ArticleInfo()
            article.title = "Bienvenido"
            article.save()
            message.success(request, "Guardado correctamente")
        except: 
            message.error(request, "Hubo un error al guardar el artículo")
        return self.get(request)