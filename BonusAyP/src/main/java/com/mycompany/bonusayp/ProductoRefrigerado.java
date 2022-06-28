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
    
    private String codigoOrganismo;
    private float tempMante;
    
    public ProductoRefrigerado (String nombre, float precio, String fechaEnvasado, String fechaCaducidad, int numeroLote, String paisOrigen, String codigoOrganismo, float tempMante){
        super(nombre, precio, fechaEnvasado, fechaCaducidad, numeroLote, paisOrigen);
        this.codigoOrganismo = codigoOrganismo;
        this.tempMante = tempMante;
    }
    
    /**
     * @return the codigoOrganismo
     */
    public String getCodigoOrganismo() {
        return codigoOrganismo;
    }

    /**
     * @param codigoOrganismo the codigoOrganismo to set
     */
    public void setCodigoOrganismo(String codigoOrganismo) {
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
    
    @Override
    public String toString() {
        return "Nombre: " + getNombre() + "\n Precio: " + getPrecio() + "\n Fecha de envasado: " + getFechaEnvasado() + "\n Fecha de caducidad: " + getFechaCaducidad() + "\n Numero de lote: " + getNumeroLote() + "\n Pais de origen: " + getPaisOrigen() + "\n Codigo de organismo: " + getCodigoOrganismo() + "\n Temp. de mantenimiento: " + getTempMante() + "\n";
    }
}
