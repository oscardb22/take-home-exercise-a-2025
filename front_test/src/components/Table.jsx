import React from 'react'
import _ from "lodash"
import Button from "../components/Button"
import { faTrash, faEdit } from "@fortawesome/free-solid-svg-icons"
import { useNavigate } from 'react-router-dom'
import ImageUrlChecker from './ImageUrlChecker'


const Table = (props) => {
    console.log("tableDataFor", props.tableDataFor)
    const navigate = useNavigate()
    const columns = Object.keys(props.tableDataFor[0] || {})
    const rowOnclick  = async (param) => {
        navigate(param)
    }
  return (
    <>
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
                                columns.map((data) => {return <th onClick={() => rowOnclick(`/free_spots/${tableData["uuid"]}`)} scope="row" key={`${data}body${index}`}><ImageUrlChecker urlImage={tableData[data]} /></th>})
                                }
                                {props.hasAction ? <th scope="row" key={`actionBody${index}`}>
                                    {props.canEdit ? <Button classData="btn-outline-success" urlTo={`/free_spots/${tableData["uuid"]}`} iconData={faEdit}/> : null}
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