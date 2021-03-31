def valid_product_position(solution, product):
    """Checks whether a transportation exchange is valid or not.

    A transportation exchange is valid if no transportation of a product from
    a warehouse to another warehouse is placed after a transportation of the
    same product from a warehouse to the client.
    """

    found_move = False
    drone = None

    sources = set()
    destinations = set()

    for transportation in solution:
        if transportation.product != product:
            continue

        # A chromosome cannot have genes that transport a product to a
        # warehouse it has been before
        #
        # Two genes are deemed repeated if their allele presents the same
        # product and destination;
        #
        # A chromosome must have one and only one gene that transports a
        # product to its final destination.
        #
        # A chromosome cannot have genes that transport the same product
        # from the same warehouse more than once.
        previous_sources_len = len(sources)
        sources.add(transportation.source.id)
        if previous_sources_len == len(sources):
            return False

        previous_destinations_len = len(destinations)
        destinations.add(transportation.destination.id)
        if previous_destinations_len == len(destinations):
            return False

        # If the move is already found and the transportation is to a
        # warehouse then the transportation is not valid
        if found_move and transportation.drone == drone and not transportation.is_final():
            return False
        elif not found_move and transportation.is_final():
            found_move = True
            drone = transportation.drone

    return True


def valid_insert(source_set, destination_set, gene):
    return gene.hash_source() not in source_set and gene.hash_destination() not in destination_set
