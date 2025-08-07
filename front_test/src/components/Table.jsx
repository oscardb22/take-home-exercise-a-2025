import React, {useState} from 'react'
import _ from "lodash"
import Button from "../components/Button"
import { faTrash, faEdit } from "@fortawesome/free-solid-svg-icons"
import { useNavigate } from 'react-router-dom'
import ImageUrlChecker from './ImageUrlChecker'
import Modal from './Modal'


const Table = (props) => {
    const [isModalOpen, setIsModalOpen] = useState("hide_display")
    const [data, setData] = useState({})
    const openModal = () => setIsModalOpen("")
    const closeModal = () => setIsModalOpen("hide_display")

    console.log("tableDataFor", props.tableDataFor)
    const navigate = useNavigate()
    const columns = Object.keys(props.tableDataFor[0] || {})
    const rowOnclick  = async (param) => {
        navigate(param)
    }
  return (
    <>
    <Modal onClose={closeModal} dataTo={data} isStyle={isModalOpen} urlToModal={props.urlToModal}/>
    <div className='container'>
        <div className='p-5 text-center bg-light-dark rounded table-responsive'>
            <table className="table table-hover table-dark">
                <thead>
                    <tr key="headers">
                        {
                        columns.map((name, index)=>{
                            return (<th scope="col" key={index}>{_.capitalize(name.split("_").join(" "))}</th>)
                        })
                        }
                        {props.hasAction ? <th colSpan="2" scope="row" key={`actionHeader`}>Actions</th> : null}
                    </tr>
                </thead>
                <tbody>
                    {
                    props.tableDataFor.map((tableData, index)=>{
                        return (
                            <tr key={index} >
                                {
                                props.showModal ? 
                                columns.map((data) => {return <th onClick={() => {setData(tableData); openModal();}} scope="row" key={`${data}body${index}`}><ImageUrlChecker urlImage={tableData[data]} /></th>})
                                 :
                                columns.map((data) => {return <th onClick={() => rowOnclick(`/${props.urlTo}/${tableData["uuid"]}`)} scope="row" key={`${data}body${index}`}><ImageUrlChecker urlImage={tableData[data]} /></th>})
                                }
                                {props.showModal ? null :props.hasAction ? <th scope="row" key={`actionBody${index}`}>
                                    {props.canEdit ? <Button classData="btn-outline-success" urlTo={`/${props.urlTo}/${tableData["uuid"]}`} iconData={faEdit}/> : null}
                                    &nbsp;
                                    {props.canDelete ? <Button classData="btn-outline-danger" urlTo="" iconData={faTrash}/> : null}
                                </th> : null}
                            </tr>
                        )
                    })
                    }
                </tbody>
            </table>
        </div>
    </div>
    </>
  )
}

export default Table