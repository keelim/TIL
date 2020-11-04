package design_pattern.facade;

public class Computer {
    private boolean turnOn = false;

    public void turnOn(){
        turnOn = true;
        System.out.println("Computer on");
    }

    public void turnOff(){
        turnOn = false;
        System.out.println("Computer off");
    }

    public boolean isTurnOn(){
        return turnOn;
    }

}
