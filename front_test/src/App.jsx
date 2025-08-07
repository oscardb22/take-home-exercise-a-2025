import { useState, createContext } from 'react'
import Login from './components/Login'
import Header from './components/Header'
import Footer from './components/Footer'
import AuthProvider from './AuthProvider'
import { BrowserRouter,Routes, Route } from 'react-router-dom'
import Dashboard from './components/dashboard/Dashboard'
import ParkingFreeSpots from './components/parking/ParkingFreeSpots'
import PrivateRouter from './PrivateRouter'
import PublicRouter from "./PublicRouter"
import './assets/css/App.css'

const UserContext = createContext()

function App() {
  const [count, setCount] = useState(0)

return (
    <>
      <AuthProvider>
        <BrowserRouter>
          <Header/>
            <Routes>
              <Route path='/' element={<Login />}/>
              <Route path='/login' element={<PublicRouter><Login /></PublicRouter>}/>
              <Route path='/dashboard' element={<PrivateRouter><Dashboard /></PrivateRouter>}/>


              <Route path='/free_spots/:garage_id' element={<PrivateRouter><ParkingFreeSpots /></PrivateRouter>}/>
              <Route path='/historical' element={<PrivateRouter><Dashboard /></PrivateRouter>}/>
              <Route path='*' element={<PublicRouter><Login /></PublicRouter>}/>
            </Routes>
          <Footer/>
        </BrowserRouter>
      </AuthProvider>
    </>
  )
}

export default App
