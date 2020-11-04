package design_pattern.observer.old;

import java.util.ArrayList;
import java.util.List;


public class PlayController2 implements Publisher {
    private List<Observer> observers = new ArrayList<>();
    private boolean play;
    @Override
    public void addObserver(Observer o) {
        observers.add(o);
    }

    @Override
    public void deleteObserver(Observer o) {
        int index = observers.indexOf(o);
        observers.remove(index);
    }

    @Override
    public void notifyObserver() {
        for(Observer observer : observers)
            observer.update(play);
    }

    public boolean isPlay() {
        return play;
    }

    public void setPlay(boolean play) {
        this.play = play;
        notifyObserver();
    }
}
