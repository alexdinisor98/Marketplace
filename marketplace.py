"""
This module represents the Marketplace.

Computer Systems Architecture Course
Assignment 1
March 2020
"""

class Marketplace:
    """
    Class that represents the Marketplace. It's the central part of the implementation.
    The producers and consumers use its methods concurrently.
    """
    def __init__(self, queue_size_per_producer):
        """
        Constructor

        :type queue_size_per_producer: Int
        :param queue_size_per_producer: the maximum size of a queue associated with each producer
        """
        self.queue_size_per_producer = queue_size_per_producer
        self.queue = [[]]
        self.carts = [[]]
        self.producers_id_list = []

    def register_producer(self):
        """
        Returns an id for the producer that calls this.
        """
        # add a list for each new producer
        self.queue.append([])
        prod_id = len(self.queue) - 1
        self.producers_id_list.append(prod_id)
        return prod_id

    def publish(self, producer_id, product):
        """
        Adds the product provided by the producer to the marketplace

        :type producer_id: String
        :param producer_id: producer id

        :type product: Product
        :param product: the Product that will be published in the Marketplace

        :returns True or False. If the caller receives False, it should wait and then try again.
        """

        list_producer = self.queue[producer_id]
        # check if there is still space available to insert
        if len(list_producer) == self.queue_size_per_producer:
            return False

        # insert the product in the corresponding producer list
        list_producer.append(product)
        return True

    def new_cart(self):
        """
        Creates a new cart for the consumer

        :returns an int representing the cart_id
        """
        # add a new list for each new cart of a consumer
        self.carts.append([])
        return len(self.carts) - 1

    def add_to_cart(self, cart_id, product):
        """
        Adds a product to the given cart. The method returns

        :type cart_id: Int
        :param cart_id: id cart

        :type product: Product
        :param product: the product to add to cart

        :returns True or False. If the caller receives False, it should wait and then try again
        """

        for i in range(0, len(self.queue)):
            current_list_in_queue = self.queue[i]
            if product in current_list_in_queue:
                # adding the product to the consumer's cart
                self.carts[cart_id].append(product)
                # now it is unavailable for other consumers
                self.queue[i].remove(product)
                return True

        return False

    def remove_from_cart(self, cart_id, product):
        """
        Removes a product from cart.

        :type cart_id: Int
        :param cart_id: id cart

        :type product: Product
        :param product: the product to remove from cart
        """

        if product in self.carts[cart_id]:
            # remove product from the corresponding cart
            self.carts[cart_id].remove(product)
            for p_id in self.producers_id_list:
                if len(self.queue[p_id]) == self.queue_size_per_producer:
                    continue
                else:
                    # add it back to queue so as to be
                    # available again for other consumers
                    self.queue[p_id].append(product)
                    break

    def place_order(self, cart_id):
        """
        Return a list with all the products in the cart.

        :type cart_id: Int
        :param cart_id: id cart

        """
        # the list from the specified cart_id
        return self.carts[cart_id]
