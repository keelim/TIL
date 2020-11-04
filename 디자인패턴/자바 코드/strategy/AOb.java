package design_pattern.strategy;

public class AOb {
    BInterface bInterface;

    public AOb() {
        bInterface = new BImplement();
    }

    public void SomeFunc(){
//        System.out.println("AA");
//        System.out.println("AAA");
        bInterface.funcA();
        bInterface.funcA();
    }
}
