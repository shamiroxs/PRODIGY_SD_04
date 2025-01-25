import os
import cv2
import numpy as np

def is_valid(matrix, row, col, num):
    """
    Check if placing num at matrix[row][col] is valid.
    """
    for x in range(9):
        if matrix[row][x] == num or matrix[x][col] == num:
            return False
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if matrix[start_row + i][start_col + j] == num:
                return False
    return True


def solve_sudoku(matrix):
    """
    Solve the Sudoku using a backtracking algorithm.
    """
    for row in range(9):
        for col in range(9):
            if matrix[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(matrix, row, col, num):
                        matrix[row][col] = num
                        if solve_sudoku(matrix):
                            return True
                        matrix[row][col] = 0
                return False
    return True


def create_sudoku_image(matrix):
    """
    Generate an image of the solved Sudoku and save it.
    """
    output_path = "./output/output.png"
    
    img_size = 450
    cell_size = img_size // 9
    font_scale = 0.9
    thickness = 2
    font = cv2.FONT_HERSHEY_SIMPLEX

    image = np.ones((img_size, img_size, 3), dtype=np.uint8) * 255

    for i in range(10):
        line_thickness = 3 if i % 3 == 0 else 1
        cv2.line(image, (0, i * cell_size), (img_size, i * cell_size), (0, 0, 0), line_thickness)
        cv2.line(image, (i * cell_size, 0), (i * cell_size, img_size), (0, 0, 0), line_thickness)

    for row in range(9):
        for col in range(9):
            if matrix[row][col] != 0:
                text = str(matrix[row][col])
                text_size = cv2.getTextSize(text, font, font_scale, thickness)[0]
                text_x = col * cell_size + (cell_size - text_size[0]) // 2
                text_y = row * cell_size + (cell_size + text_size[1]) // 2
                cv2.putText(image, text, (text_x, text_y), font, font_scale, (0, 0, 0), thickness)

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    cv2.imwrite(output_path, image)


if __name__ == "__main__":
    sudoku_matrix = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9],
    ]

    if solve_sudoku(sudoku_matrix):
        
        create_sudoku_image(sudoku_matrix)
        print(f"Solved Sudoku saved at {output_path}")
    else:
        print("No solution exists for the given Sudoku.")

