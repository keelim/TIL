package design_pattern.bridge;

public class Clean extends IAction{
    public Clean(IRobot robot) {
        super(robot);
    }

    public void doClean(){
        System.out.println("청소를 합니다.");
    }
}
