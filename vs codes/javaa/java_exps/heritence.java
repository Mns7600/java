
class Vehicle {
    void start() {
        System.out.println("Vehicle is starting...");
    }

    void stop() {
        System.out.println("Vehicle is stopping...");
    }
}

class Car extends Vehicle {
    void honk() {
        System.out.println("Car is honking");
    }
}

class Sportscar extends Car {
    void turboboost() {
        System.out.println("Sports car is using turbo boost...");
    }
}

public class heritence {
    public static void main(String[] args) {
        Sportscar mySportscar = new Sportscar();

        mySportscar.start();
        mySportscar.honk();
        mySportscar.turboboost();
        mySportscar.stop();
    }
}
