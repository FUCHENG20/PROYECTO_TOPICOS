//SWITCH

const metodoDePago = 'tarjeta';

switch(metodoDePago){
    case 'tarjeta':
        console.log('Pagastes con Tarjeta');
        break;

    default:
        console.log('Aun no has pagado');
        break;
}