package design_pattern.flyweight;

import java.util.HashMap;
import java.util.Map;

public class FlyweightFactory {
    private static Map<String, Subject> mapp = new HashMap<>();

    public Subject getSubject(String key){
        Subject subject = mapp.get(key);
        if(subject == null){
            subject = new Subject(key);
            mapp.put(key, subject);
            System.out.println("새로 생성" + key);
        } else
            System.out.println("재사용" + key);
        return subject;
    }
}
