/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.mycompany.bonusayp;

/**
 *
 * @author luisa
 */
public class ProdCongNitro extends ProductoCongelado {

    private String metodoCongelacion;
    private int tiempoExposicionN;
    
    public ProdCongNitro(String nombre, float precio, String fechaEnvasado, String fechaCaducidad, int numeroLote, String paisOrigen, float tempMante, String metodoCongelacion, int tiempoExposicionN){
        super(nombre, precio, fechaEnvasado, fechaCaducidad, numeroLote, paisOrigen, tempMante);
        this.metodoCongelacion = metodoCongelacion;
        this.tiempoExposicionN = tiempoExposicionN;
    }
    
    /**
     * @return the metodoCongelacion
     */
    public String getMetodoCongelacion() {
        return metodoCongelacion;
    }

    /**
     * @param metodoCongelacion the metodoCongelacion to set
     */
    public void setMetodoCongelacion(String metodoCongelacion) {
        this.metodoCongelacion = metodoCongelacion;
    }

    /**
     * @return the tiempoExposicionN
     */
    public int getTiempoExposicionN() {
        return tiempoExposicionN;
    }

    /**
     * @param tiempoExposicionN the tiempoExposicionN to set
     */
    public void setTiempoExposicionN(int tiempoExposicionN) {
        this.tiempoExposicionN = tiempoExposicionN;
    }
    
    @Override
    public String toString() {
        return "Nombre: " + getNombre() + "\n Precio: " + getPrecio() + "\n Fecha de envasado: " + getFechaEnvasado() + "\n Fecha de caducidad: " + getFechaCaducidad() + "\n Numero de lote: " + getNumeroLote() + "\n Pais de origen: " + getPaisOrigen() + "\n Temp. de mantenimiento: " + getTempMante() + "\n Metodo de congelacion: " + getMetodoCongelacion() + "\n Tiempo de congelacion: " + getTiempoExposicionN() + "\n";
    }
}
