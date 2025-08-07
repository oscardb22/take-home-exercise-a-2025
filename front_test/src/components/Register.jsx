import React from 'react'
import { useState } from 'react'

function Register() {
    const [formData, setFormData] = useState({
            fullName: "",
            email: "",
            password: ""
        })
        const handleChange = (e) => {
            setFormData({...formData, [e.target.name]: e.target.value})
        }
        const handleFromSubmit = (e) => {
            e.preventDefault()
            console.log("Submit data: ", formData)
        }
  return (
    <>
        <div className='container'>
            <div className='row justify-content-center'>
                <div className='col-md-6 bg-light-dark p-5 rounded'>
                    <h3 className='text-light text-center mb-4'>Create an Account</h3>
                    <form onSubmit={handleFromSubmit}>
                        <input className='form-control mb-3' value={formData.fullName} onChange={handleChange} type="text" name='fullName' placeholder='Enter your Full Name'/>
                        <input className='form-control mb-3' value={formData.email} onChange={handleChange} type="email" name='email' placeholder='Enter your Email Address'/>
                        <input  className='form-control mb-5' value={formData.password} onChange={handleChange} type="password" name="password" id="password" placeholder='Set a good password'/>
                        <button type="submit" className='btn btn-info d-block mx-auto'>Register</button>
                    </form>
                </div>
            </div>
        </div>
    </>
  )
}

export default Register