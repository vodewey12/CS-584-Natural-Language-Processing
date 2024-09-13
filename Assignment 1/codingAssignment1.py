"""
Aaron Vo
CS-584 Assignment 1
September 13, 2024

Write a Python program that will read a NxN matrix A and an NxN matrix B from an input file and outputs the NxN 
matrix product to C. N can be of any size >= 2. The output should display on the terminal screen.

"""

import numpy as np

"""
Input: file name
Output: the dot product of the two matrixes as a numpy array
"""
def matrix_product(filename: str) -> np.array:
    matrixes = []
    with open(filename, 'r') as file:
        lines = file.readlines()
        lineIndex = 0
        
        while (lineIndex < len(lines)):
            # Set the matrixes size
            lineArr = lines[lineIndex].split(" ")
            m = int(lineArr[0])
            n = int(lineArr[1])
            matrix = np.zeros((m, n))
            nextLine = 0
            
            # Interate the next line given the matrix's size
            while (nextLine < m):   
                nextLine += 1
                currArr = lines[lineIndex + nextLine].split(" ")
                
                # Set the matrix's vales
                for i in range(len(currArr)):
                    matrix[nextLine-1][i] = int(currArr[i])
            
            # Append the completed matrix to the matrix array
            matrixes.append(matrix)
            
            # Add the current line on file to the next line where the matrix size is set
            lineIndex += nextLine+1

    return np.dot(matrixes[0], matrixes[1])


if __name__ == '__main__':
    print(matrix_product('A1data.txt'))