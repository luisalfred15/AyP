package com.mycompany.bonusayp;

/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Project/Maven2/JavaApp/src/main/java/${packagePath}/${mainClassName}.java to edit this template
 */

import java.util.Scanner;

/**
 *
 * @author luisa
 */
public class BonusAyP {

    public static void main(String[] args) {
        
        ProductoFresco[] arregloFrescos = new ProductoFresco[100];
        ProductoRefrigerado[] arregloRefrigerados = new ProductoRefrigerado[100];
        ProdCongAire[] arregloCongAire = new ProdCongAire[100];
        ProdCongAgua[] arregloCongAgua = new ProdCongAgua[100];
        ProdCongNitro[] arregloCongNitro = new ProdCongNitro[100];
        
        
        ProductoFresco leche = new ProductoFresco("Leche", 10f, "24/06/2022", "01/07/2022", 23523, "Venezuela");
        arregloFrescos[0] = leche;
        ProductoFresco yogurt = new ProductoFresco("Yogurt", 5f, "24/06/2022", "29/06/2022", 87102, "Grecia");
        arregloFrescos[1] = yogurt;
        ProductoFresco tomate = new ProductoFresco("Tomate", 3.5f, "24/06/2022", "28/06/2022", 90215, "Venezuela"); 
        arregloFrescos[2] = tomate;
        ProductoFresco platano = new ProductoFresco("Platano", 3f, "24/06/2022", "27/06/2022", 77713, "Venezuela"); 
        arregloFrescos[3] = platano;
        ProductoFresco zanahoria = new ProductoFresco("Zanahoria", 3f, "24/06/2022", "29/06/2022", 42289, "Venezuela");
        arregloFrescos[4] = zanahoria;
        ProductoFresco papa = new ProductoFresco("Papa", 1.5f, "24/06/2022", "29/06/2022", 88918, "Venezuela");
        arregloFrescos[5] = papa;
        ProductoFresco cebolla = new ProductoFresco("Cebolla", 2f, "24/06/2022", "28/06/2022", 42289, "Venezuela");
        arregloFrescos[6] = cebolla;
        ProductoFresco cebollin = new ProductoFresco("Cebollin", 2.5f, "24/06/2022", "29/06/2022", 42289, "Venezuela");
        arregloFrescos[7] = cebollin;
        ProductoFresco perejil = new ProductoFresco("Perejil", 2f, "24/06/2022", "28/06/2022", 42289, "Venezuela");
        arregloFrescos[8] = perejil;
        ProductoFresco aguacate = new ProductoFresco("Aguacate", 5f, "24/06/2022", "29/06/2022", 42289, "Venezuela");
        arregloFrescos[9] = aguacate;
        
        ProductoRefrigerado atun = new ProductoRefrigerado("Atun", 15f, "24/06/2022", "24/07/2022", 14987, "EE.UU.", "C-147", -20.0f);
        arregloRefrigerados[0] = atun;
        ProductoRefrigerado carneVaca = new ProductoRefrigerado("Carne de Vaca", 30f, "24/06/2022", "24/07/2022", 68166, "Venezuela", "C-104", -27.0f);
        arregloRefrigerados[1] = carneVaca;
        ProductoRefrigerado huevos = new ProductoRefrigerado("Huevos", 8f, "24/06/2022", "30/06/2022", 93396, "Venezuela", "C-617", -10.5f);
        arregloRefrigerados[2] = huevos;
        ProductoRefrigerado torta = new ProductoRefrigerado("Torta", 20f, "24/06/2022", "28/06/2022", 42643, "Venezuela", "C-104", -12.0f);
        arregloRefrigerados[3] = torta;
        ProductoRefrigerado jamon = new ProductoRefrigerado("Jamon", 11.5f, "24/06/2022", "01/07/2022", 35191, "España", "C-147", -9.5f);
        arregloRefrigerados[4] = jamon;
        ProductoRefrigerado pollo = new ProductoRefrigerado("Pollo", 15f, "24/06/2022", "29/06/2022", 40948, "Venezuela", "C-147", -18.0f);
        arregloRefrigerados[5] = pollo;
        ProductoRefrigerado salchichas = new ProductoRefrigerado("Salchichas", 10f, "24/06/2022", "30/06/2022", 40948, "Venezuela", "C-104", -25.0f);
        arregloRefrigerados[6] = salchichas;
        ProductoRefrigerado chorizo = new ProductoRefrigerado("Chorizo", 18f, "24/06/2022", "29/06/2022", 40948, "Venezuela", "C-147", -14.5f);
        arregloRefrigerados[7] = chorizo;
        ProductoRefrigerado pavo = new ProductoRefrigerado("Pavo", 14f, "24/06/2022", "28/06/2022", 40948, "Venezuela", "C-617", -16.0f);
        arregloRefrigerados[8] = pavo;
        ProductoRefrigerado carneMolida = new ProductoRefrigerado("Carne molida", 15f, "24/06/2022", "24/07/2022", 40948, "Venezuela", "C-147", -22.0f);
        arregloRefrigerados[9] = carneMolida;
        
        ProdCongAire camarones = new ProdCongAire("Camarones", 28.5f, "24/06/2022", "24/08/2022", 26912, "Chile", -20f, 25f, 25f, 25f, 25f);
        arregloCongAire[0] = camarones;
        ProdCongAire salmon = new ProdCongAire("Salmon", 35f, "24/06/2022", "15/08/2022", 75086, "Canadá", -25f, 10f, 10f, 30f, 50f);
        arregloCongAire[1] = salmon;
        ProdCongAire merluza = new ProdCongAire("Merluza", 20f, "24/06/2022", "24/07/2022", 73729, "Venezuela", -15f, 22.5f,22.5f, 30f, 25f);
        arregloCongAire[2] = merluza;
        ProdCongAire frambuesas = new ProdCongAire("Frambuesas", 15f, "24/06/2022", "08/07/2022", 59966, "EE.UU.", -12f, 30f, 40f, 20f, 10f);
        arregloCongAire[3] = frambuesas;
        ProdCongAire tortillaIntegral = new ProdCongAire("Tortilla Integral", 6f, "24/06/2022", "28/06/2022", 72073, "Venezuela", -10f, 45f, 5f, 45f, 5f);
        arregloCongAire[4] = tortillaIntegral;
        ProdCongAire pimenton = new ProdCongAire("Pimenton", 5f, "24/06/2022", "27/06/2022", 72970, "Venezuela", -7.5f, 5f, 60f, 25f, 10f);
        arregloCongAire[5] = pimenton;
        ProdCongAire brocoli = new ProdCongAire("Brocoli", 4f, "24/06/2022", "28/06/2022", 72970, "Venezuela", -8f, 20f, 15f, 15f, 50f);
        arregloCongAire[6] = brocoli;
        ProdCongAire remolacha = new ProdCongAire("Remolacha", 8f, "24/06/2022", "27/06/2022", 72970, "Venezuela", -10f, 5f, 60f, 32f, 3f);
        arregloCongAire[7] = remolacha;
        ProdCongAire coliflor = new ProdCongAire("Coliflor", 8f, "24/06/2022", "28/06/2022", 72970, "Venezuela", -7f, 45f, 15f, 25f, 15f);
        arregloCongAire[8] = coliflor;
        ProdCongAire celeri = new ProdCongAire("Céleri", 5f, "24/06/2022", "27/06/2022", 72970, "Venezuela", -5f, 30f, 40f, 10f, 20f);
        arregloCongAire[9] = celeri;
        
        ProdCongAgua robalo = new ProdCongAgua("Robalo", 15f, "24/06/2022", "10/07/2022", 71214, "Venezuela", -10.5f, 50f);
        arregloCongAgua[0] = robalo;
        ProdCongAgua langostinos = new ProdCongAgua("Langostinos", 30f, "24/06/2022", "24/06/2022", 94691, "España", -12.5f, 25f);
        arregloCongAgua[1] = langostinos;
        ProdCongAgua cangrejo = new ProdCongAgua("Cangrejo", 40f, "24/06/2022", "24/08/2022", 13787, "Venezuela", -10f, 40f);
        arregloCongAgua[2] = cangrejo;
        ProdCongAgua pulpo = new ProdCongAgua("Pulpo", 40f, "24/06/2022", "10/07/2022", 91197, "Francia", -18f, 35f);
        arregloCongAgua[3] = pulpo;
        ProdCongAgua langosta = new ProdCongAgua("Langosta", 60f, "24/06/2022", "24/08/2022", 31608, "Dinamarca", -8f, 16.5f);
        arregloCongAgua[4] = langosta;
        ProdCongAgua calamar = new ProdCongAgua("Calamar", 50f, "24/06/2022", "24/07/2022", 77478, "Venezuela", -15f, 80.5f);
        arregloCongAgua[5] = calamar;
        ProdCongAgua anchoas = new ProdCongAgua("Anchoas", 15f, "24/06/2022", "24/07/2022", 77478, "Venezuela", -10f, 90f);
        arregloCongAgua[6] = anchoas;
        ProdCongAgua percebes = new ProdCongAgua("Percebes", 25f, "24/06/2022", "14/08/2022", 77478, "Venezuela", -20f, 75.5f);
        arregloCongAgua[7] = percebes;
        ProdCongAgua dorado = new ProdCongAgua("Dorado", 25f, "24/06/2022", "14/07/2022", 77478, "Venezuela", -30f, 80f);
        arregloCongAgua[8] = dorado;
        ProdCongAgua cazon = new ProdCongAgua("Cazon", 13f, "24/06/2022", "24/07/2022", 77478, "Venezuela", -15f, 60f);
        arregloCongAgua[9] = cazon;
        
        
        ProdCongNitro helado = new ProdCongNitro("Helado", 12f, "24/06/2022", "24/07/2022", 34672, "EE.UU.", -150f, "Nitrogeno liquido", 100);
        arregloCongNitro[0] = helado;
        ProdCongNitro alcachofa = new ProdCongNitro("Alcachofa", 8f, "24/06/2022", "29/06/2022", 49109, "Venezuela", -155f, "En camara", 75);
        arregloCongNitro[1] = alcachofa;
        ProdCongNitro arandanos = new ProdCongNitro("Arandanos", 15f, "24/06/2022", "09/07/2022", 40345, "México", -170f, "Tuneles", 120);
        arregloCongNitro[2] = arandanos;
        ProdCongNitro fresas = new ProdCongNitro("Fresas", 10.5f, "24/06/2022", "01/07/2022", 16600, "Venezuela", -150f, "Nitrogeno liquido", 190);
        arregloCongNitro[3] = fresas;
        ProdCongNitro moras = new ProdCongNitro("Moras", 18.5f, "24/06/2022", "24/07/2022", 98699, "Países Bajos", -130f, "Nitrogeno liquido", 50);
        arregloCongNitro[4] = moras;
        ProdCongNitro espinaca = new ProdCongNitro("Espinaca", 11f, "24/06/2022", "28/06/2022", 55983, "Venezuela", -160f, "En camara", 170);
        arregloCongNitro[5] = espinaca;
        ProdCongNitro lechuga = new ProdCongNitro("Lechuga", 7f, "24/06/2022", "28/06/2022", 55983, "Venezuela", -100f, "Nitrogeno liquido", 90);
        arregloCongNitro[6] = lechuga;
        ProdCongNitro kiwi = new ProdCongNitro("Kiwi", 9f, "24/06/2022", "30/06/2022", 55983, "Venezuela", -130f, "En camara", 120);
        arregloCongNitro[7] = kiwi;
        ProdCongNitro pizzaPepperoni = new ProdCongNitro("Pizza con pepperoni", 16f, "24/06/2022", "27/06/2022", 55983, "Italia", -110f, "Tuneles", 100);
        arregloCongNitro[8] = pizzaPepperoni;
        ProdCongNitro pizzaMargarita = new ProdCongNitro("Pizza Margarita", 10f, "24/06/2022", "27/06/2022", 55983, "Italia", -110f, "Tuneles", 100);
        arregloCongNitro[9] = pizzaMargarita;

        
        boolean ejecutar = true;
        
        while (ejecutar) {
            
            System.out.println("Ingrese la opcion deseada: \n 1. Conocer fecha de caduciad y lote de todos los productos \n 2. Agregar un nuevo producto \n 3. Vender un producto del almacen \n 4. Comunicarse con el obrero \n 5. Comunicarse con el administrador \n 6. Comunicarse con el supervisor \n 7. Salir del sistema");
            Scanner sc = new Scanner(System.in);
            int opcion = sc.nextInt();
            
            sc.nextLine();
            
            switch (opcion) {
                case 1:
                    
                    System.out.println("*** PRODUCTOS FRESCOS ***\n");
                    for (ProductoFresco i : arregloFrescos) {
                        if (i != null){
                            System.out.println(i.toString());
                        } else {
                            break;
                        }
                    }   
                    
                    System.out.println("*** PRODUCTOS REFRIGERADOS ***\n");
                    for (ProductoRefrigerado i : arregloRefrigerados) {
                        if (i != null){
                            System.out.println(i.toString());
                        } else {
                            break;
                        }
                    }   
                    
                    System.out.println("*** PRODUCTOS CONGELADOS POR AIRE *** \n");
                    for (ProdCongAire i : arregloCongAire) {
                        if (i != null) {
                            System.out.println(i.toString());
                        } else {
                            break;
                        }
                    }   
                    
                    System.out.println("*** PRODUCTOS CONGELADOS POR AGUA ***\n");
                    for (ProdCongAgua i : arregloCongAgua) {
                        if (i != null){
                            System.out.println(i.toString());
                        } else {
                            break;
                        }
                    }   
                    
                    System.out.println("*** PRODUCTOS CONGELADOS POR AIRE ***\n");
                    for (ProdCongNitro i : arregloCongNitro) {
                        if (i != null) {
                            System.out.println(i.toString());
                        } else {
                            break;
                        }
                    }   
                    
                    break;
                    
                case 2:
                    
                    System.out.println("Ingrese el nombre del producto: ");
                    String nombreNuevo = sc.nextLine();
                    
                    System.out.println("Ingrese el precio del producto: ");
                    float precioNuevo = sc.nextFloat();
                    
                    sc.nextLine();
                    
                    System.out.println("Ingrese la fecha de envasado del producto como dd/mm/aaaa: ");
                    String fechaEnvasadoNuevo = sc.nextLine();
                    
                    System.out.println("Ingrese la fecha de caducidad del producto como dd/mm/aaaa: ");
                    String fechaCaducidadNuevo = sc.nextLine();
                    
                    System.out.println("Ingrese el numero de lote del producto como XXXXX: ");
                    int numeroLoteNuevo = sc.nextInt();
                    
                    sc.nextLine();
                    
                    System.out.println("Ingrese el pais de origen del producto: ");
                    String paisOrigenNuevo = sc.nextLine();
                    
                    System.out.println("Seleccione que tipo de producto desea agregar: \n 1. Producto fresco \n 2. Producto refrigerado \n 3. Producto congelado");
                    int opcionProducto = sc.nextInt();
                    
                    sc.nextLine();
                    
                    switch (opcionProducto) {
                        
                        case 1:
                        
                            ProductoFresco nuevoProductoFresco = new ProductoFresco(nombreNuevo, precioNuevo, fechaEnvasadoNuevo, fechaCaducidadNuevo, numeroLoteNuevo, paisOrigenNuevo);
                            
                            for (int i = 0; i < arregloFrescos.length; i++) {
                                if (arregloFrescos[i] == null) {
                                    arregloFrescos[i] = nuevoProductoFresco;
                                    break;
                                }
                            }
                            
                            System.out.println("Producto agregado con exito!");
                            
                            break;
                        
                        case 2:
                        
                            
                            System.out.println("Ingrese el codigo del organismo, en el formato C-XXX: ");
                            String codigoOrganismoNuevo = sc.nextLine();
                            
                            System.out.println("Ingrese la temperatura de mantenimiento del producto: ");
                            float tempManteNuevo = sc.nextFloat();
                            
                            ProductoRefrigerado nuevoProductoRefrigerado = new ProductoRefrigerado(nombreNuevo, precioNuevo, fechaEnvasadoNuevo, fechaCaducidadNuevo, numeroLoteNuevo, paisOrigenNuevo, codigoOrganismoNuevo, tempManteNuevo);
                            
                            for (int i = 0; i < arregloRefrigerados.length; i++) {
                                if (arregloRefrigerados[i] == null) {
                                    arregloRefrigerados[i] = nuevoProductoRefrigerado;
                                    break;
                                }
                            }
                            
                            System.out.println("Producto agregado con exito!");
                            
                            break;
                        
                        case 3:
                        
                            System.out.println("Ingrese la temperatura de mantenimiento del producto: ");
                            float tempManteNuevo2 = sc.nextFloat();
                            
                            System.out.println("Seleccione que tipo de producto congelado desea agregar: \n 1. Congelado con aire \n 2. Congelado con agua \n 3. Congelado con nitrogeno");
                            int opcionCongelado = sc.nextInt();
                            
                            sc.nextLine();
                            
                            switch (opcionCongelado) {
                                
                                case 1:
                                
                                    
                                    System.out.println("Ingrese el porcentaje de nitrogeno del aire: ");
                                    float porcentajeNiNuevo = sc.nextFloat();
                                    
                                    System.out.println("Ingrese el porcentaje de oxigeno del aire: ");
                                    float porcentajeONuevo = sc.nextFloat();
                                    
                                    System.out.println("Ingrese el porcentaje de carbono del aire: ");
                                    float porcentajeCNuevo = sc.nextFloat();
                                    
                                    System.out.println("Ingrese el porcentaje de agua del aire: ");
                                    float porcentajeH2ONuevo = sc.nextFloat();
                                    
                                    ProdCongAire nuevoProdCongAire = new ProdCongAire(nombreNuevo, precioNuevo, fechaEnvasadoNuevo, fechaCaducidadNuevo, numeroLoteNuevo, paisOrigenNuevo, tempManteNuevo2, porcentajeNiNuevo, porcentajeONuevo, porcentajeCNuevo, porcentajeH2ONuevo);
                                    
                                    for (int i = 0; i < arregloCongAire.length; i++) {
                                        if (arregloCongAire[i] == null) {
                                            arregloCongAire[i] = nuevoProdCongAire;
                                            break;
                                        }
                                    }
                                    
                                    System.out.println("Producto agregado con exito!");
                                    
                                    break;
                                
                                case 2:
                                
                                    
                                    System.out.println("Ingrese la salinidad del agua: ");
                                    float salinidadAguaNuevo = sc.nextFloat();
                                    
                                    ProdCongAgua nuevoProdCongAgua = new ProdCongAgua(nombreNuevo, precioNuevo, fechaEnvasadoNuevo, fechaCaducidadNuevo, numeroLoteNuevo, paisOrigenNuevo, tempManteNuevo2, salinidadAguaNuevo);
                                    
                                    for (int i = 0; i < arregloCongAgua.length; i++) {
                                        if (arregloCongAgua[i] == null) {
                                            arregloCongAgua[i] = nuevoProdCongAgua;
                                            break;
                                        }
                                    }
                                    
                                    System.out.println("Producto agregado con exito!");
                                    
                                    break;
                                    
                                
                                case 3:
                                
                                   
                                    System.out.println("Ingrese el metodo de congelacion empleado: ");
                                    String metodoCongelacionNuevo = sc.nextLine();
                                    
                                    System.out.println("Ingrese el tiempo de exposicion al nitrogento: ");
                                    int tiempoExposicionNiNuevo = sc.nextInt();
                                    
                                    ProdCongNitro nuevoProdCongNitro = new ProdCongNitro(nombreNuevo, precioNuevo, fechaEnvasadoNuevo, fechaCaducidadNuevo, numeroLoteNuevo, paisOrigenNuevo, tempManteNuevo2, metodoCongelacionNuevo, tiempoExposicionNiNuevo);
                                    
                                    for (int i = 0; i < arregloCongNitro.length; i++) {
                                        if (arregloCongNitro[i] == null) {
                                            arregloCongNitro[i] = nuevoProdCongNitro;
                                            break;
                                        }
                                    }
                                    
                                    System.out.println("Producto agregado con exito!");
                                    
                                    break;
                                
                                default:
                                    
                                    System.out.println("Ingrese una opcion valida");
                                    
                                    break;
                                    
                                }
                            
                            break;
                            
                        default:
                            System.out.println("Ingrese una opcion valida");
                            break;
                    
                        }
                    
                    break;
                
                case 3:
                    
                    System.out.println("Seleccione que tipo de producto desea adquirir: \n 1. Producto fresco \n 2. Producto refrigerado \n 3. Producto congelado");
                    int opcionCompra = sc.nextInt();
                    
                    switch (opcionCompra) {
                        
                        case 1:

                            System.out.println("*** PRODUCTOS FRESCOS ***\n");
                            for (int i = 0; i < arregloFrescos.length; i++) {
                                if (arregloFrescos[i] != null){
                                    System.out.println("    ID " + i);
                                    System.out.println(arregloFrescos[i].toString());
                                } else {
                                    break;
                                }
                            }
                            
                            while (true) {
                                System.out.println("Ingrese el ID del producto que desea vender: ");
                                int id = sc.nextInt();

                                if (0 <= id && id < arregloFrescos.length){
                                    ProductoFresco[] copiaArregloFrescos = new ProductoFresco[arregloFrescos.length - 1];
                                    for (int i = 0, j = 0; i < arregloFrescos.length; i++) {
                                        if (i != id) {
                                            copiaArregloFrescos[j++] = arregloFrescos[i];
                                        }
                                    }
                                    arregloFrescos = copiaArregloFrescos;
                                    System.out.println("Producto vendido!");
                                    
                                    break;
                                } else {
                                    System.out.println("Seleccione un ID valido");
                                }
                            }
                            
                            break;
                        
                        case 2:
                            
                            System.out.println("*** PRODUCTOS REFRIGERADOS ***\n");
                            for (int i2 = 0; i2 < arregloRefrigerados.length; i2++) {
                                if (arregloRefrigerados[i2] != null){
                                    System.out.println("    ID " + i2);
                                    System.out.println(arregloRefrigerados[i2].toString());
                                } else {
                                    break;
                                }
                            }
                            
                            while (true) {
                                System.out.println("Ingrese el ID del producto que desea vender: ");
                                int id2 = sc.nextInt();

                                if (0 <= id2 && id2 < arregloRefrigerados.length){
                                    ProductoRefrigerado[] copiaArregloRefrigerados = new ProductoRefrigerado[arregloRefrigerados.length - 1];
                                    for (int i = 0, j = 0; i < arregloRefrigerados.length; i++) {
                                        if (i != id2) {
                                            copiaArregloRefrigerados[j++] = arregloRefrigerados[i];
                                        }
                                    }
                                    arregloRefrigerados = copiaArregloRefrigerados;
                                    System.out.println("Producto vendido!");
                                    break;
                                } else {
                                    System.out.println("Seleccione un ID valido");
                                }
                            }
                            
                            break;
                        
                        case 3:
                            
                            System.out.println("Seleccione que tipo de producto congelado desea adquirir: \n 1. Congelado por aire \n 2. Congelado por agua \n 3. Congelado por nitrogeno");
                            int opcionCompraCongelado = sc.nextInt();
                            
                            switch (opcionCompraCongelado) {
                                
                                case 1:

                                    System.out.println("*** PRODUCTOS CONGELADOS POR AIRE ***\n");
                                    for (int i3 = 0; i3 < arregloCongAire.length; i3++) {
                                        if (arregloCongAire[i3] != null){
                                            System.out.println("    ID " + i3);
                                            System.out.println(arregloCongAire[i3].toString());
                                        } else {
                                            break;
                                        }
                                    }
                                    
                                    while (true) {
                                        System.out.println("Ingrese el ID del producto que desea vender: ");
                                        int id3 = sc.nextInt();

                                        if (0 <= id3 && id3 < arregloCongAire.length){
                                            ProdCongAire[] copiaArregloCongAire = new ProdCongAire[arregloCongAire.length - 1];
                                            for (int i = 0, j = 0; i < arregloCongAire.length; i++) {
                                                if (i != id3) {
                                                    copiaArregloCongAire[j++] = arregloCongAire[i];
                                                }
                                            }
                                            arregloCongAire = copiaArregloCongAire;
                                            System.out.println("Producto vendido!");
                                            break;
                                        } else {
                                            System.out.println("Seleccione un ID valido");
                                        }
                                    }
                                    
                                    break;
                                
                                case 2:

                                    System.out.println("*** PRODUCTOS CONGELADOS POR AGUA ***\n");
                                    for (int i4 = 0; i4 < arregloCongAgua.length; i4++) {
                                        if (arregloCongAgua[i4] != null){
                                            System.out.println("    ID " + i4);
                                            System.out.println(arregloCongAgua[i4].toString());
                                        } else {
                                            break;
                                        }
                                    }
                                    
                                    while (true) {
                                        System.out.println("Ingrese el ID del producto que desea vender: ");
                                        int id4 = sc.nextInt();

                                        if (0 <= id4 && id4 < arregloCongAgua.length){
                                            ProdCongAgua[] copiaArregloCongAgua = new ProdCongAgua[arregloCongAgua.length - 1];
                                            for (int i = 0, j = 0; i < arregloCongAgua.length; i++) {
                                                if (i != id4) {
                                                    copiaArregloCongAgua[j++] = arregloCongAgua[i];
                                                }
                                            }
                                            arregloCongAgua = copiaArregloCongAgua;
                                            System.out.println("Producto vendido!");
                                            break;
                                        } else {
                                            System.out.println("Seleccione un ID valido");
                                        }
                                    }
                                    
                                    break;
                                    
                                case 3:

                                    System.out.println("*** PRODUCTOS CONGELADOS POR NITROGENO ***\n");
                                    for (int i5 = 0; i5 < arregloCongNitro.length; i5++) {
                                        if (arregloCongNitro[i5] != null){
                                            System.out.println("    ID " + i5);
                                            System.out.println(arregloCongNitro[i5].toString());
                                        } else {
                                            break;
                                        }
                                    }
                                    
                                    while (true) {
                                        System.out.println("Ingrese el ID del producto que desea vender: ");
                                        int id5 = sc.nextInt();

                                        if (0 <= id5 && id5 < arregloCongNitro.length){
                                            ProdCongNitro[] copiaArregloCongNitro = new ProdCongNitro[arregloCongNitro.length - 1];
                                            for (int i = 0, j = 0; i < arregloCongNitro.length; i++) {
                                                if (i != id5) {
                                                    copiaArregloCongNitro[j++] = arregloCongNitro[i];
                                                }
                                            }
                                            arregloCongNitro = copiaArregloCongNitro;
                                            System.out.println("Producto vendido!");
                                            break;
                                        } else {
                                            System.out.println("Seleccione un ID valido");
                                        }
                                    }
                                    
                                    break;
                                
                                default:
                                    System.out.println("Ingrese una opcion valida");
                                    break;
                            }
                            break; 
                        
                        default:
                            System.out.println("Ingrese una opcion valida");
                            break;
                            
                        }
                    break;    
                    
                case 4:
                    Obrero obrero1 = new Obrero();
                    obrero1.traerProductos();
                    break;
                
                case 5:
                    Administrador admin1 = new Administrador();
                    admin1.verificarRentabilidad();
                    break;
                    
                case 6:
                    Supervisor super1 = new Supervisor();
                    super1.supervisarVentas();
                    break;
                
                case 7:
                    ejecutar = false;
                    break;
                
                default:
                    System.out.println("Ingrese una opcion valida");
                    break;
                
                }
            }
        }
    }          