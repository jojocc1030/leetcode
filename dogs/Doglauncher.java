package dogs;


public class Doglauncher {
    public static void main(String[] args) {
        Dog d1 = new Dog(51);

        Dog d2 = new Dog(100);

        Dog biggerDog = Dog.maxDog(d1, d2); //call by class name , static

        biggerDog.makeNoise();

        Dog may = new Dog(20);

        biggerDog = may.maxDog(d1); // call by instance name, non static

        biggerDog.makeNoise();

        System.out.println(Dog.name);
    }
}
