package design_pattern.builder;

import java.time.LocalDate;

public class PersonBuilder { //기본적인
    private String firstName;
    private String lastName;
    private LocalDate birthDate;
    private String addressOne;
    private String addressTwo;
    private String male_female;
    private boolean driverLicence;
    private boolean married;

    public PersonBuilder FirstName(String firstName) {
        this.firstName = firstName;
        return this;
    }

    public PersonBuilder LastName(String lastName) {
        this.lastName = lastName;
        return this;
    }

    public PersonBuilder BirthDate(LocalDate birthDate) {
        this.birthDate = birthDate;
        return this;
    }

    public PersonBuilder AddressOne(String addressOne) {
        this.addressOne = addressOne;
        return this;
    }

    public PersonBuilder AddressTwo(String addressTwo) {
        this.addressTwo = addressTwo;
        return this;
    }

    public PersonBuilder Male_female(String male_female) {
        this.male_female = male_female;
        return this;
    }

    public PersonBuilder DriverLicence(boolean driverLicence) {
        this.driverLicence = driverLicence;
        return this;
    }

    public PersonBuilder Married(boolean married) {
        this.married = married;
        return this;
    }

    public person build(){
        person person = new person();
        person.setFirstName(this.firstName);
        person.setLastName(this.lastName);
        person.setAddressOne(this.addressOne);
        person.setAddressTwo(this.addressTwo);
        person.setMale_female(this.male_female);
        person.setDriverLicence(this.driverLicence);
        person.setMarried(this.married);
        return person;
    }
}

