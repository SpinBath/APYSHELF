from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from django.shortcuts import get_object_or_404
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.authtoken.models import Token

from .models import CustomUser  
from .serializers import UserSerializer




@api_view(['POST'])
def login(request):

    user = get_object_or_404(CustomUser, email=request.data['email'])

    if not user.check_password(request.data['password']):
        return Response("missing user", status=status.HTTP_404_NOT_FOUND)
    
    token, created = Token.objects.get_or_create(user=user)

    serializer = UserSerializer(user)

    return Response({'token': token.key, 'user': serializer.data})


@api_view(['POST'])
def signup(request):

    serializer = UserSerializer(data=request.data)

    if serializer.is_valid():
        
        user = serializer.save()
        user.set_password(request.data['password'])
        user.save()

        token = Token.objects.create(user=user)

        return Response({"token": token.key, "user": serializer.data})
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def test_token(request):

    user = request.user

    user_data = {
            "profile_image": str(user.profile_image),
            "id": user.id,
            "email": user.email,
            "name": user.name,
            "middlename": user.middlename,
            "lastname": user.lastname,
            "national_id": user.national_id,
            "phone": user.phone,
            "is_staff": user.is_staff,
        }

    return Response(user_data)
