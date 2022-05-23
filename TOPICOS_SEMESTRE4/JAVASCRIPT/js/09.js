const meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo']

const carrito = [
    {nombre: 'Pelota', precio: 80},
    {nombre: 'Laptop', precio: 8000},
    {nombre: 'Huawei', precio: 5000},
    {nombre: 'Mouse', precio: 350},
    {nombre: 'Teclado', precio: 500},
]

//PREGUNTAR SI ESTA MARZO EN EL ARRAY MESES

meses.forEach(function (meses){
    if (meses === 'Marzo') {
        console.log('Si esta en el Array')    
    }
})

//OTRA MANERA DE PREGUNTAR SI HAY UN ELEMENTO EN UN ARRAY

let resultado = meses.includes('Marzo')

//PARA BUSCAR EN UN ARRAY CON OBJETOS
resultado = carrito.some(
    function(producto){
        return producto.nombre === 'Laptop'
    }
)

//LO MISMO PERO CON ARROW FUNCTION
resultado = carrito.some(producto => producto.nombre === 'Laptop')

//CONTAR LOS PRECIOS
resultado = carrito.reduce(
    function (total,producto){
        return total + producto.precio
    }, 0
)

//CONTAR LOS PRECIOS CON ARROW FUNCTION
resultado = carrito.reduce((total, producto) => total + producto.precio, 0)

//FILTRAR ELEMENTOS
resultado = carrito.filter(
    function(producto){
        return producto.precio < 1000
    }
)

//FILTRAR ELEMENTOS CON ARROW FUNCTION
resultado = carrito.filter(producto => producto.precio < 1000)

//FILTRAR ELEMENTOS POR NOMBRE
resultado = carrito.filter(
    function(producto){
        return producto.nombre === 'Laptop'
    }
)


console.log(resultado)