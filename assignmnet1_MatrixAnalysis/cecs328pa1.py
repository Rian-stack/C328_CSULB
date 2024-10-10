def isValidGrid(matrix):
    n = len(matrix)

    # rows
    for i in range(n):
        if len(matrix[i]) > len(set(matrix[i])):
            return False

    # columns
    for i in range(n):
        column = []
        for j in range(n):
            column.append(matrix[j][i])
        if len(column) > len(set(column)):
            return False

    # quadrants
    h = len(matrix)
    w = len(matrix[0])  # Changed from matrix[1] to matrix[0] to avoid potential index errors.

    top_left = [item for sublist in [matrix[i][:w // 2] for i in range(h // 2)] for item in sublist]
    top_right = [item for sublist in [matrix[i][w // 2:] for i in range(h // 2)] for item in sublist]
    bot_left = [item for sublist in [matrix[i][:w // 2] for i in range(h // 2, h)] for item in sublist]
    bot_right = [item for sublist in [matrix[i][w // 2:] for i in range(h // 2, h)] for item in sublist]

    quadrants = [top_left, top_right, bot_left, bot_right]

    for q in quadrants:
        if len(q) > len(set(q)):
            return False

    return True