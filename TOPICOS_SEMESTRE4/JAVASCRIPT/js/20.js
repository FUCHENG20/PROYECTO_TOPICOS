const carrito = [
    {nombre: 'Pelota', precio: 80},
    {nombre: 'Laptop', precio: 8000},
    {nombre: 'Huawei', precio: 5000},
    {nombre: 'Mouse', precio: 350},
    {nombre: 'Teclado', precio: 500},
]


carrito.forEach(
    function(producto){
        console.log(producto);
    }
);

//CONCATENAR
carrito.forEach(
    function(producto){
        console.log(`El Nombre del Producto es ${producto.nombre}`);
    }
);

//ARROW FUNCTION FOREACH (CUANDO QUIERO RECORRER UN ARREGLO)
//carrito.forEach(producto => console.log(producto.nombre));

//ARROW FUNCTION MAP (ME DA UNA POSIBILIDAD DE SACAR LA INFORMACION DE UN ARREGLO PARA OTRO ARREGLO)
//carrito.map(producto => console.log(producto.nombre));

const arreglo1 = carrito.forEach(producto => producto.nombre);

//CONSTRUIR UN ARREGLO
const arreglo2 = carrito.map(producto => `${producto.nombre} - ${producto.precio}`);

//console.log(arreglo1);
console.log(arreglo2);

//MAP: CONVIERTE, GENERA ARREGLOS NUEVOS DE MI PROPIO ARREGLO
