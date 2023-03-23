# Define the function to generate Pascal's triangle
def pascal_triangle(n):
    # Check if n is less than or equal to 0
    if n <= 0:
        # Return an empty list if n is less than or equal to 0
        return []

    # Create the initial list with one row and one element (which is always 1)
    triangle = [[1]]

    # Loop over the remaining rows, starting from the second row
    for i in range(1, n):
        # Create a new row with the first element set to 1
        row = [1]

        # Loop over the elements in the row,
        # excluding the first and last elements
        for j in range(1, i):
            # Calculate the value of each element by
            # adding the two elements above it in the previous row
            element = triangle[i-1][j-1] + triangle[i-1][j]
            # Append the calculated element to the current row
            row.append(element)

        # Append the last element (which is always 1) to the current row
        row.append(1)

        # Append the current row to the list of rows
        triangle.append(row)

    # Return the list of rows representing Pascal's triangle
    return triangle
