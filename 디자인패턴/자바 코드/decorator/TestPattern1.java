package design_pattern.decorator;

public class TestPattern1 {
    public static void main(String[] args) {
        IceCream iceCream = new IceCreamCake();

        System.out.println(iceCream.getDescription() + "cost" +iceCream.price());

        IceCream iceCream2 = new Strawberry(new IceCreamCake());
        System.out.println(iceCream2.getDescription()+"cost"+iceCream2.price());
    }
}

