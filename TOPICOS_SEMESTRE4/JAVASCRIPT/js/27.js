
const boton = document.querySelector('#boton')

boton.addEventListener('click', () => {Notification.requestPermission() .then(resultado => console.log(resultado))})

if( Notification.permission == 'granted'){
    new Notification('Esta es una Notificacion', {
        icon: 'img/pug.jpg',
        body: 'Gracias por Visitar'
    })
}