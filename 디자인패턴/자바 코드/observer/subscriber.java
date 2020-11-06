package design_pattern.observer;


import java.util.Observable;
import java.util.Observer;

public class subscriber implements Observer {
    private subject subject;
    public subscriber(subject sub) {
        subject = sub;
        subject.addObserver(this);

    }

    @Override
    public void update(Observable o, Object arg) {
        System.out.println("메소드 호출됨");
    }
}
