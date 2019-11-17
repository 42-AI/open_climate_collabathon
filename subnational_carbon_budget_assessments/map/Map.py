class Map(object):
    def __init__(self, **kwargs):
        for field in ('id', 'name'):
            setattr(self, field, kwargs.get(field, None))