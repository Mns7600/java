interface CollegeData {
    void collegeDetail();

    default void studentData() {
        System.out.println("Courses of Student: MCA, MTECH, MBA, BCA");
    }
}

interface HostelData {
    void hostelDetail();

    default void studentData() {
        System.out.println("Student selected based on: Percentage, Financial condition");
    }
}

public class StudentRecord implements CollegeData, HostelData {

    @Override
    public void hostelDetail() {
        System.out.println("Hostel Name: LICF Hostel");
        System.out.println("Hostel Location: Koparkhairne");
    }

    @Override
    public void collegeDetail() {
        System.out.println("College Name: LTCE");
        System.out.println("College Grade: A");
        System.out.println("University of College: Mumbai");
    }

    @Override
    public void studentData() {
        // Resolving the default method ambiguity (diamond problem)
        CollegeData.super.studentData();
        HostelData.super.studentData();
    }

    public static void main(String[] args) {
        StudentRecord obj = new StudentRecord();

        obj.collegeDetail();
        obj.hostelDetail();
        obj.studentData();
    }
}