package design_pattern.observer.old;

public class MyClassB implements Observer{
    private boolean bPlay;
    @Override
    public void update(boolean play) {
        this.bPlay = play;
        myActControl();
    }

    private void myActControl() {
            if(bPlay)
                System.out.println("MyClassb 동작 실행");
            else
                System.out.println("MyClassb 동작 정지");
    }


}