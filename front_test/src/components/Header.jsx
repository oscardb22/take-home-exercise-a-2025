import React, { useContext } from 'react'
import Button from "./Button"
import { Link } from 'react-router-dom'
import { AuthContext } from "../AuthProvider"
import { useNavigate } from 'react-router-dom'

function Header() {
  const {isLoggedIn, setIsLoggedIn} = useContext(AuthContext)
  const navigate = useNavigate()
  const handleLogout = () => {
    localStorage.removeItem("accessToken")
    localStorage.removeItem("refreshToken")
    setIsLoggedIn(false)
    navigate("/login")
  }
  return (
    <>
    <nav className='navbar container pt-3 pb-3 align-items-start customNav'>
        <Link className='navbar-brand text-light' to="/" >Vite + React + Django</Link>
        <div>
          {isLoggedIn ? (
            <>
              <Button text="Historical" classData="btn-outline-success" urlTo="/historical"/>
              &nbsp;
              <Button text="Dasboard" classData="btn-outline-info" urlTo="/dashboard"/>
              &nbsp;
              <button className='btn btn-outline-danger' onClick={handleLogout}>Logout</button>
            </>
          ): null}
        </div>
    </nav>
    </>
  )
}

export default Header