package design_pattern.singleton;

public class TestPattern4 {
    public static void main(String[] args) {
        for (int i = 0; i < 50; i++) {
            Thread time = new ThreadSub(i);
            time.n();
        }
    }
}

class ThreadSub extends Thread{
    int mapp;

    public ThreadSub(int mapp) {
        this.mapp = mapp;
    }

    @Override
    public void run() {
        LogWriter logger = LogWriter.getInstance();
        if(mapp <10)
            logger.log("*** 0"  + mapp + "***");
        else
            logger.log("***" + mapp + "***");
    }
}
