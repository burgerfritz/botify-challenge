from api.filters import TownFilter
from api.models import BQLQueryTown
from api.models import Town
from api.serializers import BQLQueryTownSerializer
from api.serializers import TownSerializer
from api.serializers import UserSerializer
from api.utils import build_query

from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

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


class QueryViewSet(GenericViewSet, mixins.CreateModelMixin):
    """
    API endpoint for of transforming a JSON query (in a custom DSL)
    into a SQLite Query.
    More information about the custom DSL at:
    https://developers.botify.com/api/bql/
    """
    queryset = BQLQueryTown.objects.all()
    serializer_class = BQLQueryTownSerializer

    def create(self, request, *args, **kwargs):
        if 'fields' not in request.data:
            raise ValidationError(
                'fields key must be at the root of the DSL query')

        serializer = BQLQueryTownSerializer(data=request.data)
        if serializer.is_valid():
            result = build_query(request.data)
            data = {'query': result}
            return Response(data)
        return super().create(request, *args, **kwargs)
