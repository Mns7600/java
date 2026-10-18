public class student {
    String name;
    int age;

    student(){
        name = "Bot";
        age = 5;
    }
    student(String name){
        this.name = name;
        age = 14;
    }
    student(String name, int age){
        this.name = name;
        this.age = age;
    }

    void display (){
        System.out.println(name + " " + age);
    }

    public static void main(String args[]){
        student s1 = new student();
        student s2 = new student("Manas");
        student s3 = new student("Zareen", 20);

        s1.display();
        s2.display();
        s3.display();

    }
}
