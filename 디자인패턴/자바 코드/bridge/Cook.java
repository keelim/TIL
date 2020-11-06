package design_pattern.bridge;

public class Cook extends IAction {
    public Cook(IRobot robot) {
        super(robot);
    }

    public void doCook(){
        System.out.println("doing Cook");
    }
}
