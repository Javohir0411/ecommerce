from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.decorators import api_view
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from rest_framework import status, mixins
from .permissions import IsOwnerOrSuperUser
from datetime import datetime
from .models import PasswordResets
from random import randint
from config import settings

