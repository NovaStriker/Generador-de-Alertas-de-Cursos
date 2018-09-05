package texto_java;
import java.io.*;
import java.util.Map;
import java.util.TreeMap;
//import java.util.HashMap;

public class TextoJavaMain {

	public static void main(String[] args) {
		
		//nombre del archivo de datos y archivo de datos procesado
		String archivoProcedencia = "datos.txt";
		String archivoProcesado = "datos procesados.txt";
		String linea = "";
		int cantidadPublicaciones = 0;
		int cantidadPorRedesSociales = 0;
		//palabras de interés
		String [] palabrasClave = {"curso", "maestria", "participa", "seminario", "taller"};
		
		//asignación de palabras de interés a diccionario
		Map<String, Integer> categoriaCantidad = new TreeMap<String, Integer>();
		for (int palabra = 0; palabra < palabrasClave.length; palabra++) {
			categoriaCantidad.put(palabrasClave[palabra], 0);
		}
		//System.out.println(categoriaCantidad.size());
		//System.out.println(categoriaCantidad.values());
		
		//redes sociales
		String [] redesSociales = {"facebook", "instagram", "twitter"};
		
		//asignación de redes sociales a diccionario
		Map<String, Integer> redSocialCantidad = new TreeMap<String, Integer>();
		for (int red = 0; red < redesSociales.length; red++) {
			redSocialCantidad.put(redesSociales[red], 0);
		}
		//System.out.println(redSocialCantidad.size());
		//System.out.println(redSocialCantidad.values());
		
		//índice de contenido y enlace
		int indiceLinea = 1; 
		
		try {
			//atributo de lectura de texto
			FileReader fileReader = new FileReader(archivoProcedencia);
			
			//buffer de lectura que se junta con atributo de lectura
			BufferedReader bufferedReader = new BufferedReader(fileReader);
			
			//atributo de escritura de texto
			FileWriter fileWriter = new FileWriter(archivoProcesado);
			
			//buffer de escritura que se junta con el atributo de escritura
			BufferedWriter bufferedWriter = new BufferedWriter(fileWriter);
			
			//leyendo el archivo línea por línea
			while((linea = bufferedReader.readLine()) != null) {
				//verificando indice de contenido
				if(indiceLinea == 1) {
					//verificando contenido válido para mostrar
					for (int i = 0; i < palabrasClave.length; i++) {
						if(linea.contains(palabrasClave[i])) {
							//System.out.println(linea);
							//escribiendo contenido a archivo de texto procesado
							bufferedWriter.write(linea + "\n");
							//actualización de diccionario según las categorías que se encuentren
							cantidadPublicaciones = (categoriaCantidad.get(palabrasClave[i])) + 1;
							categoriaCantidad.put(palabrasClave[i], cantidadPublicaciones);
							//incremento de índice a enlace
							indiceLinea++;
							break;
						}
					}
				//verificando índice de enlace
				} else if(indiceLinea == 2) {
					//System.out.println(linea);
					//escribiendo enlace a archivo de texto procesado
					bufferedWriter.newLine();
					bufferedWriter.write(linea + "\n");
					bufferedWriter.newLine();
					//regresando a índice de contenido
					indiceLinea = 1;
					
					for( int j = 0; j < redesSociales.length; j++) {
						if(linea.contains(redesSociales[j])) {
							cantidadPorRedesSociales = (redSocialCantidad.get(redesSociales[j])) + 1;
							redSocialCantidad.put(redesSociales[j], cantidadPorRedesSociales);
						}
					}
				}
				
			}
			//se cierra el documento
			bufferedWriter.close();
			bufferedReader.close();
		} catch(FileNotFoundException ex) {
			System.out.println("Este archivo no existe : " + archivoProcedencia);
		} catch(IOException ex) {
			System.out.println("Error leyendo archivo : " + archivoProcedencia);
		}
		
		System.out.println("Archivo generado");
		System.out.println(categoriaCantidad.values());
		System.out.println(redSocialCantidad.values());
	}
}
