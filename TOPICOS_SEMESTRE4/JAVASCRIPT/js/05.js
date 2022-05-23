//Objetos: ACCESO A DATOS POR PROPIEDAD vs DESTRUCTURING

const persona = {
    nombre: 'Fucheng',
    genero: 'Hombre',
    edad: '20'

}

//ACCESO A DATOS POR PROPIEDAD
//FORMA 1
console.log("\nFORMA 1 PARA ACCEDER A LOS DATOS")
console.log(persona.nombre)
console.log(persona.genero)

const nombrePersona = persona.nombre4
console.log(nombrePersona)

//FORMA 2
console.log("\nFORMA 2 PARA ACCEDER A LOS DATOS")
console.log(persona["nombre"])
console.log(persona["genero"])

const edadPersona = persona["nombre"]
console.log(edadPersona)

//ACCESO A DATOS USANDO DESTRUCTURING
const{nombre,genero,edad} = persona
console.log('\n ACCESO A DATOS POR DESTRUCTURING')
console.log(nombre)

//AGREGAR PROPIEDAD AL OBJETO
persona.peso = 70

console.log(persona)