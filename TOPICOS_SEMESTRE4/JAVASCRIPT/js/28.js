//Async, await

function descargarNuevosClientes (){
    return new Promise (resolve => {
        console.log('Descargando Clientes....., espere....')

        setTimeout(()=>{
            resolve('Los clientes fueron descargados')
        },  //TIEMPO (MILISEGUNDOS) (5segundos)
        5000)
    })
}

function descargarUltimosPedidos (){
    return new Promise (resolve => {
        console.log('Descargando Pedidos....., espere....')

        setTimeout(()=>{
            resolve('Los Pedidos fueron descargados')
        }, //TIEMPO (MILISEGUNDOS) (3segundos)
        3000)
    })
}

async function app(){
    try {
        //const clientes = await descargarNuevosClientes()
        //const pedidos = await descargarUltimosPedidos()
        //console.log(clientes)
        //console.log(pedidos)

        const resultados = await Promise.all([descargarNuevosClientes(), descargarUltimosPedidos()]);

        //MOSTRAR LOS VALORES DE CADA UNO DEL ARREGLO
        console.log(resultados[0]);
        console.log(resultados[1]);

    } catch (error) {
        console.log(error)
    }
}

app();
