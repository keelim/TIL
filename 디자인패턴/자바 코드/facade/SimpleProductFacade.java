package design_pattern.facade;

public class SimpleProductFacade {
    ComplexProduct difficultProduct;

    public SimpleProductFacade() {
        difficultProduct = new ComplexProduct();
    }

    public void setName(String n){
        char chars[] = n.toCharArray();

        if(chars.length>0)
            difficultProduct.namechar0(chars[0]);
        if(chars.length>1)
            difficultProduct.namechar0(chars[1]);
        if(chars.length>2)
            difficultProduct.namechar0(chars[2]);
        if(chars.length>3)
            difficultProduct.namechar0(chars[3]);
        if(chars.length>4)
            difficultProduct.namechar0(chars[4]);
        if(chars.length>5)
            difficultProduct.namechar0(chars[5]);
        if(chars.length>6)
            difficultProduct.namechar0(chars[6]);
        if(chars.length>7)
            difficultProduct.namechar0(chars[7]);
        if(chars.length>8)
            difficultProduct.namechar0(chars[9]);

    }


}
