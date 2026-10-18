// Multiple Inheritance

interface University{
    default void uni(String u){
        System.out.println("University: " + u);
    }
}

interface college{
    default void clg(String c){
        System.out.println("College: "+ c);
    }
}

interface department{
    default void depart(String d){
        System.out.println("Department: " + d);
    }
}

class candidate implements University, college, department{
    void user(String n, int erp){
        System.out.println("Candidate Name: " + n);
        System.out.println("Enrolment No: " + erp);
    }
}

public class profile{
    public static void main(String args[]){
        candidate c = new candidate();
        c.uni("Mumbai University");
        c.clg("LTCE");
        c.depart("DS");
        c.user("Raj", 2567);

    }
}