from api.models import Town
from api.serializers import TownSerializer
from api.serializers import UserSerializer

from django.contrib.auth.models import User

from rest_framework import viewsets


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class TownViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Town.objects.all()
    serializer_class = TownSerializer
