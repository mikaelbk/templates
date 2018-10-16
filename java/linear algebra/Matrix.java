import java.util.ArrayList;

class Matrix{
    public double[][] matrix;
    public int m;
    public int n;
    private double tol = 0.0001;

    Matrix(double[][] matrix){
        for(int i = 1; i < matrix.length; i++){
            if(matrix[i].length != matrix[i-1].length){
                throw new IllegalArgumentException("Columns needs to be of equal size");
            }
        }
        this.matrix = matrix;
        this.m = matrix.length;
        this.n = (matrix[0]).length;
    }

    public void print(){
        System.out.println("Printing a " + m + "x" + n + " matrix");
        for(int i = 0; i < m; i++){
            for(int j = 0; j < n; j++){
                System.out.printf("%.0f\t", matrix[i][j]);
            }
            System.out.println("");
        }
        System.out.println();
    }

    public Matrix times(Matrix b){
        if(n != b.m){
            throw new IllegalArgumentException("Can not multiply with a matrix whose number of rows does not equal this matrix' number columns");
        }
        double[][] product = new double[m][b.n];
        for(int i = 0; i < m; i++){
            for(int j = 0; j < b.n; j++){
                for(int k = 0; k < n; k++){
                    product[i][j] += matrix[i][k] * b.matrix[k][j];
                }
            }
        }
        return new Matrix(product);
    }
}