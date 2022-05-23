import React from 'react'
import { Paciente } from './Paciente'

export const Listado = ({ pacientes, setPaciente, eliminarPaciente }) => {
    return (
        <div className='bg-slate-700 mx-10 md:mt-0 mt-5 p-10 rounded-lg mb-10 overflow-y-scroll md:h-screen md:w-1/2 lg:w-3/5' >

            <div>
                <h2 className='bg-white text-3xl p-1 text-center rounded-lg text-black'>Listado Pacientes</h2>
                <p className='text-xl mt-5'>Administra tus <span className='font-bold text-emerald-500'>Pacientes y Citas</span></p>
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
