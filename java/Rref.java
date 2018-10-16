import java.lang.Math;

class Rref{
    public static void main(String[] args) {
        double[][] a = {{1,3,1,9},{1,1,-1,1},{3,11,5,35}};
        printMatrix(a);
        double[][] aRref = rref(a);
        printMatrix(aRref);
    }

    // calculate and return the row reduced echelon form of a matrix
    // the double[][] array should have rows as primary elements
    public static double[][] rref(double[][] matrix){
        int m = matrix.length;
        int n = matrix[0].length;
        int minDim = (m < n) ? m : n;
        int i_max = 0;
        double[] temp = matrix[0];
        double f = 0;

        // transforming the matrix to row echelon form by handling each pivot column k seperately
        for (int k = 0; k < minDim; k ++){
            i_max = k;
            for (int i = k; i < m; i ++){                
                if (matrix[i][k] > Math.abs(matrix[i_max][k])){
                    i_max = i;
                }
            }

            if (matrix[i_max][k] == 0){
                System.out.println("Matrix is singular!");
            }
            temp = matrix[k];
            matrix[k] = matrix[i_max];
            matrix[i_max] = temp;
            System.out.println("switching rows for pivot " + k);
            printMatrix(matrix);
            
            for (int i = k+1; i < m; i++){
                f = matrix[i][k] / matrix[k][k];
                for (int j = k+1; j < n; j++){
                    matrix[i][j] = matrix[i][j] - matrix[k][j] * f;
                }
                matrix[i][k] = 0;
            }

            System.out.println("reduced for pivot " + k);
            printMatrix(matrix);
        }

        // transforming the ref to reduced ref
        //for (int k = 0; k < )

        return matrix;
    }

    // multiply a row by a constant
    public static double[] rowMultiply(double[] row, double k){
        if (k==0){
            System.out.println("Warning: you multplied by zero");
        }
        for (int i = 0; i < row.length; i++){
            row[i] = row[i] * k;
        }
        return row;
    }

    // adding one row to another
    public static double[] rowAddition(double[] row1, double[] row2){
        for (int i = 0; i < row1.length; i++){
            row1[i] = row1[i] + row2[i];
        }
        return row1;
    }

    // printing a matrix
    public static void printMatrix(double[][] matrix){
        System.out.println("Printing a " + (matrix[0].length) + " by " + (matrix.length) + " matrix:");
        for (int i = 0; i < matrix.length; i ++){
            for (int j = 0; j < matrix[0].length; j ++){
                System.out.printf(" %2.0f ", matrix[i][j]);
            }
            System.out.println("");
        }
        System.out.println("");
    }
}