from __future__ import print_function
from future.utils import raise_from

class Order(object):
    """This represents a checkout in the Holvi system"""
    def __init__(self, connection, jsondata=None):
        self.connection = connection
        if not jsondata:
            self._init_empty()
        else:
            self._jsondata = jsondata

    def __getattr__(self, attr):
        if attr[0] != '_':
            return self._jsondata[attr]
        try:
            return object.__getattribute__(self, attr)
        except KeyError as e:
            raise_from(AttributeError, e)

    def _init_empty(self):
        """Creates the base set of attributes order has/needs"""
        raise NotImplementedError()

    def save(self):
        """Creates or updates the order"""
        raise NotImplementedError()


class CheckoutAPI(object):
    """Handles the operations on invoices, instantiate with a Connection object"""

    def __init__(self, connection):
        self.connection = connection
        raise NotImplementedError()
        self.base_url = str(connection.base_url_fmt + self.base_url_fmt).format(pool=connection.pool)
