//ARROW FUNCTION

//PARA DOS O MAS VARIABLE ES NECESARIO PONER ENTRE PARENTESIS
const sumar = (n1, n2) => console.log(n1 + n2);

sumar(20, 70);

//PARA UNA VARIABLE NO ES NECESARIO PONER ENTRE PARENTESIS
const cuadrado = num => console.log(num * num);

cuadrado(4);

const aprendiendo = tecnologia => console.log(`Estoy aprendiendo ${tecnologia} `);

aprendiendo("JavaScript");

const operaciones = (n1, n2) => {
    if(n1 > n2){
        console.log('N1 es mayor que N2')
    }
    else{
        console.log('N2 es el Mayor')
    }
}

operaciones(10,20);


