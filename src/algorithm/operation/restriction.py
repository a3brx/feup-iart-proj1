def valid_insert(source_set, destination_set, gene):
    return gene.hash_source() not in source_set and gene.hash_destination() not in destination_set
