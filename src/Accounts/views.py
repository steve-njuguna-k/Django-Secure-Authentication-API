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

    token = jwt.encode(payload, 'secret', algorithm='HS256')

    return Response({
        "message":"Login Successful!",
        "token":token
    })
