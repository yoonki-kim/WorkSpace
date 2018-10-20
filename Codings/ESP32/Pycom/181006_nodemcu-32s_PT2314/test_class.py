class Address(object):
    """An address for one or more ballasts."""
    _addrtypes = []

    @classmethod
    def __init__(cls):
        if not hasattr(cls, '_addrtypes'):
            cls._addrtypes = []
        else:
            cls._addrtypes.append(cls)

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
