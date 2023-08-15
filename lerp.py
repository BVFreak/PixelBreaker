def lerp(a: float, b: float, t: float) -> float:
    """Performs linear interpolation between two values.

    Linear interpolation, commonly known as lerp, calculates a smooth transition between
    a starting value `a` and an ending value `b` based on an interpolation factor `t`.
    The function returns an interpolated value that lies between `a` and `b`.

    The interpolation factor `t` determines the position of the interpolated value
    along the line connecting `a` and `b`. When `t` is 0, the function returns `a`,
    indicating the starting value. When `t` is 1, the function returns `b`,
    indicating the ending value. Values of `t` between 0 and 1 produce intermediate
    values that smoothly transition between `a` and `b` in a linear fashion.

    Args:
        a: The starting value.
        b: The ending value.
        t: The interpolation factor. Should be a value between 0 and 1.

    Returns:
        The interpolated value between `a` and `b` based on the interpolation factor `t`.

    Raises:
        TypeError: If `a`, `b`, or `t` is not a numeric value.
        ValueError: If `t` is not within the valid range of 0 to 1.

    Examples:
        >>> lerp(0, 10, 0.5)
        5.0
        >>> lerp(5, 15, 0.25)
        7.5
        >>> lerp(100, 200, 1)
        200.0
    """
    if not isinstance(a, (int, float)):
        raise TypeError("The starting value 'a' must be a numeric value.")
    if not isinstance(b, (int, float)):
        raise TypeError("The ending value 'b' must be a numeric value.")
    if not isinstance(t, (int, float)):
        raise TypeError("The interpolation factor 't' must be a numeric value.")
    if not 0 <= t <= 1:
        raise ValueError("The interpolation factor 't' must be between 0 and 1.")

    return (1 - t) * a + t * b