package design_pattern.bridge;

public class IAction {
    private IRobot robot;

    public IAction(IRobot robot) {
        this.robot = robot;
    }

    void powerOn(){
        robot.powerOn();
    }

    void powerOff(){
        robot.powerOff();
    }
}
