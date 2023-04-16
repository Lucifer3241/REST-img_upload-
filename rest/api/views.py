from rest_framework import generics

from .models import Airport
from .serializer import AirportSerilizer


class AirportList(generics.ListCreateAPIView):
    serializer_class=AirportSerilizer
    queryset=Airport.objects.all()

class AirportDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class=AirportSerilizer
    queryset=Airport.objects.all()


from rest_framework import permissions
from rest_framework.parsers import MultiPartParser, FormParser

class AirportViewSet(generics.ListCreateAPIView):
    queryset = Airport.objects.order_by()
    serializer_class =AirportSerilizer
    parser_classes = (MultiPartParser, FormParser)
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)
