from django.shortcuts import render
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render


from coinbase_commerce.client import Client
from django.shortcuts import render

from CoreRoot import settings



# Create your views here.
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from core.user.models import User

class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})
    
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def check_authorization(request):
    # Perform your authorization check logic here
    if request.user.is_authenticated and request.user.has_perm('core_wallet.can_access_feature'):
        return Response({'message': 'Authorized'}, status=200)
    else:
        return Response({'message': 'Unauthorized'}, status=403)


        

    
