from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_api import serializers


# Create your views here.
class HelloApiView(APIView):
    """Test APIView"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, ormat=None):
        """ Returns a list of APIView features"""
        an_apiview = [
        "Uses HTTP methods as function(get,post, put, patch)",
        "Is similar to any Django View",
        "Gives you the most control over you aplication logic",
        "is mapped mannnually to URLs",
        ]

        return Response({'message': 'Hello', 'an_apiview': an_apiview })

    def post (self, request):
        """ Create Hello Messagewith our name"""
        serializer= self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(serializer.errors,
            status=status.HTT_400_BAD_REQUEST
            )

    def put (self, request, pk=None):
        """ Handle Updating an object"""
        return Response({'method': 'PUT'})

    def patch (self, request, pk=None):
        """Handle a partial update of an object"""
        return Response({'method': 'PATCH'})

    def delete (self, request, pk=None):
        """Handle a partial update of an object"""
        return Response({'method': 'DELETE'})
