import React, {useContext} from 'react'
import Button from './Button'
import { AuthContext } from "../AuthProvider"

function Main() {
  const {isLoggedIn, setIsLoggedIn} = useContext(AuthContext)
  return (
    <>
    <div className='container'>
        <div className='p-5 text-center bg-light-dark rounded'>
            <h1 className='text-light'>Vite + React + Django</h1>
            <p className='text-light lead'>
                Why use Airflow for ETL with Python?

Workflow as Code (Python): Airflow allows you to define your entire ETL workflow (DAGs - Directed Acyclic Graphs) in Python code. This brings all the benefits of software engineering practices: version control, testing, modularity, and reusability.
Orchestration: Airflow manages the dependencies between your ETL tasks, ensuring they run in the correct order. If a task fails, Airflow can retry it, notify you, and provide detailed logs.
Scheduling: You can define flexible schedules for your ETL pipelines (e.g., daily, hourly, event-driven), automating their execution.
Scalability: Airflow is designed to scale, allowing you to run a large number of tasks concurrently across a distributed architecture.
Extensibility: Airflow has a rich ecosystem of "providers" (plugins) that offer integrations with various data sources, destinations, and processing tools (databases, cloud storage, APIs, etc.). You can also write custom operators and hooks in Python to fit your specific needs.
Monitoring and UI: The Airflow web UI provides a visual interface to monitor the status of your DAGs and tasks, view logs, and troubleshoot issues.
            </p>
            {isLoggedIn ? (
              <></>
          ): (
            <Button text="Login" classData="btn-outline-info" urlTo="/login"/>
          )}
        </div>
    </div>
    </>
  )
}

export default Main