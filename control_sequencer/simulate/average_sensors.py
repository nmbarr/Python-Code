def average_2oo3(sensor_values):
    """
    Performs 2oo3 voting logic on three sensor values.

    Args:
        sensor_values (list of float): List of 3 sensor values

    Returns:
        float: Average of the two closest sensor values
    """
    if len(sensor_values) != 3:
        raise ValueError("2oo3 voting requires exactly 3 sensor values")

    a, b, c = sensor_values

    # Calculate pairwise differences
    ab = abs(a - b)
    ac = abs(a - c)
    bc = abs(b - c)

    # Find the pair with the smallest difference
    if ab <= ac and ab <= bc:
        return (a + b) / 2
    elif ac <= ab and ac <= bc:
        return (a + c) / 2
    else:
        return (b + c) / 2
