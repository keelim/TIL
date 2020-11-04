package design_pattern.strategy;

enum DBTYPE {mysql, informix}
public class DatabaseUse {
    Database db;

    public void connect(DBTYPE dbtype){
        switch ((dbtype)){
            case mysql:
                db = new MySql();
                break;
            case informix:
                db = new Informix();
                break;

        }
        if (db==null){
            System.out.println("error");
        } else{
            db.connectDatabase();
        }
    }

    public void go(){
        db.selectData();
    }
}
