/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.mycompany.bonusayp;

/**
 *
 * @author luisa
 */
public class ProductoRefrigerado extends Producto {
    
    private int codigoOrganismo;
    private float tempMante;
    
    public ProductoRefrigerado (String nombre, float precio, String fechaCaducidad, int numeroLote, String fechaEnvasado, String paisOrigen, int codigoOrganismo, float tempMante){
        super(nombre, precio, fechaCaducidad, numeroLote, fechaEnvasado, paisOrigen);
        this.codigoOrganismo = codigoOrganismo;
        this.tempMante = tempMante;
    }
    
    /**
     * @return the codigoOrganismo
     */
    public int getCodigoOrganismo() {
        return codigoOrganismo;
    }

    /**
     * @param codigoOrganismo the codigoOrganismo to set
     */
    public void setCodigoOrganismo(int codigoOrganismo) {
        this.codigoOrganismo = codigoOrganismo;
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
    public void setTempMante(int tempMante) {
        this.tempMante = tempMante;
    }
}
