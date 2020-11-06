package design_pattern.flyweight;

public class TestPattern3 {
    public static void main(String[] args) {
        FlyweightFactory flyweightFactory = new FlyweightFactory();
        flyweightFactory.getSubject("mapp");
        flyweightFactory.getSubject("mapp");
        flyweightFactory.getSubject("n");
        flyweightFactory.getSubject("n");
    }
}
