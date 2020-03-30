"""
This module represents the Consumer.

Computer Systems Architecture Course
Assignment 1
March 2020
"""
import time
from threading import Thread


class Consumer(Thread):
    """
    Class that represents a consumer.
    """

    def __init__(self, carts, marketplace, retry_wait_time, **kwargs):
        """
        Constructor.

        :type carts: List
        :param carts: a list of add and remove operations

        :type marketplace: Marketplace
        :param marketplace: a reference to the marketplace

        :type retry_wait_time: Time
        :param retry_wait_time: the number of seconds that a producer must wait
        until the Marketplace becomes available

        :type kwargs:
        :param kwargs: other arguments that are passed to the Thread's __init__()
        """
        Thread.__init__(self, **kwargs)
        self.carts = carts
        self.marketplace = marketplace
        self.retry_wait_time = retry_wait_time
        self.kwargs = kwargs
        self.id = self.marketplace.new_cart()

    def run(self):
        for list in self.carts:
            for elem in list:
                if elem["type"] == "add":
                    nrcrt = 0
                    while nrcrt < elem["quantity"]:
                        res = self.marketplace.add_to_cart(self.id, elem["product"])
                        if not res:
                            time.sleep(self.retry_wait_time)
                            continue
                        else:
                            nrcrt = nrcrt + 1

                if elem["type"] == "remove":
                    for i in range(0, elem["quantity"]):
                        self.marketplace.remove_from_cart(self.id, elem["product"])

        for product in self.marketplace.place_order(self.id):
            print("%s bought %s" % (self.kwargs["name"], product))
