 import java.util.Scanner;
import java.util.Scanner;
public class AdjustableCar
{
    private String make;
    private int year;
    private int speed;
    
    
    public void setMake(String carMake)
    {
        make = carMake;
    }
    
    public String getMake()
    {
         return make;
    }
    
    public void setYear(int newYear)
    {
         year = newYear;
    }  
    
    public int getYear()
    {
         return year;
    }  
    
    public void accelerate(int MaxSpeed)
    {   
    	for (int i = 0; i < MaxSpeed; i++) { 
    	System.out.println("Accelerating to: " + i + "mph");
    	speed++;
    	}
    	System.out.println("Speed is now: " + speed + "mph");
    }
    
    public void brake (int carSpeed)
    {   
         speed = speed--;
    }
    
    public void setSpeed(int newSpeed)
    {
         speed = newSpeed;
    }  
    
    public int getSpeed()
    {
        return speed;
    }
   
    public static void main(String[] args)
    {
        AdjustableCar ford = new AdjustableCar();
        ford.setMake("Ford");
        ford.setYear(2004);
        
        
        AdjustableCar toyota = new AdjustableCar();
        toyota.setMake("Toyota");
        toyota.setYear(2007);
        toyota.setSpeed(0);
        
        
        System.out.println("First car make is: " + ford.getMake());
        System.out.println("First car year is: " + ford.getYear());
        
        System.out.println("\nSecond car make is: " + toyota.getMake());
        System.out.println("Second car year is: " + toyota.getYear());
        
        System.out.println("Speed is: " + toyota.getSpeed() + "mph");

      
        Scanner reader = new Scanner(System.in);
        System.out.println("What speed do you want to go?: ");
        int s = reader.nextInt();
    
        toyota.accelerate(s);
        
      reader.close();
    }
}
