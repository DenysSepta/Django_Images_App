from django.shortcuts import render
from rest_framework import viewsets
from .models import Image
from .serializers import ImageSerializer
from rest_framework.permissions import IsAuthenticated

class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)
