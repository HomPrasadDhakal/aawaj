from rest_framework import serializers
from audio.models import (
    AudioBooks,
    Category,
    Chapters,
)
from accounts.models import (
    User,
)
from aawaj import settings
class UserSerializer(serializers.ModelSerializer):
    profile_picture = serializers.ImageField(source="profile.profile_picture", read_only=True)
    address = serializers.CharField(source="profile.address", read_only=True)
    phone = serializers.CharField(source="profile.phone", read_only=True)
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'profile_picture', 'address', 'phone')

class AllChapterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chapters
        fields = ('audio_book', 'title', 'description', 'duration', 'created_at', 'audio_file', 'album')

class AllAudoSerializers(serializers.ModelSerializer):
    category = serializers.CharField(source="category.name", read_only=True)
    uploaded_by = UserSerializer(read_only=True)
    class Meta:
        model = AudioBooks
        fields = ('id','book_name', 'book_author', 'category', 'speaker', 'publication', 'description', 'pdf_file', 'publish_date', 'uploaded_by')