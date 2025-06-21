from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer,CharField,ValidationError
class UserSerializer(ModelSerializer):
    confirm_password = CharField(write_only=True,style={'input_type':'password'})
    class Meta:
        model = User
        fields = ['username','email','password','confirm_password']
        extra_kwargs = {
            'password':{'write_only':True},
            'style':{'input_type':'password'},
        }
    def save(self):
        if self.validated_data['password'] == self.validated_data['confirm_password']:
            if User.objects.filter(email=self.validated_data['email']).exists():
                raise ValidationError("Account With This Email Already Exists")
            else:
                account = User(email=self.validated_data['email'],username=self.validated_data['username'])
                account.set_password(self.validated_data['password'])
                account.save()
                return account
        else:
            raise ValidationError("Passwords Do Not Match")