class AddressTracker(type):
    """Metaclass keeping track of all the types of Address we understand."""

    #def __init__(cls, name, bases, attrs):
    def __init__(cls):
        if not hasattr(cls, '_addrtypes'):
            cls._addrtypes = []
        else:
            cls._addrtypes.append(cls)

class add(AddressTracker):
    pass

a = add('name',(),{})
