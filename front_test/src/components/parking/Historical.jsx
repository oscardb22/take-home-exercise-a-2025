import React, {useEffect, useState} from "react"
import {useParams} from "react-router-dom"
import LocalAxios from "../../api/axios"
import Table from "../Table"

const Historical = () => {
    const [tableData, setTableData] = useState([])
    const {plate} = useParams()

    useEffect(() => {
        const fetchProtectedData = async () => {
            try{
                const response = await LocalAxios.get(`parking/historical/?plate=${plate || "NQZ777"}`)
                setTableData(response.data)
            }catch(error){
                console.error(error)
            }
        }
        fetchProtectedData()
        return () => {}
      }, [plate, ])
  return (
    <>
    <h2>Historical</h2>
      <Table tableDataFor={tableData} hasAction={false} canDelete={false} canEdit={true} />
    </>
  )
}

export default Historical