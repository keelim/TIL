package design_pattern.adapter;

public class APlayerImpl implements APlayer {
    @Override
    public void play(String fileName) {
        System.out.println(": " + fileName);
    }

    @Override
    public void stop() {

    }
}
