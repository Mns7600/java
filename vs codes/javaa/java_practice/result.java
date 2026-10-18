class name{
    name(String n){
        System.out.println("Name: " + n);
    }
}
class roll extends name{
    roll(String n, int r){
        super(n);
        System.out.print("Roll: " + r);
    }
}

class cgpa extends roll{
    cgpa(String n, int r, float c){
        super(n,r);
        System.out.println("CGPA: "+ c);
    }
}

public class result{
    public static void main(String args[]){
        cgpa c = new cgpa("Jay", 5, 9.0f);
    }
}