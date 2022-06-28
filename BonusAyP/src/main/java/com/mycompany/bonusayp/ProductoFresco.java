/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.mycompany.bonusayp;

/**
 *
 * @author luisa
 */

public class ProductoFresco extends Producto {
    public ProductoFresco (String nombre, float precio, String fechaEnvasado, String fechaCaducidad, int numeroLote, String paisOrigen) {
        super(nombre, precio, fechaEnvasado, fechaCaducidad, numeroLote, paisOrigen);
    }
    
    @Override
    public String toString() {
        return "Nombre: " + getNombre() + "\n Precio: " + getPrecio() + "\n Fecha de envasado: " + getFechaEnvasado() + "\n Fecha de caducidad: " + getFechaCaducidad() + "\n Numero de lote: " + getNumeroLote() + "\n Pais de origen: " + getPaisOrigen() + "\n";
    }
}
