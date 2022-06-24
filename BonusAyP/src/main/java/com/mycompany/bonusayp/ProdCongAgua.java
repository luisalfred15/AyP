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
    
    public ProdCongAgua(String nombre, float precio, String fechaCaducidad, int numeroLote, String fechaEnvasado, String paisOrigen, float tempMante, float salinidadAgua) {
        super(nombre, precio, fechaCaducidad, numeroLote, fechaEnvasado, paisOrigen, tempMante);
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
}
