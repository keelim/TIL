package design_pattern.singleton;

public class TestPattern2 {
    static int nNum = 0;

    Runnable task = new Runnable() {
        @Override
        public void run() {
            try {
                nNum++;
                Database database = Database.getInstance(nNum + "첫번쨰");
            } catch (Exception e) {
                e.printStackTrace();
            }
            for(int i=0; i<10; i++){
                Thread time = new Thread(task);
                time.n();
            }
        }

    };



}
