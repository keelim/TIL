package design_pattern.bridge;

public class RobotModel1 implements  IRobot{
    @Override
    public void powerOn() {
        System.out.println("type1: power on");
    }

    @Override
    public void powerOff() {
        System.out.println("type1: power off");
    }


}
