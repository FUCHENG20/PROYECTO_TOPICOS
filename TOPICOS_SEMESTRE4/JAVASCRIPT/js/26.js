// PROMISES

const usuarioAutentificado = new Promise((resolve,reject) => {
    const auth = false;
    if(auth){
        resolve('Usuario Autentificado'); //EL PROMISE SE CUMPLE
    }else{
        reject('No se puede Iniciar Sesion'); //EL PROMISE NO SE CUMPLE
    }
    
});

usuarioAutentificado
    .then(resultado => console.log(resultado))
    .catch(error => console.log(error))


//EN LOS PROMISE EXISTEN 3 VALORES
// Pending: NO SE HA CUMPLIDO PERO TAMPOCO SE HA RECHAZADO
// Fullfiled: YA SE CUMPLIO
// Rejected: NO SE CUMPLIO