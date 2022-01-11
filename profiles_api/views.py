from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class HelloApiView(APIView):
    """Test APIView"""
    def get(self, request, ormat=None):
        """ Returns a list of APIView features"""
        an_apiview = [
        "Uses HTTP methods as function(get,post, put, patch)",
        "Is similar to any Django View",
        "Gives you the most control over you aplication logic",
        "is mapped mannnually to URLs",
        ]

        return Response({'message': 'Hello', 'an_apiview': an_apiview })
