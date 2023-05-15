from django.shortcuts import render
from rest_framework import mixins
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status, viewsets
from rest_framework.response import Response
from accounts.serializers import (
    UserRegistrationSerializer,
)
from accounts.models import (
    User,
)
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from accounts.emailintegration import SendGridSendMail
from aawaj import settings
import jwt
from django.http import HttpResponse

class UserRegistration(viewsets.GenericViewSet, mixins.CreateModelMixin):
    serializer_class = UserRegistrationSerializer
    permission_classes = [AllowAny]

    def create(self, request):
        user = request.data
        serializer = UserRegistrationSerializer(data=user)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            user_data = serializer.data
            user = User.objects.get(email=user_data["email"])
            user.user_type = "NORMALUSERS"
            user.save()
            token = RefreshToken.for_user(user).access_token
            subject_message = "please activate your account with the given link to login into the aawaj system"
            current_site = get_current_site(request).domain
            link = (
                current_site
                + "/apis/v1/impl/registration-email-verify/"
                + "?token="
                + str(token)
            )
            message = render_to_string(
                "site/email/user_verification_mail.html",
                {
                    "link": link,
                    "user": user,
                    "redirectlinks": current_site
                },
            )
            SendGridSendMail(to_email=[user.email], subject=subject_message, message=message, from_email=settings.SENDGRID_FROM_EMAIL)
            return Response(user_data, status=status.HTTP_200_OK)
        
class VerifyEmail(viewsets.GenericViewSet, mixins.ListModelMixin):
    permission_classes = [AllowAny]

    def get_serializer_class(self):
        return None

    def list(self, request):
        token = request.GET.get("token")
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
            user = User.objects.get(id=payload["user_id"])
            if not user.is_active:
                user.is_active = True
                user.save()
            return HttpResponse('successfully activated you can login now')
        except jwt.InvalidTokenError as indentifier:
            return HttpResponse("something went wrong try again later")