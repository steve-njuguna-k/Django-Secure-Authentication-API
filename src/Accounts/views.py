from .serializers import RegisterSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

# Create your views here.
@api_view(['POST'])
def RegisterAPI(request):
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response('Failed To Register User!', status=status.HTTP_400_BAD_REQUEST)