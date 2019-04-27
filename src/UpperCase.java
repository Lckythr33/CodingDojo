import java.lang.String;
import java.util.Scanner;
public class UpperCase
{
    public static String upperFirst()
    {  
        //Prompts user to enter a String
        System.out.println("Enter a String.");
        Scanner keyboard = new Scanner(System.in);
        String input = keyboard.nextLine();
        
    		String[] sentences = input.split("\\.\\s");
    		StringBuilder sb = new StringBuilder();

    		for (String s: sentences) {
    			sb.append(Character.toUpperCase(s.charAt(0)));
				sb.append(s.substring(1));
      			sb.append(". ");
    		} 		
    		
    		System.out.println(sb.toString());
    		return sb.toString().trim();
    }
    
    public static void main(String[] args)
    {
        upperFirst();
    }
}