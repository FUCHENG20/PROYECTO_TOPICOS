//POO - CLASES

class vehiculo {
    constructor(numLlantas, numPuertas, color){
        this.numLlantas = numLlantas
        this.numPuertas = numPuertas
        this.color = color
    }

    describirVehiculo(){
        return `Soy un vehiculo de ${this.numLlantas} Llantas`;
    }
}

class carro{
    constructor(numLlantas, numPuertas, color, modelo, numCilindros){
        this.numLlantas = numLlantas
        this.numPuertas = numPuertas
        this.color = color
        this.modelo = modelo
        this.numCilindros = numCilindros
    }

    describirCarro(){
        return `Soy un Carro ${this.modelo} de color ${this.color} con ${this.numLlantas} Llantas`;
    }
}

const bici = new vehiculo(2,0,"Rojo");

const honda = new carro(4 , 4 ,"Azul","Honda", 4)

const mazda = new carro(4 , 4 , "Morado", "Mazda", 8)

console.log(bici.describirVehiculo());

console.log(honda.describirCarro());
console.log(mazda.describirCarro());