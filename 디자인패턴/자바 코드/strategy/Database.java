package design_pattern.strategy;

public abstract class Database {
    public String name;
    public double rows;

    public abstract void connectDatabase();

    public void insertData(){
        System.out.println(name+"추가");
    }

    public void selectData(){
        System.out.println(name+"데이터를"+rows+"조회합니다.");
    }
}
