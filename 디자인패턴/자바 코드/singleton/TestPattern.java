package design_pattern.singleton;

public class TestPattern {
    public static void main(String[] args) {
        Database database;

        database = Database.getInstance("첫번쨰 데이터 베이스");
        System.out.println("This is the " +database.getName() + "!!");

        database = Database.getInstance("첫번쨰 데이터 베이스!!!!!");
        System.out.println("This is the " +database.getName() + "!!");


    }
}