//INVOCANDO LA EJECUCION ESTRICTA DE JS
"use strict"

//Objetos: MODIFICANDO, ELIMINANDO, CONGELANDO Y SELLANDO PROPIEDADES
const persona = {
    nombre: 'Fucheng',
    genero: 'Hombre',
    edad: '20'

}

//AGREGAR UNA PROPIEDAD NUEVO AL OBJETO
persona.peso = 70
console.log(persona)

//ELIMINANDO UNA PROPIEADAD DEL OBJETO
delete persona.edad
console.log(persona)

//CONGELANDO EL OBJETO
//Object.freeze(persona)

//persona.estatura = 1.70
//console.log(persona)

//SELLANDO EL OBJETO PERMITE MODIFICAR LOS DATOS PERO NO AGREGAR NI ELIMINAR
Object.seal(persona)
persona.nombre = 'Zhou'
console.log(persona)


