def add_metaclass(metaclass):
    """Class decorator for creating a class with a metaclass."""

    def wrapper(cls):
        orig_vars = cls.__dict__.copy()
        orig_vars.pop('__dict__', None)
        orig_vars.pop('__weakref__', None)
        slots = orig_vars.get('__slots__')
        if slots is not None:
            if isinstance(slots, str):
                slots = [slots]
            for slots_var in slots:
                orig_vars.pop(slots_var)

        return metaclass(cls.__name__, cls.__bases__, orig_vars)
        #return metaclass
    return wrapper

class AddressTracker(type):
    """Metaclass keeping track of all the types of Address we understand."""

    def __init__(cls, name, bases, attrs):
    #def __init__(cls):
        if not hasattr(cls, '_addrtypes'):
            cls._addrtypes = []
        else:
            cls._addrtypes.append(cls)

@add_metaclass(AddressTracker)
class Address(object):
    """An address for one or more ballasts."""

    @classmethod
    def from_frame(cls, f):
        """Return an Address object

        If the frame has a destination address, return a suitable
        Address object; otherwise return None.
        """
        if cls != Address:
            return
        for at in cls._addrtypes:
            r = at.from_frame(f)
            if r:
                return r

    def add_to_frame(self, f):
        raise IncompatibleFrame("Cannot add unknown address to any frame")

    def __str__(self):
        return "<no address>"