package design_pattern.builder;

public class TestPattern1 {
    public static void main(String[] args) {
        person p1 = createPersonForTesting();
        System.out.println(p1.getFirstName());
        person p2 = person.personBuilder()
                .FirstName("sdsd")
                .AddressOne("aaa")
                .LastName("sdsd")
                .Married(true)
                .AddressTwo("2323")
                .DriverLicence(true)
                .Male_female("male")
                .build();

    }

    public static person createPersonForTesting() { //기존 getter, setter
        person person = new person();
        person.setFirstName("FirstName");
        person.setLastName("LastName");
        person.setAddressOne("Address1");
        person.setAddressTwo("Address2");
        person.setMale_female("male");
        person.setDriverLicence(false);
        person.setMarried(true);

        return person;
    }
}





