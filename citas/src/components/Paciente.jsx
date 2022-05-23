import React from 'react'

export const Paciente = ({ paciente, setPaciente, eliminarPaciente }) => {

    const handleEliminar = () => {
        const respuesta = confirm('Deseas Eliminarlo?')
        if (respuesta) {
            eliminarPaciente(paciente.id);
        }
    }

    return (
        <div>
            <div className='mt-5 shadow-md bg-white rounded-lg p-8 uppercase mb-3 sm:p-10'>
                <p className='text-gray-700 font-bold text-xs sm:text-lg'>Nombre Paciente: <span className='font-normal normal-case'>{paciente.nombre}</span></p>
                <p className='text-gray-700 font-bold text-xs sm:text-lg'>Email: <span className='font-normal normal-case'>{paciente.correo}</span></p>
                <p className='text-gray-700 font-bold text-xs sm:text-lg'>Fecha: <span className='font-normal normal-case'>{paciente.fecha}</span></p>
                <p className='text-gray-700 font-bold text-xs sm:text-lg'>Síntomas: <span className='font-normal normal-case'>{paciente.sintomas}</span></p>
                <div>
                    <input className="bg-green-500 text-white border-2 rounded-2xl w-1/2 p-2 mt-6 hover: cursor-pointer hover:bg-green-400" type="submit" value="Editar" onClick={() => setPaciente(paciente)} />
                    <input className="bg-red-700 text-white border-2 rounded-2xl w-1/2 p-2 mt-6 hover:cursor-pointer hover:bg-red-600" type="submit" value="Eliminar" onClick={handleEliminar} />
                </div>
            </div>
        </div>
    )
}

