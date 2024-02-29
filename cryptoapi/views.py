from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone 
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from .models import Cryptocurrency
from .serializers import CryptocurrencySerializer, CryptocurrencyUpdateSerializer
# Create your views here.

def main(request):
    return HttpResponse("Crypto")

class CryptocurrencyList(generics.ListCreateAPIView):
    queryset = Cryptocurrency.objects.all()
    serializer_class = CryptocurrencySerializer

class CryptocurrencyUpdate(generics.RetrieveUpdateAPIView):
    queryset = Cryptocurrency.objects.all()
    serializer_class = CryptocurrencyUpdateSerializer
    lookup_field = 'symbol'
    def get(self, request, *args, **kwargs):
        symbol = kwargs.get('symbol').upper()
        try:
            cryptocurrency = Cryptocurrency.objects.get(symbol=symbol)
            serializer = self.get_serializer(cryptocurrency)
            return Response(serializer.data)
        except:
            return Response({"error": f"Cryptocurrency with symbol '{symbol}' does not exist."}, status=status.HTTP_404_NOT_FOUND)
    
    def perform_update(self, serializer):
        # Update the timestamp field before saving
        serializer.validated_data['timestamp'] = timezone.now()
        super().perform_update(serializer)

    def put(self, request, *args, **kwargs):
        symbol = kwargs.get('symbol').upper()
        try:
            cryptocurrency = Cryptocurrency.objects.get(symbol=symbol)
            serializer = self.get_serializer(cryptocurrency)
        except Cryptocurrency.DoesNotExist:
            return Response({"error": f"Cryptocurrency with symbol '{symbol}' does not exist."}, status=status.HTTP_404_NOT_FOUND)
        serializer = self.get_serializer(cryptocurrency, data=request.data, partial=True)
        try:
            serializer.is_valid(raise_exception=True)
        except serializer.ValidationError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        self.perform_update(serializer)
        updated_cryptocurrency = Cryptocurrency.objects.get(symbol=symbol)
        updated_serializer = CryptocurrencySerializer(updated_cryptocurrency)
        return Response(updated_serializer.data)
  

class CryptocurrencyBySymbolView(generics.RetrieveAPIView):
    queryset = Cryptocurrency.objects.all()
    serializer_class = CryptocurrencySerializer
    lookup_field = 'symbol'

    def get(self, request, *args, **kwargs):
        symbol = kwargs.get('symbol').upper()
        try:
            cryptocurrency = Cryptocurrency.objects.get(symbol=symbol)
            serializer = self.get_serializer(cryptocurrency)
            return Response(serializer.data)
        except Cryptocurrency.DoesNotExist:
            return Response({"error": f"Cryptocurrency with symbol '{symbol}' does not exist."}, status=status.HTTP_404_NOT_FOUND)
