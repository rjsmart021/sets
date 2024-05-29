from typing import List


def remove_duplicate_customer_ids(customer_ids: List[str]) -> set[str]:
    """

    :param customer_ids: list of customer ID's
    :return: set of unique customer ID's
    """

    unique_customer_ids = set()

    for customer_id in customer_ids:
        if customer_id not in unique_customer_ids:
            print(customer_id)
            unique_customer_ids.add(customer_id)

    return unique_customer_ids


customer_ids = ["C001", "C002", "C003", "C002", "C001", "C004"]
unique_customer_ids = remove_duplicate_customer_ids(customer_ids)

