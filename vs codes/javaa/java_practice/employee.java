public class employee{
    int id;
    String name;
    float salary;

    void insert(int i, String n, float s){
        id = i;
        name = n;
        salary = s;
    }
    void display(){
        System.out.println(id + " " + name + " " + salary);
    }

    public static void main(String args[]){
        employee e1 = new employee();
        employee e2 = new employee();

        e1.insert(5,"Manas", 5000);
        e2.insert(7,"zareen", 6000);
        e1.display();
        e2.display();
    }
}