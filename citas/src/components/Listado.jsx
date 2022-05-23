import React from 'react'
import { Paciente } from './Paciente'

export const Listado = ({ pacientes, setPaciente, eliminarPaciente }) => {
    return (
        <div className='bg-slate-700 border-2 mt-10 md:mt-0 md:ml-3 mx-10 md:mx-10 p-10 rounded-3xl mb-10 overflow-y-scroll md:h-screen md:w-1/2 lg:w-3/5' >

            <div>
                <h2 className='bg-white text-xl border-2 border-black p-1 text-center rounded-lg text-black sm:text-3xl sm: font-bold'>Listado Pacientes</h2>
                <p className=' mt-5 text-sm sm:text-xl sm:font-bold'>Administra tus <span className='font-bold text-sm text-emerald-500 sm:text-xl sm:font-bold'>Pacientes y Citas</span></p>
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
