def translation(inp):
    from web_app_tool import final_step
    vector, matrix = final_step(inp)
    def VM_multiplication(vector, matrix):
        for element in range(len(vector)):
            try:
                for collum in range(len(matrix[element])):
                    matrix[element][collum] = matrix[element][collum] * vector[element]
            except IndexError:
                ""

        for new in range(len(vector)):
            vector[new] = 0
            try:
                for col in range(len(matrix)):
                    vector[new] += matrix[col][new]
            except IndexError:
                ""

        return vector

    return VM_multiplication(vector, matrix)

