from accounts.models import User
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status
from ..serializers import (
    RegisterSerializer,
    CustomAuthTokenSerializer,
    CustomTokenObtainPairSerializer,
    ChangePasswordSerializer,
    ActivateResendSerializer,
)
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView

# from django.core.mail import send_mail
from mail_templated import EmailMessage
from ...utils import EmailThread
from rest_framework_simplejwt.tokens import RefreshToken
from django.shortcuts import get_object_or_404
import jwt
from django.conf import settings


class RegisterApiViews(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            email = serializer.validated_data["email"]
            data = {"email": email}
            user_object = get_object_or_404(User, email=email)
            token = self.get_tokens_for_user(user_object)
            email_obj = EmailMessage(
                "email/activation.tpl",
                {"token": token},
                "reza72rg@gmail.com",
                to=[email],
            )
            EmailThread(email_obj).start()
            return Response(data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_tokens_for_user(self, user):
        refresh = RefreshToken.for_user(user)
        return str(refresh.access_token)


class CustomAuthToken(ObtainAuthToken):
    serializer_class = CustomAuthTokenSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data, context={"request": request}
        )
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        token, created = Token.objects.get_or_create(user=user)
        return Response(
            {"token": token.key, "user_id": user.pk, "email": user.email}
        )


class CustomDiscardAuthToken(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class ChangePasswordApiView(generics.GenericAPIView):
    serializer_class = ChangePasswordSerializer
    model = User
    permission_classes = (IsAuthenticated,)

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def put(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(
                serializer.data.get("old_password")
            ):
                return Response(
                    {"old_password": ["Wrong password."]},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            return Response(
                {"details": "password was change successfully"},
                status=status.HTTP_200_OK,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ActivationApiView(APIView):
    def get(self, request, token, *args, **kwargs):
        try:
            token = jwt.decode(
                token, key=settings.SECRET_KEY, algorithms=["HS256"]
            )
            user_id = token.get("user_id")
            user = User.objects.get(pk=user_id)
            if not user.is_verified:
                user.is_verified = True
                user.save()
                return Response(
                    {"email": "Successfully activated"},
                    status=status.HTTP_200_OK,
                )
            else:
                return Response(
                    {"error": "Your accounts already been verified"},
                    status=status.HTTP_200_OK,
                )
        except jwt.ExpiredSignatureError:
            return Response(
                {"error": "Activations link expired"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        except jwt.exceptions.DecodeError:
            return Response(
                {"error": "Invalid Token"},
                status=status.HTTP_400_BAD_REQUEST,
            )


class ActivationResendApiView(generics.GenericAPIView):
    serializer_class = ActivateResendSerializer

    def post(self, request, *args, **kwargs):
        serializer = ActivateResendSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user_object = serializer.validated_data["user"]
        token = self.get_tokens_for_user(user_object)
        email_obj = EmailMessage(
            "email/activation.tpl",
            {"token": token},
            "reza72rg@gmail.com",
            to=[user_object.email],
        )
        EmailThread(email_obj).start()
        return Response(
            {"detail": "Email activate resend successfully"},
            status=status.HTTP_200_OK,
        )

    def get_tokens_for_user(self, user):
        refresh = RefreshToken.for_user(user)
        return str(refresh.access_token)


"""class SendEmail(generics.GenericAPIView):
    def get(self, request, *args, **kwargs):
        self.email = "r@gmail.com"
        user_object = get_object_or_404(User, email=self.email)
        token = self.get_tokens_for_user(user_object)
        email_obj = EmailMessage(
            "email/activation.tpl",
            {"token": token},
            "reza72rg@gmail.com",
            to=[self.email],
        )
        EmailThread(email_obj).start()
        return Response({"detail": "Send email successful"})

    def get_tokens_for_user(self, user):
        refresh = RefreshToken.for_user(user)
        return str(refresh.access_token)
"""
