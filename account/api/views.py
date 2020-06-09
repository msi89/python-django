from django.http import JsonResponse, HttpResponse
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import RegisterSerializer
from account.models import Account
from .serializers import (
    AccountSerializer, UpdateAccountSerializer)


@api_view(['GET', ])
@permission_classes([IsAuthenticated])
def getAllUsers(request):
    if request.method == 'GET':
        accounts = Account.objects.all()
        serializer = AccountSerializer(accounts, many=True)
        return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def getUser(request, pk):
    try:
        account = Account.objects.get(pk=pk)
    except Account.DoesNotExist:
        return JsonResponse({'error': 'account does not exists'}, status=404)

    if request.method == 'GET':
        serializer = AccountSerializer(account)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = UpdateAccountSerializer(account, data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)

    if request.method == 'DELETE':
        account.delete()
        return HttpResponse(status=204)


@api_view(['POST', ])
@permission_classes([AllowAny])
def signUp(request):
    if request.method == 'POST':
        serializer = RegisterSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            account = serializer.save()
            data['id'] = account.pk
            data['full_name'] = account.full_name
            data['email'] = account.email
            data['username'] = account.username
            data['is_admin'] = account.is_admin
            data['is_active'] = account.is_active
            token = Token.objects.get(user=account)
            data['token'] = token.key
        else:
            return Response(serializer.errors, status=400)
        return Response(data)


@api_view(['GET'])
def getCurrentUser(request):
    serializer = AccountSerializer(request.user)
    return Response(serializer.data)
