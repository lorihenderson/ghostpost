from django.shortcuts import render, HttpResponseRedirect, reverse
from homepage import models
from homepage.forms import PostForm
from homepage.models import BoastRoast


def index(request):
    ghostposts = models.BoastRoast.objects.all().order_by("-time_posted")
    return render(request, "index.html", {"ghostposts":ghostposts})


def create_post_view(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            models.BoastRoast.objects.create(
                choices = data.get("choices"),
                user_input = data.get("user_input")
            )
            return HttpResponseRedirect(reverse("homepage"))
    form = PostForm()
    return render(request, "createpost.html", {"form": form})


def boast_view(request):
    boast = BoastRoast.objects.filter(choices=True).order_by("-time_posted")
    return render(request, "boasts.html", {"boast": boast})


def roast_view(request):
    roast = BoastRoast.objects.filter(choices=False).order_by("-time_posted")
    return render(request, "roasts.html", {"roast": roast})


def upvote_view(request, upvote_id):
    post = BoastRoast.objects.filter(id=upvote_id).first()
    post.upvotes += 1
    post.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def downvote_view(request, downvote_id):
    post = BoastRoast.objects.filter(id=downvote_id).first()
    post.downvotes += 1
    post.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def sort_by_votes(request):
    sorted_votes = sorted(BoastRoast.objects.all(), key=lambda x: x.votes, reverse=True)
    return render(request, "sortbyvotes.html", {"sorted_votes": sorted_votes})