package design_pattern.singleton;

public class Database{
    //dao의 기능을 하는 것을 만든다,
    private static Database singleton = new Database("product");
    private String name;

    private Database(String name){
        super();
        try {
            Thread.sleep(100);
            this.name = name;
        } catch (InterruptedException e) {
            e.printStackTrace();
        }

    }

    public synchronized static Database getInstance(String name){
        if(singleton == null){ //static 이라서 가능한 부분
            singleton = new Database(name);
        }
        return singleton;
    }

    public String getName(){
        return name;
    }
}