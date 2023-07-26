from .models import EthModel
from .models import UsdModel
from django.shortcuts import render
from rest_framework import status
from  rest_framework.permissions import AllowAny,IsAuthenticated
from .serializers import EthSerializer,BtcSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from core.auth.permissions import UserPermission
from core.user.models import User

from rest_framework.response import Response
from .models import UsdModel
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.shortcuts import render
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render


from coinbase_commerce.client import Client
from django.shortcuts import render

from CoreRoot import settings

trackpayment=[]

class TopUpBtcViewset(viewsets.ViewSet):
    serializer_class = BtcSerializer
    permission_classes = (IsAuthenticated,)
    http_method_names = ['post','get','patch']

    from django.shortcuts import get_list_or_404

# ...

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        payment_stage=1
        if serializer.is_valid():
            user = request.user
            
            
            # Create your views here.
        
            

            from django.shortcuts import render


            
        
            # Retrieve the latest top-up
            
            # Assuming you want the latest top-up
            
            new_topup_amount = serializer.validated_data['amount']
            
            trackpayment.append(new_topup_amount)

            
            response_data = {
                'click_link':'Click this link to continue with toping up your balance http://localhost:8000/wallet/topup/'
                
            }

            return Response(response_data, status=status.HTTP_200_OK)

        return redirect('topup')
    def get_queryset(self):
        return UsdModel.objects.all()
    
    
def topup(request):
    
    client = Client(api_key=settings.COINBASE_COMMERCE_API_KEY)
    domain_url = 'http://localhost:8000/'
    product = {
        'name': 'Top Up Wallet',
        'description': 'Top up your wallet address to be able to gpt sender product',
        'local_price': {
            'amount': f'{trackpayment[0]}',
            'currency': 'USD'
        },
        'pricing_type': 'fixed_price',
        'redirect_url': domain_url + 'success/',
        'cancel_url': domain_url + 'cancel/',
    }
    charge = client.charge.create(**product)

    return render(request, 'home.html', {
        'charge': charge,
    })


def success_view(request):
    user=request.user
    new_topup = UsdModel.objects.get(user=user)
    total_payment=int(trackpayment[0])+new_topup
    new_topup.amount=total_payment
    new_topup.save()
    return Response({"successful_msg":f"{user} top up of {trackpayment[0]} successful total balance is {total_payment}"}, 'success.html', {})


def cancel_view(request):
    return render(request, 'cancel.html', {})


    # def list(self, request):
    #     try:
    #         user = request.user
    #         current_balance = UsdModel.objects.filter(user=user).latest('id')    # Retrieve the UsdModel based on the user's ID
    #         total_amount = current_balance.amount
    #         return Response({"successful_msg":total_amount},status=status.HTTP_200_OK)
    #     except UsdModel.DoesNotExist:
    #     # Create a new UsdModel for the user
    #         import random
    #         def randomWalletAddress(N):
    #             minimum = pow(10, N-1)
    #             maximum = pow(10, N) - 1
    #             return random.randint(minimum, maximum)

    #         wallet_address=randomWalletAddress(10)
    #         wallet_address=wallet_address
            

    #         new_balance = UsdModel.objects.create(wallet_address=wallet_address,user=user, amount=0)

    
    

    #         new_balance = UsdModel.objects.create(wallet_address=wallet_address,user=user, amount=0)

    #         return Response({"successful_msg": new_balance.amount}, status=status.HTTP_200_OK)



    
    
    # def get_object(self):
    #     obj = BtcModel.objects.get(pk=id)

    #     self.check_object_permissions(self.request, obj)


class BtcAmountView(viewsets.ViewSet):
    
    def create(self,request):
        user=request.user
        current_balance=get_object_or_404(UsdModel,user__email=user.email)
        current_balance.amount
        
