from django.shortcuts import render, get_object_or_404
from .models import App  # Assuming the model is named 'App'

def index(request):
    apps = App.objects.all()  # Retrieve all apps from the database
    return render(request, 'app_catlog/index.html', {'apps': apps})

def app_detail(request, name):
    app = App.objects.get(name=name)  # Retrieve the app with the specified id
    return render(request, "app_catlog/app_detail.html", {
        "name": app.name,
        "developer": app.developer,
        "rating": app.rating,
        "is_bestselling": app.is_bestselling 
    })
