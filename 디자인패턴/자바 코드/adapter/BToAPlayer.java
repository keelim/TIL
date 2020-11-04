package design_pattern.adapter;

public class BToAPlayer implements APlayer{
    private BToAPlayer media;

    public BToAPlayer(BToAPlayer media) {
        this.media = media;
    }

    @Override
    public void play(String fileName) {

    }

    @Override
    public void stop() {

    }
}
