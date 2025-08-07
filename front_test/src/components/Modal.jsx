import React from "react"
import { useState, useContext, useEffect } from 'react'
import LocalAxios from "../api/axios"
import { useNavigate } from 'react-router-dom'
import { AuthContext } from "../AuthProvider"
import '../assets/css/Modal.css'

const Modal = (props) => {
    const [time, setTime] = useState(10 * 60);
    const [plate, setPlate] = useState("");
    const [errorData, setErrorData] = useState({})
    const navigate = useNavigate()
    const [responseData, setResponseData] = useState({})
    const [loadingData, setLoadingData] = useState(false)
    const [formData, setFormData] = useState({
            garage: "",
            day: "",
            start_time: "",
            end_time: "",
            plate: "",
            uuid: ""
        })
    const handleChange = (e) => {
        setFormData({
            garage: props.dataTo.garage,
            day: props.dataTo.day,
            start_time: props.dataTo.start_time,
            end_time: props.dataTo.end_time,
            uuid: props.dataTo.uuid,
            [e.target.name]: e.target.value,
        })
    }

  useEffect(() => {
    if (time <= 0) {
        props.onClose()
        setTime(10 * 60)
      return;
    }
    const timerId = setInterval(() => {
      setTime(prevTime => prevTime - 1);
    }, 1000);
    return () => clearInterval(timerId);
  }, [time, props]) 

  const formatTime = (seconds) => {
    const minutes = Math.floor(seconds / 60)
    const remainingSeconds = seconds % 60
    return `${minutes}:${remainingSeconds < 10 ? '0' : ''}${remainingSeconds}`
  }

  const submitInfo = async () => {
    console.log(formData[props.deleteField], props.deleteField)
    if (props.deleteField){
      await LocalAxios.delete(`${props.urlToModal}${formData[props.deleteField]}/`, formData).then((response)=>{
        setErrorData({})
        setResponseData(response)
        props.onClose() 
        setTime(10 * 60)
        navigate("/historical/"+props.dataTo.plate)
    }).catch((error) =>{
        setResponseData({})
        setErrorData(error.response.data)
        console.log(error)
    }).finally(()=>{
        setLoadingData(false)
    })
    }else{
    await LocalAxios.post(props.urlToModal, formData).then((response)=>{
        setErrorData({})
        setResponseData(response)
        props.onClose() 
        setTime(10 * 60)
        navigate("/historical/"+formData.plate)
    }).catch((error) =>{
        setResponseData({})
        setErrorData(error.response.data)
        console.log(error)
    }).finally(()=>{
        setLoadingData(false)
    })
  }
  }
  return (
    <div className={"modal-overlay "+props.isStyle} onClick={props.onClose}>
      <div className="modal-content" onClick={e => e.stopPropagation()}>
        <h2>Spots Reservation</h2>
        <p>Time Remaining: {formatTime(time)}</p>
        <p>
            Garage: {props.dataTo.name}
            <br/>
            Day: {props.dataTo.day}
            <br/>
            Start Time: {props.dataTo.start_time}
            <br/>
            End Time: {props.dataTo.end_time}
        </p>
        <div className='mb-3'>
            <input className='form-control' value={formData.plate} onChange={handleChange} type="text" name='plate' placeholder="Enter your late's car" required/>
            <small>{errorData.plate && <div className='text-danger'>{errorData.plate}</div>}</small>
        </div>
        <button onClick={submitInfo}>Booking</button>
      </div>
    </div>
  );
};

export default Modal
