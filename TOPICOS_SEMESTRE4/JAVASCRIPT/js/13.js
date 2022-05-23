//METODOS DE FUNCION
const reproductor = {
    reproducir : function(id){
        console.log(`Reproduciendo ${id}`);
    },
    pausar : function (){
        console.log("Pausando.....");
    },
    crearPlayList : function(nombre){
        console.log(`Creando la PlayList ${nombre}`)
    },
    reproducirPlayList : function(nombre){
        console.log(`Reproduciendo la PlayList ${nombre}`)
    }
}

reproductor.borrarCancion = function(id){
    console.log(`Eliminando la Cancion ${id}`);
}


reproductor.reproducir(40);

reproductor.pausar();

reproductor.borrarCancion(40);

reproductor.crearPlayList("Mis Favoritas");

reproductor.reproducirPlayList("Mis Favoritas");