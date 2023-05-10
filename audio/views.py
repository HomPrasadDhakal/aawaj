from django.shortcuts import render
from rest_framework import status, viewsets, mixins
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

from audio.serializers import (
    AllAudoSerializers,
    AllChapterSerializer,
)

from audio.models import (
    AudioBooks,
    Chapters,
)

class AllAudioBooksList(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    permission_classes = [AllowAny]
    serializer_class = AllAudoSerializers
    queryset = AudioBooks.objects.all().order_by("-id")
    
    def list(self, *args, **kwargs):
        allaudiobooks = AudioBooks.objects.all().order_by("-id")
        serializer = AllAudoSerializers(allaudiobooks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def retrieve(self, *args, **kwargs):
        single_audiobooks = AudioBooks.objects.get(id=self.kwargs["pk"])
        SerializerAudioBoooks = AllAudoSerializers(single_audiobooks)
        AllChapter = Chapters.objects.filter(audio_book=single_audiobooks)
        serializer = AllChapterSerializer(AllChapter, many=True)
        AllData = [
            {"main_audiobooks":SerializerAudioBoooks.data},
            {"all_chapters": serializer.data},
        ]
        return Response(AllData, status=status.HTTP_200_OK)