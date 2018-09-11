
def cast(value, toType):

    if toType.upper() == 'INTEGER':
        return toInteger(value)
    else:
        return None


def toInteger(value):
    try:
        return int(value)
    except ValueError as e:
        print('\t* Error parsing value {} to int.'.format(value))
        return value
