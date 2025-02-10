import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        System.out.println("Hello World");

        // Variables
        int edad;
        double estatura; // float
        boolean finado;
        char letra;
        String nombre;
        long numeroLargo;


        // Operacion de asignacion
        edad = 34;
        estatura = 50.42;
        finado = false;
        letra = 'b';
        nombre = "Hugo Perez 412";
        numeroLargo = 42423432;


        System.out.println("Mi edad: " + edad);
        System.out.println(estatura);
        System.out.println("Es finado: " + finado);
        System.out.println(letra);
        System.out.println(nombre);
        System.out.println("Numero largo: " + numeroLargo);

        // Operadores

        int num1, num2, suma, resta, multi;
        // double num1, num2, suma, resta, multi; // Las variables tambien deben
        // ser double junto con el scanner, (,)
        double divi;
        Scanner entrada = new Scanner(System.in);

        System.out.println("Ingrese su primer numero: ");
        num1 = entrada.nextInt();
        System.out.println("Ingrese su segundo numero: ");
        num2 = entrada.nextInt();

        suma = num1 + num2;
        resta = num1 - num2;
        multi = num1 * num2;
        divi = num1 / num2;

        System.out.println("La suma de ambos numeros es: " + suma);
        System.out.println("La resta de ambos numeros es: " + resta);
        System.out.println("La multiplicion de ambos numeros es: " + multi);
        System.out.println("La division de ambos numeros es: " + divi);



    }
}