package design_pattern.observer.old;

public class MyClassA implements Observer{
    private boolean aPlay;
    @Override
    public void update(boolean play) {
        this.aPlay = play;
        myActControl();
    }

    private void myActControl() {
            if(aPlay)
                System.out.println("MyClassA 동작 실행");
            else
                System.out.println("MyClassA 동작 정지");
    }


}