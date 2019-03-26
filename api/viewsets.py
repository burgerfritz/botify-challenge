from api.filters import TownFilter
from api.models import Town
from api.serializers import TownSerializer
from api.serializers import UserSerializer

from django.contrib.auth.models import User

from django_filters.rest_framework import DjangoFilterBackend

from drf_aggregates.renderers import AggregateRenderer
from drf_aggregates.exceptions import AggregateException
from rest_framework import mixins
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.filters import OrderingFilter
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
    filter_backends = (DjangoFilterBackend, OrderingFilter,)
    filterset_class = TownFilter
    ordering_fields = ('region_name', 'code', 'region_code', 'population')


class TownAggsViewSet(GenericViewSet, mixins.ListModelMixin):
    """
    API endpoint that aggregate the towns in the database by Dept Code.
    """
    queryset = Town.objects.all()
    serializer_class = TownSerializer
    filter_backends = (DjangoFilterBackend,)

    def list(self, request, *args, **kwargs):
        renderer = request.accepted_renderer
        if isinstance(renderer, AggregateRenderer):
            queryset = self.filter_queryset(self.get_queryset())
            try:
                data = request.accepted_renderer.render({
                    'queryset': queryset, 'request': request
                })
            except AggregateException as e:
                # Raise other types of aggregate errors
                return Response(str(e), status=400)
            return Response(data, content_type=f'application/json')
        return super().list(request, *args, **kwargs)
