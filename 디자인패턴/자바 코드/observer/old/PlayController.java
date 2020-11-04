package design_pattern.observer.old;

import java.util.Observable;

public class PlayController extends Observable { //Subject
    private boolean bPlay;

    public PlayController() {
    }

    //데이터를 전달 받아 플래그 값을 변경하고
    //새로운 데이터가 들어왔음을 알린다.
    public void setFlag(boolean bPlay){
        this.bPlay = bPlay;
        setChanged();
        notifyObservers();
    }

    public boolean getFlag(){
        return bPlay;
    }
}
