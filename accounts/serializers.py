from rest_framework import serializers
from accounts.models import (
    User,
)
from django.forms import ValidationError
import re



class UserRegistrationSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    password = serializers.CharField(max_length=55, required=True, write_only=True)
    password2 = serializers.CharField(max_length=55, required=True, write_only=True)
    class Meta:
        model = User
        fields = ["username","email","first_name", "last_name", "password","password2"]
        extra_kwargs = {
            "password": {"write_only": True},
            "password2": {"write_only": True},
        }

    def validate_username(self, username):
        if User.objects.filter(username=username):
            raise ValidationError("Usename already taken")
        
        if len(username) > 10:
            raise ValidationError("username cannot be greater the 10 characters maxium")
        return username
    
    def validate_email(self, email):
    
        if User.objects.filter(email=email):
            raise ValidationError("Email is already register into our system, processed to login")

        if len(email) > 30:
            raise ValidationError("username cannot exceed more then 30 character !!! ")
        return email

    def validate_password(self, password):

        if len(password) < 7:
            raise serializers.ValidationError(
                "This password is too short. It must contain at least "
                "8 characters !!!"
            )

        if not re.search(r"[\d]+", password):
            raise ValidationError("The password must contain at least one digit")

        if password.isdigit():
            raise serializers.ValidationError("password contain all numeric value !!!")

        if not re.search(r"[A-Z]+", password):
            raise ValidationError(
                "The password must contain at least one uppercase character"
            )

        if not re.search(r"[a-z]+", password):
            raise ValidationError(
                "The password must contain at least one lowercase character"
            )
        return password

    def validate(self, data):
        if data["password"] != data["password2"]:
            raise serializers.ValidationError("password dosen't match !!! ")
        return data

    def create(self, validated_data):
        user = User.objects.create_user(
            username = validated_data["username"],
            email = validated_data["email"],
            first_name = validated_data["first_name"],
            last_name = validated_data["last_name"],
            is_active = False,
            user_type = "NORMALUSERS"
        )
        user.set_password(validated_data["password"])
        user.save()
        return user
        

