from rest_framework.authtoken.models import Token
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from main.models.auth import User
from main.v1_views.helper import No_method
from main.v1_views.serializer import User_Serializer


class Sign_in(GenericAPIView, No_method):

    permission_classes = AllowAny,

    def post(self, request):
        data = request.data
        print(data)

        if 'email' not in data or 'password' not in data:
            return Response({
                'error':'To\'liq ma\'lumot berilmadi! '
            })
        
        user = User.objects.filter(email=data['email']).first()

        if not user:
            return Response({
                'error':'Foydalanuvchi mavjud emas'
            })
        if not user.check_password(data['password']):
            return Response({
                'error':'Xato parol !'
            })
        
        token = Token.objects.get_or_create(user=user)[0]

        return Response({
            'token': token.key
        })


class Sign_up(GenericAPIView, No_method):
    
    permission_classes = AllowAny,
    serializer_class = User_Serializer

    def post(self, request, *args, **kwargs):
        data = request.data
        password = data.get('password')

        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        user.set_password(str(password))
        user.save()
        
        token = Token.objects.create(user=user)

        return Response({
            'token': token.key
        })
