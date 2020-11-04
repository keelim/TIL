package design_pattern.singleton;

public class TestPattern3 {
    public static void main(String[] args) {
        LogWriter logger;

        logger = LogWriter.getInstance();
        logger.log("김재현");
        logger.log("김재현");
        logger.log("김재현");
        logger.log("김재현");
        logger.log("전우치");


    }
}
