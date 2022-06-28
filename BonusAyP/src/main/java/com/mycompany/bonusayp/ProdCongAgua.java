/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.mycompany.bonusayp;

/**
 *
 * @author luisa
 */
public class ProdCongAgua extends ProductoCongelado {

    private float salinidadAgua;
    
    public ProdCongAgua(String nombre, float precio, String fechaEnvasado, String fechaCaducidad, int numeroLote, String paisOrigen, float tempMante, float salinidadAgua) {
        super(nombre, precio, fechaEnvasado, fechaCaducidad, numeroLote, paisOrigen, tempMante);
        this.salinidadAgua = salinidadAgua;
    }
    
        /**
     * @return the salinidadAgua
     */
    public float getSalinidadAgua() {
        return salinidadAgua;
    }

    /**
     * @param salinidadAgua the salinidadAgua to set
     */
    public void setSalinidadAgua(float salinidadAgua) {
        this.salinidadAgua = salinidadAgua;
    }
    
    @Override
    public String toString() {
        return "Nombre: " + getNombre() + "\n Precio: " + getPrecio() + "\n Fecha de envasado: " + getFechaEnvasado() + "\n Fecha de caducidad: " + getFechaCaducidad() + "\n Numero de lote: " + getNumeroLote() + "\n Pais de origen: " + getPaisOrigen() + "\n Temp. de mantenimiento: " + getTempMante() + "\n Salinidad del agua: " + getSalinidadAgua() + "\n";
    }
}
