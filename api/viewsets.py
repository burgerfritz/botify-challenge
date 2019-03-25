from api.filters import TownFilter
from api.models import Town
from api.serializers import TownSerializer
from api.serializers import UserSerializer

from django.contrib.auth.models import User

from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.viewsets import GenericViewSet


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class TownViewSet(GenericViewSet, mixins.ListModelMixin):
    """
    API endpoint that allows towns to be viewed, with optional filtering.
    """
    queryset = Town.objects.all()
    serializer_class = TownSerializer
    ordering_fields = ('region_name', 'code', 'region_code', 'population')
    filterset_class = TownFilter
