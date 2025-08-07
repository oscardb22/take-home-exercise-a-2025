import React, {useEffect, useState} from "react"
import {useParams} from "react-router-dom"
import LocalAxios from "../../api/axios"
import Table from "../Table"

const ParkingFreeSpots = () => {
    const [tableData, setTableData] = useState([])
    const {garage_id} = useParams()

    useEffect(() => {
        const fetchProtectedData = async () => {
            try{
                const response = await LocalAxios.get(`parking/free_spots/?garage_id=${garage_id}`)
                setTableData(response.data.results)
            }catch(error){
                console.error(error)
            }
        }
        fetchProtectedData()
        return () => {}
      }, [])
  return (
    <>
    <h2>Free Spots</h2>
      <Table tableDataFor={tableData} hasAction={true} canDelete={false} canEdit={true} />
    </>
  )
}

export default ParkingFreeSpots