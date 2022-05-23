//Uso de Arreglos: Crear un Arreglo
const numero = [12,14,16,18,20,22]

console.log('Recorrido C/u')
console.log(numero[0])
console.log(numero[1])
console.log(numero[2])
console.log(numero[3])
console.log(numero[4])


//RECORRER EL ARREGLO CON FUNTION 
console.log('Recorrido con Funcion')
numero.forEach(function (num){
    console.log(num)
})

console.log('Recorrido con ArrowFunction')
numero.forEach(num => console.log(num))

//AGREGAR ELEMENTOS AL FINAL DEL ARREGLO CON PUSH
numero.push(100)

//IMPRESION DEL ARREGLO EN UNA TALBLA
console.table(numero)

//AGREGAR ELEMENTOS AL INICIO DEL ARREGLO CON UNSHIFT
numero.unshift(-10,0)
console.table(numero)

//SACA UN ELEMENTO DEL ARREGLO
numero.pop()
console.table(numero)

//ELIMINA EL PRIMER ELEMENTO DEL ARREGLO CON EL SHIFT
let primerNumero = numero.shift()
console.log(`El primer valor en el arreglo fue: ${primerNumero}`)
//IMPRESION DEL ARREGLO EN UNA TABLA
console.table(numero)


const meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo']

//ELIMINAR ELEMENTOS A PARTIR DE UNA POSICION
//meses.splice(2,1)

//HACER UNA COPIA DEL OBJETO
let nuevosMeses = ['Diciembre',...meses,'Junio']

//ELIMINAR ELEMENTOS DEL ARRAY



console.log(nuevosMeses)



