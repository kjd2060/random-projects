/*
 * quick pass at this.  this will work but make sure to seperate the main function into its own class/file (Main.java) 
 * and the DataClass into its own file (DataClass.java)
*/

// this class should be its own file...eg DataClass.java
public class DataClass{ // was there a class name?
    double rate10 = 0; // correct variable names?
    double rate5 = 0;

    // not setting variables with instantiation?
    public DataClass(){
        rate10 = 10.00;
        rate5 = 5.00;
        displayRates(); // print the things
    }

    private void displayRates(){
        // should this loop?
        System.out.println("rate10: " + rate10 + ", rate5: " + rate5);
    }

    // you should seperate this out into its own file; e.g. Main.java
    public static void main(String[] args){
        DataClass temp = new DataClass(); // should start printing immediately
    }
}
