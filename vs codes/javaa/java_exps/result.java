class name{
    name(String n){
        System.out.println("Name of student: "+ n);
    }
}
class roll_no extends name{
    roll_no(String n, int r){
        super(n);
        System.out.println("Roll number: "+ r);
    }
}
class CGPA extends roll_no{
    CGPA(String n, int r, float c){
        super(n,r);
        System.out.println("CGPA: "+c);
    }
}
class result{
    public static void main(String args[]){
        // name n = new name("Manas");
        // System.out.println();
        // roll_no r = new roll_no("Manas", 18);
        // System.out.println();
        CGPA c = new CGPA("Jay", 21, 9.52f);

}
}