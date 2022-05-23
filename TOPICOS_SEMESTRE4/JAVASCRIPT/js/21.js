// this en JAVASCRIPT

//DEFINIR LA VARIABLE DESDE LA VENTANA
window.nombre = 'Fucheng';
window.total = 50;

const reservacion = {
    nombre: 'Pedrito',
    apellido: 'Sola',
    total: 5000,
    pagado: false,
    informacion : function(){
        //NADA MAS HACE REFERENCIA AL OBEJTO
        console.log(this)
        console.log(`El Cliente ${reservacion.nombre} reservo y debe pagar ${reservacion.total}`)
    }
}

const reservacion2 = {
    nombre: 'Pedrito',
    apellido: 'Sola',
    total: 5000,
    pagado: false,
    informacion : () => {
        //HACE REFERENCIA A TODO EL ARCHIVO
        console.log(this)
        console.log(`El Cliente ${this.nombre} reservo y debe pagar ${this.total}`)
    }
}

reservacion.informacion();

reservacion2.informacion();