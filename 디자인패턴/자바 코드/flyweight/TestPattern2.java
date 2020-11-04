package design_pattern.flyweight;

public class TestPattern2 {
    public static void main(String[] args) {
        Data d1 = new Data();
        d1.name = "keelim";
        d1.xpos = 10;
        d1.ypos = 11;

        Data d2 = new Data();
        d2.name = "keelim";
        d2.xpos = 10;
        d2.ypos = 11;


        Data d3 = new Data();
        d3.name = "keelim";
        d3.xpos = 10;
        d3.ypos = 11;

    }


}

class Data {
    int xpos;
    int ypos;
    String name;
}