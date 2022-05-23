import { useState, useEffect } from 'react';

export const Formulario = ({ setPacientes, pacientes, paciente, setPaciente }) => {

    //DEFINIR EL ESTADO PARA LOS CAMPOS
    const [nombre, setNombre] = useState("");
    const [correo, setCorreo] = useState("");
    const [fecha, setFecha] = useState("");
    const [sintomas, setSintomas] = useState("");

    const [error, setError] = useState(false)

    useEffect(() => {

        if (Object.keys(paciente).length > 0) {
            setNombre(paciente.nombre);
            setCorreo(paciente.correo);
            setFecha(paciente.fecha);
            setSintomas(paciente.sintomas);
        }


    }, [paciente]);

    const generarID = () => {
        const random = Math.random().toString(16).substring(2);
        const fecha = Date.now().toString(36);
        return random + fecha;
    }

    const validarFormulario = (e) => {
        e.preventDefault();

        if ([nombre, correo, sintomas, fecha].includes('')) {
            setError(true);
            return
        }
        //SE COLOCA EL ERROR EN FALSO PARA INDICAR QUE TODOS LOS CAMPOS ESTAN LLENOS
        setError(false)

        const objetoPaciente = {
            nombre,
            correo,
            fecha,
            sintomas
        };


        if (paciente.id) {
            //ACTUALIZAMOS PACIENTES
            objetoPaciente.id = paciente.id

            const pacientesActualizados = pacientes.map(remplazo => (remplazo.id === paciente.id ? objetoPaciente : remplazo));
            setPacientes(pacientesActualizados)
            setPaciente({});
        }
        else {
            // AGREGAMOS PACIENTES
            objetoPaciente.id = generarID();
            setPacientes([...pacientes, objetoPaciente]);
        }

        const limpiarDatos = () => {
            setNombre("");
            setCorreo("");
            setFecha("");
            setSintomas("");
        };

        limpiarDatos();

    }


    return (
        <div className='bg-slate-700 border-2 rounded-3xl mx-10 md:mr-3 p-10 mb-auto md:w-1/2 lg:w-2/5'>
            {error && <p className='bg-red-700 text-white font-bold p-2 rounded-lg mb-4 text-center'>DEBES DE LLENAR LOS CAMPOS</p>}
            <div>
                <h2 className='bg-white border-2 border-black text-3xl p-1 mb-6 text-center rounded-lg text-black'>Formulario</h2>
            </div>
            <form action="" onSubmit={validarFormulario}>
                <div className='mb-3 font-bold'>
                    <label >Nombre Paciente</label>
                    <input className='block w-full rounded-lg placeholder:nombre paciente text-black p-2' placeholder="nombre paciente" type="text" id='nombre' value={nombre} onChange={(e) => setNombre(e.target.value)} />
                </div>

                <div className='mb-3 font-bold'>
                    <label>Correo</label>
                    <input className='block w-full rounded-lg text-black p-2' placeholder="correo electrónico" type="email" name='correo' value={correo} onChange={(e) => setCorreo(e.target.value)} />
                </div>

                <div className='mb-3 font-bold'>
                    <label>Fecha Cita</label>
                    <input className='block w-full rounded-lg text-black p-2' type="date" name='fecha' value={fecha} onChange={(e) => setFecha(e.target.value)} />
                </div>

                <div className='mb-3 font-bold'>
                    <label>Síntomas</label>
                    <textarea className='block w-full rounded-lg text-black p-2 mb-4' name="sintomas" id="" cols="30" rows="5" placeholder="síntomas" value={sintomas} onChange={(e) => setSintomas(e.target.value)}></textarea>
                </div>

                <div>
                    <input className="bg-slate-700 border-2 rounded-2xl font-bold mt-5 w-full p-2 hover:cursor-pointer hover:bg-slate-800" type="submit" id='submit' value={paciente.id ? 'ACTUALIZAR PACIENTE' : 'AGREGAR'} />
                </div>
            </form >
        </div >

    )
}
