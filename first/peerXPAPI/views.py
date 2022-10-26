from types import new_class
from rest_framework import viewsets
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
from .models import  NewDepartment, User,Department,NewTickect,ManageTicket
from .serializers import ManageTicketSerializer, UserSerializer,DepartmentSerializer,NewDepartmentSerializer,NewTickectSerializer
from rest_framework import generics, status, viewsets, response
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.urls import reverse
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

from . import serializers

class UserViewSet(viewsets.ModelViewSet):

    permission_classes =(IsAuthenticated,)
    serializer_class = UserSerializer
    queryset = get_user_model().objects.all()
class PasswordReset(generics.GenericAPIView):
    serializer_class = serializers.EmailSerializer 
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.data["email"]
        user = User.objects.filter(email=email).first()
        if user:
            encoded_pk = urlsafe_base64_encode(force_bytes(user.pk))
            token = PasswordResetTokenGenerator().make_token(user)
            reset_url = reverse(
                "reset-password",
                kwargs={"encoded_pk": encoded_pk, "token": token},
            )
            reset_link = f"localhost:8000{reset_url}"

            # send the rest_link as mail to the user.

            return response.Response(
                {
                    "message": 
                    f"Your password rest link: {reset_link}"
                },
                status=status.HTTP_200_OK,
            )
        else:
            return response.Response(
                {"message": "User doesn't exists"},
                status=status.HTTP_400_BAD_REQUEST,
            )


class ResetPasswordAPI(generics.GenericAPIView):
    serializer_class = serializers.ResetPasswordSerializer

    def patch(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data, context={"kwargs": kwargs}
        )
        serializer.is_valid(raise_exception=True)
        return response.Response(
            {"message": "Password reset complete"},
            status=status.HTTP_200_OK,
        )

class ListDepartment(generics.ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
class ListUser(generics.ListCreateAPIView):
    queryset  = User.objects.all()
    serializer_class = UserSerializer

class NewDepartmentlist(generics.ListCreateAPIView):
    queryset  = NewDepartment.objects.all()
    serializer_class = NewDepartmentSerializer

class DetailNewDepartmentlist(generics.RetrieveUpdateDestroyAPIView):
    queryset  = NewDepartment.objects.all()
    serializer_class = NewDepartmentSerializer 
class NewTickectlist(generics.ListCreateAPIView):
    queryset  = NewTickect.objects.all()
    serializer_class = NewTickectSerializer 
class DetailNewTickectList(generics.RetrieveUpdateDestroyAPIView):
    queryset =NewTickect.objects.all()
    serializer_class = NewTickectSerializer

class ManageTickectlist(generics.ListCreateAPIView):
    queryset = ManageTicket.objects.all()
    serializer_class = ManageTicketSerializer   
class DetailManageTickectlist(generics.RetrieveUpdateDestroyAPIView):
    queryset = ManageTicket.objects.all()
    serializer_class =ManageTicketSerializer         




    # def post(self, request, format=None):
    #     serializer = NewDepartmentSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # def get(self, request, format=None):
    #     new_class = NewDepartment.objects.all()
    #     serializer = NewDepartmentSerializer(new_class,many=True)
    #     return Response(serializer.data)  
        
          

    