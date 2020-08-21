"""ghostpost URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from homepage.views import index, boast_view, roast_view, create_post_view, upvote_view, downvote_view, sort_by_votes

urlpatterns = [
    path('', index, name="homepage"),
    path('sortbyvotes/', sort_by_votes),
    path('boasts/', boast_view),
    path('roasts/', roast_view),
    path('createpost/', create_post_view),
    path('upvote/<int:upvote_id>/', upvote_view),
    path('downvote/<int:downvote_id>/', downvote_view),
    path('admin/', admin.site.urls),
]
