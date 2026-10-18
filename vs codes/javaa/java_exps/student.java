public class student {
    String name;
    int age;

    student(){
        name = "mango";
        age = 12;
    }
    student(String name){
        this.name = name;
        age = 14;
    }
    student(String name,int age){
        this.name = name;
        this.age = age;
    }
    void display(){
        System.out.println("Name: "+ name+ ", Age: "+age);
    }
    public static void main(String args[]){
        student s1 = new student();
        s1.display();
        student s2 = new student("Leeche");
        s2.display();
        student s3 = new student("banana",16);
        s3.display();
    }
}
