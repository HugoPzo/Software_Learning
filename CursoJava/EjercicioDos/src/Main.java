import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        /*Realizar un programa que muestre en pantalla los números del 1 al 35
        * (uno abajo del otro).*/

        /*for (int i = 1; i <= 35; i++){
            System.out.println(i);
        }*/

        /*Realizar un programa que dado por teclado un limite numerico (n), muestre
        * en pantalla todos los numero hasta ese limite (empezando por 1)*/

        /*Scanner entry = new Scanner(System.in);
        System.out.println("Ingresa un numero limite: ");
        int limite = entry.nextInt();

        for (int i = 1; i <= limite; i++){
            System.out.println(i);
        }*/

        /*Realizar un programa que muestre por pantalla los numeros del 200 al 250 saltando
        * de 2 en 2.*/

        /*for(int i = 200; i <= 250; i+=2){
            System.out.println(i);
        }*/

        /*Realizar un programa que lleve a cabo la cuenta regresiva para el año nuevo.
        * La cuenta debe comenzar en 10 y terminar en 1*/

        /*for (int i = 10; i > 0; i--){
            System.out.println(i);
        }*/

        /*Realizar un programa que muestre en pantalla palabras que sean ingresadas
        * por teclado hasta que ingrese la palabra "salir"*/

        Scanner entry = new Scanner(System.in);
        String palabra = "";

        while(!palabra.equals("salir")){
            palabra = entry.nextLine();
            System.out.println(palabra);
        }


    }
}