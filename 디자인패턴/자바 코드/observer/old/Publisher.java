package design_pattern.observer.old;



public interface Publisher {

    public void addObserver(Observer o);
    public void deleteObserver(Observer o);
    public void notifyObserver();
}
