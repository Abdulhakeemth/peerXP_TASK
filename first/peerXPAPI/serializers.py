from dataclasses import fields
from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.http import urlsafe_base64_decode
from .models import ManageTicket, NewDepartment, NewTickect, User,Department

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields ='__all__'

class EmailSerializer(serializers.Serializer):
    email = serializers.EmailField()
    class Meta:
        fields = ("email",)  
class ResetPasswordSerializer(serializers.Serializer):
    password = serializers.CharField(
        write_only=True,
        min_length=1,
    )

    class Meta:
        field = ("password")
    def validate(self, data):
        password = data.get("password")
        token = self.context.get("kwargs").get("token")
        encoded_pk = self.context.get("kwargs").get("encoded_pk")

        if token is None or encoded_pk is None:
            raise serializers.ValidationError("Missing data.")

        pk = urlsafe_base64_decode(encoded_pk).decode()
        user = User.objects.get(pk=pk)
        if not PasswordResetTokenGenerator().check_token(user, token):
            raise serializers.ValidationError("The reset token is invalid")

        user.set_password(password)
        user.save()
        return data  

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['Department']

class  UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['Name','Email','Phone_Number','Password','Department_id','Role','Created_by','Created_at','Last_Updated_at']


class NewDepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewDepartment
        fields = ['id','Name','Description','Created_by','Created_at','Last_Updated_at']

class NewTickectSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewTickect 
        fields=['Subject','Body','Priority','Email','Phone_Number']
class ManageTicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = ManageTicket
        fields =['Ticket_ID','Subject','Priority','Created_at']              

         
       