#!/usr/bin/python3
"""
Module for Pascal's Triangle generation
"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing
    the Pascal's triangle of n.
    
    Args:
        n (int): Number of rows to generate
        
    Returns:
        list: Empty list if n <= 0, otherwise a list of lists
              representing Pascal's triangle
    """
    if n <= 0:
        return []
        
    # Initialize triangle with first row
    triangle = [[1]]
    
    # Generate each row based on the previous row
    for i in range(1, n):
        # Start the row with 1
        row = [1]
        
        # Calculate middle elements using previous row
        prev_row = triangle[i-1]
        for j in range(1, i):
            row.append(prev_row[j-1] + prev_row[j])
            
        # End the row with 1
        row.append(1)
        
        # Add the row to the triangle
        triangle.append(row)
        
    return triangle
