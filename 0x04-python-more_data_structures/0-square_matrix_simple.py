def square_matrix_simple(matrix=[]):
    def square(array):
        result = []
        for cell in array:
            result.append(cell ** 2)
        return result
    return list(map(square, matrix))
