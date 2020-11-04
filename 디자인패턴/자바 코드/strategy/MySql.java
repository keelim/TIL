package design_pattern.strategy;

public class MySql extends Database{
    public MySql() {
        name = "MySql";
        rows = 20;

    }

    @Override
    public void connectDatabase() {
        System.out.println(name+"에 접속");
    }
}
