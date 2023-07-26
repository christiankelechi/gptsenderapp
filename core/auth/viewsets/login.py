from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework_simplejwt.exceptions import TokenError, InvalidToken
from core.auth.serializers import LoginSerializer
from rest_framework import viewsets

from rest_framework.permissions import IsAuthenticated

class LoginViewSet(ViewSet):
    serializer_class = LoginSerializer
    permission_classes = (AllowAny,)
    http_method_names = ['post']

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        
        
        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise InvalidToken(e.args[0])

        return Response(serializer.validated_data, status=status.HTTP_200_OK)
    
# class StoreCurrentUserTokenViewset(viewsets.ModelViewSet):
#     http_method_names=['post']
#     permission_classes=[IsAuthenticated,]
   

    # def create(self,request,*args,**kwargs):
    #     user_email=request.user
    #     current_user=self.serializer_class(data=request.data)
    #     current_user.save()
    #     return Response({"token_update_message":"User token Updated"},status=status.HTTP_200_OK)


from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.utils import timezone

class UpdateLastLoginView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        # Update the last login of the authenticated user
        request.user.last_login = timezone.now()
        request.user.save()
        return Response({"message": "Last login updated."})