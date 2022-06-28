/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.mycompany.bonusayp;

/**
 *
 * @author luisa
 */
public class ProdCongAire extends ProductoCongelado {


    
    private float porcentajeN;
    private float porcentajeO;
    private float porcentajeC;
    private float porcentajeH2O;
    
    public ProdCongAire (String nombre, float precio, String fechaEnvasado, String fechaCaducidad, int numeroLote, String paisOrigen, float tempMante, float porcentajeN, float porcentajeO, float porcentajeC, float porcentajeH2O) {
        super(nombre, precio, fechaEnvasado, fechaCaducidad, numeroLote, paisOrigen, tempMante);
        this.porcentajeN = porcentajeN;
        this.porcentajeO = porcentajeO;
        this.porcentajeN = porcentajeN;
        this.porcentajeH2O = porcentajeH2O;
    }
    
        /**
     * @return the porcentajeN
     */
    public float getPorcentajeN() {
        return porcentajeN;
    }

    /**
     * @param porcentajeN the porcentajeN to set
     */
    public void setPorcentajeN(float porcentajeN) {
        this.porcentajeN = porcentajeN;
    }

    /**
     * @return the porcentajeO
     */
    public float getPorcentajeO() {
        return porcentajeO;
    }

    /**
     * @param porcentajeO the porcentajeO to set
     */
    public void setPorcentajeO(float porcentajeO) {
        this.porcentajeO = porcentajeO;
    }

    /**
     * @return the porcentajeC
     */
    public float getPorcentajeC() {
        return porcentajeC;
    }

    /**
     * @param porcentajeC the porcentajeC to set
     */
    public void setPorcentajeC(float porcentajeC) {
        this.porcentajeC = porcentajeC;
    }

    /**
     * @return the porcentajeH2O
     */
    public float getPorcentajeH2O() {
        return porcentajeH2O;
    }

    /**
     * @param porcentajeH2O the porcentajeH2O to set
     */
    public void setPorcentajeH2O(float porcentajeH2O) {
        this.porcentajeH2O = porcentajeH2O;
    }
    
    @Override
    public String toString() {
        return "Nombre: " + getNombre() + "\n Precio: " + getPrecio() + "\n Fecha de envasado: " + getFechaEnvasado() + "\n Fecha de caducidad: " + getFechaCaducidad() + "\n Numero de lote: " + getNumeroLote() + "\n Pais de origen: " + getPaisOrigen() + "\n Temp. de mantenimiento: " + getTempMante() + "\n Porcentaje de N: " + getPorcentajeN() + "\n Porcentaje de O: " + getPorcentajeO() + "\n Porcentaje de C: " + getPorcentajeC() + "\n Porcentaje de H2O: " + getPorcentajeH2O() + "\n";
    }
    
}
