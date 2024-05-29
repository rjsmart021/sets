our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}


def get_common_destinations() -> set[str]:
    """
    :return: all destinations that are common between your and competitor arlines.
    """
    return our_routes.intersection(competitor_routes)


def get_your_unique_destinations() -> set[str]:
    """
    :return: all destinations that are unique to your airline
    """
    return our_routes.difference(competitor_routes)


def get_unshared_destinations() -> set[str]:
    """
    :return: all destinations that neither shares by both airlines.
    """
    return our_routes.symmetric_difference(competitor_routes)


print("Destinations that both airlines fly to: ", get_common_destinations())
print("Destinations unique to your airline: ", get_your_unique_destinations())
print("Destinations that neither airline shares: ", get_unshared_destinations())
