def compute_slope(p1, p2):
    """Compute slope while handling vertical lines to avoid division by zero."""
    dx = p2[0] - p1[0]
    dy = p2[1] - p1[1]

    if dx == 0:
        return float('inf')
    return dy / dx
