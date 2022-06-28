/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.mycompany.bonusayp;

/**
 *
 * @author luisa
 */
public abstract class ProductoCongelado extends Producto {

    private float tempMante;
    
    public ProductoCongelado(String nombre, float precio, String fechaEnvasado, String fechaCaducidad, int numeroLote, String paisOrigen, float tempMante) {
        super(nombre, precio, fechaEnvasado, fechaCaducidad, numeroLote, paisOrigen);
        this.tempMante = tempMante;
    }
   
        /**
     * @return the tempMante
     */
    public float getTempMante() {
        return tempMante;
    }

    /**
     * @param tempMante the tempMante to set
     */
    public void setTempMante(float tempMante) {
        this.tempMante = tempMante;
    }

}
