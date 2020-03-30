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
        self.id_cart = self.marketplace.new_cart()

    def run(self):
        for carts_list in self.carts:
            for elem in carts_list:
                if elem["type"] == "add":
                    nr_crt = 0
                    while nr_crt < elem["quantity"]:
                        res = self.marketplace.add_to_cart(self.id_cart, elem["product"])
                        if not res:
                            time.sleep(self.retry_wait_time)
                            continue
                        else:
                            nr_crt = nr_crt + 1

                if elem["type"] == "remove":
                    quantity_elem = elem["quantity"]
                    while quantity_elem > 0:
                        self.marketplace.remove_from_cart(self.id_cart, elem["product"])
                        quantity_elem -= 1

        for product in self.marketplace.place_order(self.id_cart):
            print("%s bought %s" % (self.kwargs["name"], product))
