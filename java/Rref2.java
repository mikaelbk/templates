import java.lang.Math;

class Rref2{
    public static void main(String[] args) {
        double[][] a = {{-1,0,1,0.5},{1/3.0,-1,0,0},{1/3.0,1/2.0,-1,1/2.0},{1/3.0,1/2.0,0,-1}};
        double[][] aRref = rref(a,true);
    }

    // calculate and return the row reduced echelon form of a matrix
    // the double[][] array should have rows as primary elements
    public static double[][] rref(double[][] matrix, boolean withSteps){
        int m = matrix.length;
        int n = matrix[0].length;
        //int minDim = (m < n) ? m : n;
        int i_max = 0;
        double[] temp = matrix[0];
        double f = 0;

        if (withSteps){
            System.out.println("original matrix");
            printMatrix(matrix);
        }
        
        // transforming the matrix to row echelon form by handling each pivot column k seperately
        for (int k = 0; k < m && k < n ; k ++){
            i_max = k;
            for (int i = k; i < m ; i ++){                
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
            //System.out.println("switching rows for pivot " + k);
            //printMatrix(matrix);
            
            for (int i = k+1; i < m; i++){
                f = matrix[i][k] / matrix[k][k];
                //System.out.println(f);
                for (int j = k+1; j < n; j++){
                    matrix[i][j] = matrix[i][j] - matrix[k][j] * f;
                }
                matrix[i][k] = 0;
            }

            // System.out.println("reduced for pivot " + k);
            //printMatrix(matrix);
        }

        if (withSteps){
            System.out.println("ref");
            printMatrix(matrix);
        }

        // transforming the ref to reduced ref
        for ( int k = m-1; k > -1; k--){
            for (int i = 0; i < n; i ++){
                if (matrix[k][i] != 0){
                    matrix[k] = rowMultiply(matrix[k],1/matrix[k][i]);
                    if (k == 0){
                        break;
                    }
                        
                    for (int j = k-1; j > -1; j--){
                        matrix[j] = rowAddition(matrix[j],rowMultiply(matrix[k],-1*matrix[j][i]));
                    }
                    break;
                }
            }
        }
        
        if (withSteps){
            System.out.println("rref");
            printMatrix(matrix);
        }

        return matrix;
    }

    // multiply a row by a constant
    public static double[] rowMultiply(double[] row, double k){
        double[] temp = new double[row.length];
        if (k==0){
            System.out.println("Warning: you multiplied by zero");
        }
        for (int i = 0; i < row.length; i++){
            temp[i] = row[i] * k;
        }
        return temp;
    }

    // adding one row to another
    public static double[] rowAddition(double[] row1, double[] row2){
        double[] temp = new double[row1.length];
        for (int i = 0; i < row1.length; i++){
            temp[i] = row1[i] + row2[i];
        }
        return temp;
    }

    // printing a matrix
    public static void printMatrix(double[][] matrix){
        //System.out.println("Printing a " + (matrix[0].length) + " by " + (matrix.length) + " matrix:");
        for (int i = 0; i < matrix.length; i ++){
            for (int j = 0; j < matrix[0].length; j ++){
                System.out.printf(" %5.2f ", matrix[i][j]);
            }
            System.out.println("");
        }
        System.out.println("");
    }
}
