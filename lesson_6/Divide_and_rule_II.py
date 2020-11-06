# Imagine you are a farmer and you own a piece of land. You want to divide your land into equal square parts.
# These parts should be as big as possible.


def split_farm_area(height, width):
    if height > width:
        parts = height % width
        if parts == 0:
            return tuple([width, width])
        else:
            height = parts
            return split_farm_area(height, width)
    else:
        parts = width % height
        if parts == 0:
            return tuple([height, height])
        else:
            width = parts
            return split_farm_area(height, width)


print(split_farm_area(981, 60))
