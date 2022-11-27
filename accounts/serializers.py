from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.validators import UniqueValidator



User=get_user_model()
class RegisterSerializer(serializers.ModelSerializer):
    email=serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
        #check all the users to make sure noone uses the same email
        )
    password_1=serializers.CharField(required=True,write_only=True)
    password_2=serializers.CharField(required=True,write_only=True)

    class Meta:
        model=User
        fields=(
            'email','username',
            'password_1','password_2',
            'first_name','last_name',
        )
        extra_kwargs={
            'first_name':{'required':False},
            'last_name':{'required':False},

        }

    def validate(self, attrs):
        if attrs['password_1'] != attrs['password_2']:
            raise serializers.ValidationError({
                'password':'Passwords did not match.'
            })
        return super(RegisterSerializer, self).validate(attrs)



    def create(self, validated_data):
        user=User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data.get('fist_name',''),
            last_name=validated_data.get('last_name',''),
            password=validated_data['password_1']

        )
        #user.set_password(validated_data['password_1'])
        #I wrote this line in seperate line because if I puted it in the lines above, It did not show as hash pass.
        #user.save()
        return user

