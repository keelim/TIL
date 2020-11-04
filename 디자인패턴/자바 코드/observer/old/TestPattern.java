package design_pattern.observer.old;

public class TestPattern {
    public static void main(String[] args) {
        PlayController2 pager = new PlayController2();
        Observer ob1 = new MyClassA();
        Observer ob2 = new MyClassB();

        pager.addObserver(ob1);
        pager.addObserver(ob2);

        pager.setPlay(false);

        pager.deleteObserver(ob1);

        System.out.println("- - - - - - - - - - ");

        pager.setPlay(false);


    }
}

