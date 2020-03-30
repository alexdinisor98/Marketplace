# Marketplace

A marketplace with 2 product types (Tea and Coffee), implementing multiple
producers multiple consumers problem.

The marketplace has:
- a buffer for all the products provided by each producer
(a list with each producer's list of products named "queue")
- a list with each consumer's list of carts named "carts"

To organize the producers' ids, at each new producer a new list is added =>
the size of the "queue" increases => a new producer id.
(Available for carts ids too).

The producer calls the "publish" method to add the product to its list if
there is any available place (limit is queue_size_per_producer). 
If the producer receives False, then it should wait the "republish_wait_time"
and then call the method again.

The consumer calls the "add_to_cart" method to add the product to the specified
cart id in its cart (using append) and remove it from the "queue", so as that the product is unavailable to other consumers if they want to add it in their carts.

The consumer calls the "remove_from_cart" method to remove the product from
its corresponding cart => add it back to the queue so that it is now available
for other customers. There is a check if the product is not available in queue 
=> it should wait(maybe another producer would produce that product)
