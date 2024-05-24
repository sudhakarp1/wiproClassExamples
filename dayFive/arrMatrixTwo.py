#[4:15 PM] Satyam Singh (Unverified)
def create_matrix(rows, columns, start):
    return [[start + col + row * columns for col in range(columns)] for row in range(rows)]
 
def addMatrix(a, b):
    if len(a) != len(b) or len(a[0]) != len(b[0]):
        raise ValueError("Matrices must have the same dimensions to be added.")
    return [[a[i][j] + b[i][j] for j in range(len(a[0]))] for i in range(len(a))]
 
def subMatrix(a, b):
    if len(a) != len(b) or len(a[0]) != len(b[0]):
        raise ValueError("Matrices must have the same dimensions to be subtracted.")
    return [[a[i][j] - b[i][j] for j in range(len(a[0]))] for i in range(len(a))]
 
def mulMatrix(a, b):
    try:
        if len(a[0]) != len(b):
            raise ValueError("Number of columns in the first matrix must be equal to the number of rows in the second matrix for multiplication.")
        
        return [[sum(a[i][k] * b[k][j] for k in range(len(a[0]))) for j in range(len(b[0]))] for i in range(len(a))]
    except ValueError as e:
        print(e)

    return [[]]
if __name__ == '__main__': 
    rows_a = int(input("Enter the number of rows for matrix A: "))
    columns_a = int(input("Enter the number of columns for matrix A: "))
    start_a = int(input("Enter the starting value for matrix A: "))
    matrix_a = create_matrix(rows_a, columns_a, start_a)
    
    rows_b = int(input("Enter the number of rows for matrix B: "))
    columns_b = int(input("Enter the number of columns for matrix B: "))
    start_b = int(input("Enter the starting value for matrix B: "))
    matrix_b = create_matrix(rows_b, columns_b, start_b)
    
    print("Matrix A:")
    for row in matrix_a:
        print(row)
    
    print("Matrix B:")
    for row in matrix_b:
        print(row)
    
    
        # Perform matrix addition
    addition_result = addMatrix(matrix_a, matrix_b)
    print("\nMatrix Addition Result:")
    for row in addition_result:
        print(row)
    
    # Perform matrix subtraction
    subtraction_result = subMatrix(matrix_a, matrix_b)
    print("\nMatrix Subtraction Result:")
    for row in subtraction_result:
        print(row)
    
    # Perform matrix multiplication
    multiplication_result = mulMatrix(matrix_a, matrix_b)
    print("\nMatrix Multiplication Result:")
    for row in multiplication_result:
        print(row)
    
    
    