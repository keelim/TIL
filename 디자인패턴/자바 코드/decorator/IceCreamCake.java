package design_pattern.decorator;

public class IceCreamCake extends IceCream {

    public IceCreamCake() {
        this.description = "콘";
    }

    @Override
    public int price() {
        return 1500;
    }
}
