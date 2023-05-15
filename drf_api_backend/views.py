from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view()
def root_route(request):
    return Response({
        "message": "Hello, and welcome to our social media API.",
    })