package design_pattern.decorator;

public class Strawberry extends decorator {
    IceCream iceCream;

    public Strawberry(IceCream iceCream) {
        this.iceCream = iceCream;
    }

    @Override
    public String getDescription() {
        return iceCream.getDescription()+" 딸기";
    }

    @Override
    public int price() {
        return 2200;
    }
}
