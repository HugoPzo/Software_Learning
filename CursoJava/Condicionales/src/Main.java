import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        int edad;

        Scanner entrada = new Scanner(System.in);

        System.out.println("Ingrese su edad: ");
        edad = entrada.nextInt();

        if(edad<18){
            System.out.println("Usted es menor de edad");

        }else if(edad >= 18 && edad<=25) {
            System.out.println("Usted es joven");
        }else if(edad == 65 || edad == 90) {
            System.out.println("Le atinaste a la edad");
        }else{
            if(edad == 32){
                System.out.println("Tienes 32 anios");
            }else if(edad != 40){
                System.out.println("No tienes 40 anios");
            }
            System.out.println("Usted es viejo.");
        }

    }
}