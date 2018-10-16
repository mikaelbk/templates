class Test{
    public static void main(String[] args){
        Matrix column = new Matrix(new double[][]{{2,3},{4,5}});
        column.print();

        Matrix row = new Matrix(new double[][]{{1,2},{3,4}});
        row.print();

        Matrix a = column.times(row);
        a.print();
    }
}