import React from "react"
import { Link } from "react-router-dom"
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome"

const Button = (props) => {
  return (
    <>
    {props.iconData ? 
    <Link className={`btn ${props.classData}`} to={props.urlTo}><FontAwesomeIcon icon={props.iconData} /></Link>
    :
    <Link className={`btn ${props.classData}`} to={props.urlTo}>{props.text}</Link>
    }
    </>
  )
}

export default Button