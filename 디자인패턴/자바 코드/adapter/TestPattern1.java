package design_pattern.adapter;

public class TestPattern1 {
    public static void main(String[] args) {
        APlayer player1 = new APlayerImpl();
        player1.play("aaa.mp3");

        //APlayerImpl을 사용 못함

        //BPlayer

    }
}
