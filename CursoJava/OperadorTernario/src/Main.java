import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        // OPERADOR TERNARIO - VERSIONES MAS NUEVAS

        // HERRAMIENTA EN JAVA PARA TOMAR DECISIONES SIMPLES EN UNA SOLA LINEA DE CODIGO

        // variable = (condicion) ? valor_si_verdadero : valor_si_falso; //

        // Programa que dependiendo del promedio, nos diga si aprobo, o no una materia

        double calif;
        String repAprob;
        Scanner entrada = new Scanner(System.in);

        calif = entrada.nextDouble();

        repAprob = (calif >= 6) ? "Aprobado" : "Reprobado";

        System.out.println(repAprob);


    }
}