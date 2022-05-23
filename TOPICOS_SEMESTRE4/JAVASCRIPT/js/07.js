//INVOCANDO LA EJECUCION ESTRICTA DE JS
"use strict"

//Objetos: 
const persona = {
    nombre: 'Fucheng',
    genero: 'Hombre',
    edad: '20'

}

const medidas = {
    peso: 80,
    estatura: 165
}

//USANDO EL OPERADOR ... SPREAD OPERATOR
const datosVolibolista = {...persona, ...medidas}
console.log(datosVolibolista)
