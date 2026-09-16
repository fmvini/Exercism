EXPECTED_BAKE_TIME = 40


def bake_time_remaining(elapsed_bake_time):
    """Calculate the remaining baking time.

    Parameters:
        elapsed_bake_time (int): Time the lasagna has already been baking.

    Returns:
        int: The remaining baking time in minutes.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(number_of_layers):
    """Calculate the preparation time based on the number of layers.

    Parameters:
        number_of_layers (int): The number of layers in the lasagna.

    Returns:
        int: The preparation time in minutes.
    """
    return 2 * number_of_layers


def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the total elapsed cooking time.

    Parameters:
        number_of_layers (int): The number of layers in the lasagna.
        elapsed_bake_time (int): Time the lasagna has already been baking.

    Returns:
        int: The total time spent preparing and baking the lasagna.
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time