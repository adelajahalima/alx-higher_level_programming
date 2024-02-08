scal_traigle module."""


def pascal_triangle(n):
    """ pascal traigle class body.
    """
    if n <= 0:
        return []

    triangles = [[1]]
    while len(triangles) != n:
        tri = triangles[-1]
        tmp = [1]
        for w in range(len(tri) - 1):
            tmp.append(tri[w] + tri[w + 1])
        tmp.append(1)
        triangles.append(tmp)
    return
