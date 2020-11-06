package design_pattern.strategy;

public class TestPattern2 {
    public static void main(String[] args) {
        DatabaseUse myDb = new DatabaseUse();

        myDb.connect(DBTYPE.mysql);
        myDb.go();
    }
}
