import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.HashMap;
import java.util.Map;

public class RedesSociales {
	
	public static void main(String[] args) {
		String csvFile="";
		try {
			csvFile = args[0];
		} catch (Exception e) {
			System.out.println("nombre archivo");
			System.exit(0);
		}
		
		String line = "";
		String csvSplitBy = ",";
		
		Map<String, Integer> NameOccurence = new HashMap<String, Integer>();
		Map
	}
}