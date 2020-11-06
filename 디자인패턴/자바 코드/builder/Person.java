package design_pattern.builder;

import java.time.LocalDate;

public class person {
    private String firstName;
    private String lastName;
    private LocalDate birthDate;
    private String addressOne;
    private String addressTwo;
    private String male_female;
    private boolean driverLicence;
    private boolean married;

    //
    public String getFirstName() {
        return firstName;
    }

    public void setFirstName(String firstName) {
        this.firstName = firstName;
    }

    public String getLastName() {
        return lastName;
    }

    public void setLastName(String lastName) {
        this.lastName = lastName;
    }

    public LocalDate getBirthDate() {
        return birthDate;
    }

    public void setBirthDate(LocalDate birthDate) {
        this.birthDate = birthDate;
    }

    public String getAddressOne() {
        return addressOne;
    }

    public void setAddressOne(String addressOne) {
        this.addressOne = addressOne;
    }

    public String getAddressTwo() {
        return addressTwo;
    }

    public void setAddressTwo(String addressTwo) {
        this.addressTwo = addressTwo;
    }

    public String getMale_female() {
        return male_female;
    }

    public void setMale_female(String male_female) {
        this.male_female = male_female;
    }

    public boolean isDriverLicence() {
        return driverLicence;
    }

    public void setDriverLicence(boolean driverLicence) {
        this.driverLicence = driverLicence;
    }

    public boolean isMarried() {
        return married;
    }

    public void setMarried(boolean married) {
        this.married = married;
    }

    public static PersonBuilder personBuilder(){
        return new PersonBuilder();
    }

}
