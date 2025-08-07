import React, {useEffect, useState} from "react"
import {useSearchParams} from "react-router-dom"
import LocalAxios from "../../api/axios"
import Table from "../Table"

const Dashboard = () => {
    const [tableData, setTableData] = useState([])
    const [searchParams, setSearchParams] = useSearchParams()
    const query = searchParams.get("query")
    const category = searchParams.get("category")
    const sort = searchParams.get("sort")

    const handleSortChange = () => {
        setSearchParams({ query, category, sort: sort === "asc" ? "desc" : "asc" })
    }

    useEffect(() => {
        const fetchProtectedData = async () => {
            try{
                const response = await LocalAxios.get(`parking/garage/`)
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
    <h2>Garages</h2>
      <Table tableDataFor={tableData} hasAction={true} canDelete={false} canEdit={true} />
    </>
  )
}

export default Dashboard