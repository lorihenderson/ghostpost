from django.shortcuts import render, HttpResponseRedirect, reverse
from homepage import models
from homepage.forms import PostForm
from homepage.models import BoastRoast
from homepage.serializers import BoastRoastSerializer

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response


class CreatePostViewSet(viewsets.ModelViewSet):
    queryset = BoastRoast.objects.all()
    serializer_class = BoastRoastSerializer

    @action(detail=False, methods=["post"])
    def all_boasts(self, request):
        boasts = BoastRoast.objects.filter(choices=True).order_by("-time_posted")
        serializer = self.get_serializer(boasts, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=["post"])
    def all_roasts(self, request):
        roasts = BoastRoast.objects.filter(choices=False).order_by("-time_posted")
        serializer = self.get_serializer(roasts, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=["post"])
    def all_upvotes(self, request, pk=None):
        post = self.get_object()
        post.upvotes += 1
        post.save()
        return Response({"status": post.upvotes})

    @action(detail=True, methods=["post"])
    def all_downvotes(self, request, pk=None):
        post = self.get_object()
        post.downvotes += 1
        post.save()
        return Response({"status": post.downvotes})

    @action(detail=False)
    def total_votes(self, request):
        sorted_votes = sorted(BoastRoast.objects.all(), key=lambda x: x.votes, reverse=True)
        serializer = self.get_serializer(sorted_votes, many=True)
        return Response(serializer.data)