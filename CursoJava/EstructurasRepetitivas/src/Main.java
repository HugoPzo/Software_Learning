public class Main {
    public static void main(String[] args) {
        int contador = 50;

        // Do While

        do{

            System.out.println("Estoy en la vuelta numero: " + (contador));
            contador++;

        }while(contador <= 10);

        System.out.println("\n");

        // While

        while(contador < 100){

            System.out.println(contador);
            contador++;
        }

        System.out.println("\n");

        // Ejemplo de bucle controlado por centinela
        boolean bandera = true;
        int contadorBandera = 0;

        while(bandera){

            if (contadorBandera == 43){
                System.out.println("Ya es 43");
                bandera = false;
            }

            contadorBandera++;

        }



    }
}