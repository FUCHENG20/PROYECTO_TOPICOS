import { useEffect, useState } from 'react'
import logo from './logo.svg'
import './App.css'
import { Cabecera } from './components/Cabecera'
import { Formulario } from './components/Formulario'
import { Listado } from './components/Listado'

function App() {

  const [pacientes, setPacientes] = useState([])
  const [paciente, setPaciente] = useState({})

  useEffect(() => {
    const pacientesLocalStorage = localStorage.getItem('Pacientes')
  })

  useEffect(() => {
    localStorage.setItem('Pacientes', JSON.stringify(pacientes));
  }, [pacientes]);

  const eliminarPaciente = (id) => {
    console.log('Eliminando Paciente: ' + id);
    const pacientesActualizados = pacientes.filter(remplazo => remplazo.id !== id);

    setPacientes(pacientesActualizados)
  };

  return (
    <div className='text-[#85BBB2]'>
      <Cabecera />
      <div className='mt-3 md:flex w-full'>
        <Formulario
          setPacientes={setPacientes}
          pacientes={pacientes}
          paciente={paciente}
          setPaciente={setPaciente}
        />
        <Listado
          pacientes={pacientes}
          setPaciente={setPaciente}
          eliminarPaciente={eliminarPaciente}
        />
      </div>
    </div>
  )
}

export default App
