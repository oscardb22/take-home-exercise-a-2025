import React from 'react'
import { useState, useContext } from 'react'
import LocalAxios from "../api/axios"
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faSpinner } from '@fortawesome/free-solid-svg-icons'
import { useNavigate } from 'react-router-dom'
import { AuthContext } from "../AuthProvider"

const Login = () => {
    const {isLoggedIn, setIsLoggedIn} = useContext(AuthContext)
    const [errorData, setErrorData] = useState({})
    const navigate = useNavigate()
    const [responseData, setResponseData] = useState({})
    const [loadingData, setLoadingData] = useState(false)
    const [formData, setFormData] = useState({
            email: "",
            password: ""
        })
    const handleChange = (e) => {
        setFormData({...formData, [e.target.name]: e.target.value})
    }
    const handleFromSubmit = async (e) => {
        e.preventDefault()
        setIsLoggedIn(false)
        setLoadingData(true)
        setErrorData({})
        setResponseData({})
        await LocalAxios.post(`authentication/token/`, formData).then((response)=>{
            setErrorData({})
            setResponseData(response)
            setIsLoggedIn(true)
            localStorage.setItem("accessToken", response.data.access)
            localStorage.setItem("refreshToken", response.data.refresh)
            navigate("/dashboard")
            //sessionStorage.setItem("accessToken", response.data.access)
            //sessionStorage.setItem("refreshToken", response.data.refresh)
        }).catch((error) =>{
            setResponseData({})
            setErrorData(error.response.data)
            setIsLoggedIn(false)
        }).finally(()=>{
            setLoadingData(false)
        })
    }
  return (
    <>
        <div className='container'>
            <div className='row justify-content-center'>
                <div className='col-md-6 bg-light-dark p-5 rounded'>
                    <h3 className='text-light text-center mb-4'>Login</h3>
                    <small>{errorData.non_field_errors && <div className='text-danger'>{errorData.non_field_errors}</div>}</small>
                    <form onSubmit={handleFromSubmit}>
                        <div className='mb-3'>
                            <input className='form-control' value={formData.email} onChange={handleChange} type="text" name='email' placeholder='Enter your Email Address' required/>
                            <small>{errorData.email && <div className='text-danger'>{errorData.email}</div>}</small>
                        </div>
                        <div className='mb-3'>
                            <input  className='form-control' value={formData.password} onChange={handleChange} type="password" name="password" id="password" placeholder='Set a good password' required/>
                            <small>{errorData.password && <div className='text-danger'>{errorData.password}</div>}</small>
                        </div>
                        {isLoggedIn && <div className='alert alert-success'>Login Successfull</div>}
                        {loadingData ?(
                            <button type="buttom" className='btn btn-info d-block mx-auto' disabled><FontAwesomeIcon icon={faSpinner} spin/> Logging in ...</button>
                        ):(
                            <button type="submit" className='btn btn-info d-block mx-auto'>Enter</button>
                        )}
                    </form>
                </div>
            </div>
        </div>
    </>
  )
}

export default Login