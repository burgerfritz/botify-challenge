from api.models import Town

from django.contrib.auth.models import User

from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class TownField(serializers.Field):

    def to_representation(self, value):
        ret = {
            value.name: {
                'region_name': value.region_name,
                'code': value.code,
                'region_code': value.region_code,
                'population': value.population,
            }
        }
        return ret

    def to_internal_value(self, data):
        ret = {
            data['town_name']:
                {
                    'region_name': data['region_name'],
                    'code': data['code'],
                    'region_code': data['region_code'],
                    'population': data['population'],
                }
        }
        return ret


class TownSerializer(serializers.HyperlinkedModelSerializer):
    town = TownField(source='*')

    class Meta:
        model = Town
        fields = ('town',)
