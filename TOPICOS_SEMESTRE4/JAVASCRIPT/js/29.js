//FETCH API
//AJAX - Permite Enviar Informacion al Servidor u Obtener Informacion de un Servidor
//Podemos obtener un archivo o una respuesta de un Servidor (texto o JSON)
//Al Igual que en otras API'S Javascript utiliza PROMISSES o ASYNC/AWAIT

//QUE ES JSON? 
//JSON = JavaScript Object Notation

//Un JSON puede ser creado en cualquier lenguaje y se puede consumir en JavaScript por medio de FETCH API y poderlo mostrar en un sitio WEB

function obtenerEmpleados() {
    const archivo = '1.json';
    fetch(archivo)
        //Ve y realiza la busqueda, si lo encuentras conviertelo en json
        .then(resultado => {
            return resultado.json();
        })
        //Luego lo vamos a leer en datos para que lo imprima
        .then(datos => {
            //console.log(datos)

            const { empleados } = datos;
            //console.log(empleados)

            empleados.forEach(personal => {
                console.log(personal.id, personal.nombre, personal.puesto)
            });

        })
}

obtenerEmpleados();



