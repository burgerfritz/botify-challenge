from django.core.exceptions import ValidationError


FIELDS = {
    'name': str,
    'code': int,
    'population': int,
    'average_age': float,
    'distr_code': int,
    'dept_code': int,
    'region_name': str,
    'region_code': int,
}


PREDICATES = {
    'equal': ' = ',
    'gt': ' > ',
    'lt': ' < ',
    'contains': ' %LIKE% ',
}


def validate_fields(value):
    if not isinstance(value, list):
        raise ValidationError(
            '{} needs to be a list and not a ' + str(type(value))
            .format(value)
        )
    for field in value:
        if field not in FIELDS:
            raise ValidationError(
                field + ' is not a valid field. Please use one of these: '
                + ', '.join(FIELDS.keys())
            )


def validate_filters(value):
    if value:
        if not isinstance(value, dict):
            raise ValidationError(
                '{} needs to be a dictionary and not a ' + str(type(value))
                .format(value)
            )
        if 'field' not in value:
            raise ValidationError(
                'field key must be in filters keys')
        else:
            if value['field'] not in FIELDS:
                raise ValidationError(
                    value['field'] + ' is not a valid field. Please use one of these: '
                    + ', '.join(FIELDS.keys())
                )
            else:
                if type(value['field']) != FIELDS[value['field']]:
                    raise ValidationError(
                        'Type of {} needs to be {} and not ' + str(type(value['field']))
                        .format(value['field'], FIELDS[value['field']])
                    )
        if 'value' not in value:
            raise ValidationError(
                'value key must be in filters keys')

        if 'predicate' in value and value['predicate'] not in PREDICATES.keys():
            raise ValidationError(
                value['predicate'] + ' is not valid. Please use one of these: '
                + ', '.join(PREDICATES.keys())
            )


def build_query(validated_data):
    query = 'SELECT '
    query += ', '.join(validated_data.get('fields'))
    query += ' FROM towns'

    filters = validated_data.get('filters')
    if filters:
        query += ' WHERE '
        query += str(filters['field'])
        query += PREDICATES[filters.get('predicate')] if 'predicate' in filters else ' = '
        query += str(filters['value'])
    return query
