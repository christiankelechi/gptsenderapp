from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets

from core.user.serializers import UserSerializer
from core.user.models import User
from core.auth.permissions import UserPermission
from core.user.serializers import CurrentUserTokenSerializer
from rest_framework.response import Response
from rest_framework import status
from core.user.models import CurrentUserToken
from django.shortcuts import get_object_or_404
from django.db import IntegrityError

class UserViewSet(viewsets.ModelViewSet):
    http_method_names = ('patch', 'get','post')
    permission_classes = (IsAuthenticated,UserPermission)
    serializer_class = UserSerializer

    def get_queryset(self):
        if self.request.user.is_superuser:
            return User.objects.all()
        return User.objects.exclude(is_superuser=True)

    def get_object(self):
        obj = User.objects.get_object_by_public_id(self.kwargs['pk'])

        self.check_object_permissions(self.request, obj)

        return obj

    
class CurrentUserTokenViewset(viewsets.ModelViewSet):
    serializer_class=CurrentUserTokenSerializer
    permission_classes=[IsAuthenticated,]
    http_method_names=['get','post']

    def create(self,request):
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = request.user
            token=serializer.validated_data['token']
            if user in CurrentUserToken.objects.all().get('user').user:
                print(user)
            serializer.save(user=user, token=serializer.validated_data['token'],time_of_generation=serializer.validated_data['time_of_generation'])

            try:
            # Check if an existing token exists for the user
                existing_token = CurrentUserToken.objects.get(user=user)
                existing_token.token = token
                existing_token.save()
                return Response({"success_msg": "Token updated successfully"}, status=status.HTTP_200_OK)
            except CurrentUserToken.DoesNotExist:
                # Create a new token
                serializer.save(user=user, token=token)
                return Response({"success_msg": "Token stored successfully"}, status=status.HTTP_200_OK)
            except IntegrityError:
                return Response({"error_msg": "Integrity Error occurred"}, status=status.HTTP_400_BAD_REQUEST)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def list(self, request):
        try:
            user = request.user
            current_token = CurrentUserToken.objects.filter(user=user).latest('id')    # Retrieve the UsdModel based on the user's ID
            user_token = current_token.token
            return Response({"user_token":user_token},status=status.HTTP_200_OK)
        except CurrentUserToken.DoesNotExist:
        # Create a new UsdModel for the user
            # new_balance = UsdModel.objects.create(user=user, amount=0)
            return Response({"error_message":"no_token_for_user"}, status=status.HTTP_200_OK)


        
    def get_object(self):
        return super().get_object()

    def get_queryset(self):
        return CurrentUserToken.objects.all()