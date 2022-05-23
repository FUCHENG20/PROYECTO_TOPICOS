//FUNCIONES

//DECLARACION DE FUNCION
//SE PUEDE UTILIZAR EN CUALQUIER PARTE DEL ARCHIVO
//EJEMPLO suma1(100,100)

function suma1(a,b){
    console.log(a + b)
}

//EXPRESION DE FUNCION
//SOLAMENTE SE PUEDE UTILIZAR POR DEBAJO DE LA DECLARACION

const suma2 = function (){
    console.log(10 + 10)
}

suma2();

//FUNCIONES IIFE

(function(){
    console.log('Esta es una funcion')
}) ()

console.log(cliente)
