import React from 'react'
import { Paciente } from './Paciente'

export const Listado = ({ pacientes, setPaciente, eliminarPaciente }) => {
    return (
        <div className='bg-slate-700 mr-10 ml-10 p-10 rounded-lg xl:w-auto mb-10 overflow-y-scroll md:h-screen' >

            <div>
                <h2 className='bg-green-700 text-3xl p-1 text-center rounded-lg text-green-100'>Listado Pacientes</h2>
                <p className='text-xl mt-5'>Administra tus <span className='font-bold text-emerald-600'>Pacientes y Citas</span></p>
            </div>

            {pacientes.map(paciente => (
                <Paciente
                    key={paciente.id}
                    paciente={paciente}
                    setPaciente={setPaciente}
                    eliminarPaciente={eliminarPaciente}
                />
            ))}

        </div>
    )
}
