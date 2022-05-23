//POO - CLASES - HERENCIA

//HERENCIA (PADRE)
class vehiculo {
    constructor(numLlantas, numPuertas, color){
        this.numLlantas = numLlantas
        this.numPuertas = numPuertas
        this.color = color
    }

    //SI HAY DOS METODOS IGUALES EN LA HERENCIA SE UTILIZA EL DE SI MISMO DE CADA UNO
    describirVehiculo(){
        return `Soy un vehiculo de color ${this.color} con ${this.numLlantas} Llantas`;
    }
}

//CREAR HERENCIA CON EXTENDS (HIJO)
class carro extends vehiculo{
    constructor(numLlantas, numPuertas, color, modelo, numCilindros){
        super(numLlantas, numPuertas, color)
        this.modelo = modelo
        this.numCilindros = numCilindros
    }

    describirCarro(){
        return `Soy un Carro ${this.modelo} de color ${this.color} con ${this.numLlantas} Llantas`;
    }

    //SI HAY DOS METODOS IGUALES EN LA HERENCIA SE UTILIZA EL DE SI MISMO DE CADA UNO
    describirVehiculo(){
        return `Soy un ${this.modelo} de color ${this.color} con ${this.numLlantas} Llantas y ${this.numCilindros} Cilindros`;

        //PARA ACCESAR A LA DEL PADRE
        //return super.describirVehiculo()
    }
}

const honda = new vehiculo(4, 4, "Rojo")

const mazda = new carro(4, 4 , "Azul", "Mazda", 4)

console.log(honda.describirVehiculo())

console.log(mazda.describirVehiculo())
