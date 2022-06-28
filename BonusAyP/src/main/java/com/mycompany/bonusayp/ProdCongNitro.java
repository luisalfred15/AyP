/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.mycompany.bonusayp;

/**
 *
 * @author luisa
 */
public class ProdCongNitrogeno extends ProductoCongelado {

    private String metodoCongelacion;
    private int tiempoExposicionN;
    
    public ProdCongNitrogeno(String nombre, float precio, String fechaCaducidad, int numeroLote, String fechaEnvasado, String paisOrigen, float tempMante, String metodoCongelacion, int tiempoExposicionN){
        super(nombre, precio, fechaCaducidad, numeroLote, fechaEnvasado, paisOrigen, tempMante);
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
    
    
}
