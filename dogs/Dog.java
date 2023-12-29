package dogs;

public class Dog {
    public int wieght;

    public static String  name = "aaaa";

    public Dog(int w){
        wieght = w;
    }


    public void makeNoise() {
        if (wieght < 10){
            System.out.println("yip!!!");
        } else if (wieght < 30){
            System.out.println("Bark!!");
        } else{
            System.out.println("woof!!");
        }

    }

    public static Dog maxDog(Dog d1, Dog d2){
        if(d1.wieght > d2.wieght){
            return d1;
        }
        return d2;
    }

    public Dog maxDog(Dog d){
        if(this.wieght > d.wieght){
            return this;
        }
        return d;
    }
    
}
