import { useState } from 'react'
import reactLogo from './assets/react.svg'
import './App.css'
import { SideBar } from './components/sidebar'
import Avatar from '@mui/material/Avatar/Avatar'

function App() {
  const [count, setCount] = useState(0)

  return (
    <div>
    <Avatar alt="Travis Howard" src="./assets/react.svg" />
    <SideBar />
      </div>)
}

export default App
