from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    birth_date = serializers.DateField(help_text='(فرمت مناسب: 1988-02-02)')
    class Meta:
        model=Profile
        fields=('birth_date',)

class UserSerializer(serializers.Serializer):
    username=serializers.CharField(max_length=100,required=True,allow_blank=False,allow_null=False,help_text='ضروری .حداکثر 150 کاراکتر')
    first_name = serializers.CharField(max_length=255, required=False, help_text='اختیاری',allow_null=True,allow_blank=True)
    last_name = serializers.CharField(max_length=255, required=False, help_text='اختیاری',allow_null=True,allow_blank=True)
    email = serializers.EmailField(max_length=255,required=True,help_text='لطفا ایمیل به فرمت مناسب استفاده شود')
    password=serializers.CharField(
        write_only=True,
        style={'input_type': 'password', 'placeholder': 'Password'}
    )
    confirm_password=serializers.CharField(
        write_only=True,
        style={'input_type': 'password', 'placeholder': 'Password'}
    )

    profile=ProfileSerializer(required=True)

    def validate_email(self, email):
        existed=User.objects.filter(email=email).first()
        if existed:
            raise serializers.ValidationError("شخص دیگری با همین ایمیل ثبت نام کرده است!")
        return email
    def validate_username(self,username):
        existed=User.objects.filter(username=username).first()
        if existed:
            raise serializers.ValidationError("نام کاربری تکراری است")
        return username
    def validate(self, data):
        if not data.get('password') or not data.get('confirm_password'):
            raise serializers.ValidationError("لطفا فید پسورد و تایید پسورد را پر کنید!")
        elif data.get('password') != data.get('confirm_password'):
            raise serializers.ValidationError("پسوردها یکسان نیستند")
        return data

    def create(self, validated_data):
        user=User.objects.create(
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email'],
            password=make_password(validated_data['password'])
        )
        profile_data=validated_data.pop('profile')
        user.refresh_from_db()
        user.profile.birth_date=profile_data['birth_date']
        return user

    class Meta:
        model=User
        fields = ('username', 'first_name', 'last_name', 'email', 'password','profile', )