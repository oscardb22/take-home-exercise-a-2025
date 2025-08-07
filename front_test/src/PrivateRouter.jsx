import {useContext, useEffect} from 'react'
import { AuthContext } from './AuthProvider'
import { Navigate } from 'react-router-dom'
import LocalAxios from "./api/axios"
import { useNavigate } from 'react-router-dom'

const PrivateRouter = ({children}) => {
    const { isLoggedIn, setIsLoggedIn } = useContext(AuthContext)
    const navigate = useNavigate()
    useEffect(() => {
        const fetchProtectedData = async () => {
            try{
                await LocalAxios.get(`authentication/protected-view/`)
            }catch(error){
                console.error("PrivateRouter", error)
                setIsLoggedIn(false)
                localStorage.removeItem("accessToken")
                localStorage.removeItem("refreshToken")
                navigate("/login")
            }
        }
        fetchProtectedData()
      }, [navigate, setIsLoggedIn])
  return isLoggedIn ? children : <Navigate to="/login" />
}

export default PrivateRouter
