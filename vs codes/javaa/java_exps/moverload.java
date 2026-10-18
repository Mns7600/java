class moverload {
    void area(float r){
        float area = 3.14f*r*r;
        System.out.println("The area of circle is "+ area );
    }
    void area(int a , int b){
        int area = a*b;
        System.out.println("The area of rectangle is " + area);
    }
    void area(int x){
        int area = x*x;
        System.out.println("The area of square is "+ area);
    }
    void area(float l, float h){
        float area = 0.5f*l*h;
        System.out.println("The area of triangle is "+ area);
    }
    public  static  void main(String args[]){
        moverload mo = new moverload();
        mo.area(3f);
        mo.area(2,3);
        mo.area(4);
        mo.area(4f,5f);
    }
}
