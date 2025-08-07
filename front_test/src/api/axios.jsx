import React, {useContext} from 'react'
import axios from "axios"
import { AuthContext } from "../AuthProvider"

const LocalAxios = axios.create({
    baseURL: import.meta.env.VITE_REACT_APP_BACK_END_URL,
    timeout: 1000,
    headers: {"Content-Type": "application/json"}
})
LocalAxios.interceptors.request.use(
    function(config){
        const accessToken = localStorage.getItem("accessToken")
        if(accessToken){
            config.headers["Authorization"] = `Bearer ${accessToken}`
        }
        return config
    },
    function(error){
        return Promise.reject(error)
    }
)
LocalAxios.interceptors.response.use(
    function(response){
        return response
    },
    async function(error){
        const {setIsLoggedIn} = useContext(AuthContext)
        const originalRequest = error.config
        if(error.response.status === 401 && !originalRequest.retry){
            originalRequest.retry = true
            const refreshToken = localStorage.getItem("refreshToken")
            try {
                const response = await LocalAxios.post(`authentication/token/refresh/`, {refresh: refreshToken})
                localStorage.setItem("accessToken", response.data.access)
                originalRequest.headers["Authorization"] = `Bearer ${response.data.access}`
                return LocalAxios(originalRequest)
            }catch(error){
                localStorage.removeItem("accessToken")
                localStorage.removeItem("refreshToken")
                setIsLoggedIn(false)
                console.error(error)
            }
        }
        return Promise.reject(error)
    }
)

export default LocalAxios
