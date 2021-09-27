from .serializers import RegisterSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.exceptions import AuthenticationFailed
import jwt, datetime

# Create your views here.
@api_view(['POST'])
def RegisterAPI(request):
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response('Failed To Register User!', status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def LoginAPI(request):
    username = request.data['username']
    password = request.data['password']

    user = User.objects.filter(username=username).first()

    if user is None:
        raise AuthenticationFailed('Incorrect Username!')

    if not user.check_password(password):
        raise AuthenticationFailed('Incorrect Password!')

    payload = {
        'id':user.id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=15),
        'iat':datetime.datetime.utcnow()
    }

    token = jwt.encode(payload, key='secret', algorithm='HS256')

    response = Response()
    
    response.set_cookie(key='jwt', value=token, httponly=True)
    response.data = {
        'jwt': token
        }
    return response

@api_view(['GET'])
def UserAPI(request):
    token = request.COOKIES.get('jwt')

    if not token:
        raise AuthenticationFailed('Unauthenticated!')

    try:
        payload = jwt.decode(token, key='secret', algorithms=['HS256'])

    except jwt.ExpiredSignatureError:
        raise AuthenticationFailed('Unauthenticated!')

    user = User.objects.filter(id=payload['id']).first()
    serializer = RegisterSerializer(user)

    return Response(serializer.data)

@api_view(['POST'])
def LogoutAPI(request):
    response = Response()
    response.delete_cookie('jwt')
    response.data = {
        "message":"Successfully Logged Out!"
    }

    return response