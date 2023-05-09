from django.shortcuts import render
from rest_framework import status, viewsets, mixins
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
import requests
from audio.serializers import (
    AllAudoSerializers,

)
from audio.models import (
    AudioBooks,
)

class AllAudioBooksList(viewsets.GenericViewSet, mixins.ListModelMixin):
    permission_classes = [AllowAny]
    serializer_class = AllAudoSerializers
    
    def list(self, *args, **kwargs):
        allaudiobooks = AudioBooks.objects.all().order_by("-id")
        serializer = AllAudoSerializers(allaudiobooks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)