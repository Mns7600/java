public class moverload {
    void area(float r){
        float area = 3.14f*r*r;
        System.out.println("The area of circle is "+ area);
    }
    void area (float x, float y){
        float area = 0.5f*x*y;
        System.out.println("The area of triangle is " + area);
    }
    void area(int a, int b){
        int area = a*b;
        System.out.println("The area of rectangle is " + area);
    }

    public static void main(System args[]){
        moverload m = new moverload();
        m.area(3.5f);
        m.area(3.5f,4.5f);
        m.area(3,4);        
    }
}
