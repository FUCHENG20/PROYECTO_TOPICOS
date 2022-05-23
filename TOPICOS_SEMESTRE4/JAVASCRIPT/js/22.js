//POO

//OBJETO LITERAL

const producto = {
    nombre: 'Tablet',
    precio: 500
}

//OBJECTO CONSTRUCTOR 
//(CUANDO EMPIEZA CON MAYUSCULA SON CLASES Y MINUSCULA METODOS O FUNCIONES)
function Producto(nombre, precio){
    this.nombre = nombre;
    this.precio = precio;
}

const producto2 = new Producto('TV', 500);
console.log(producto2);

