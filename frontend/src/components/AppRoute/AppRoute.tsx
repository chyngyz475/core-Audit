import React from 'react'
import { Route, Routes } from 'react-router-dom'
import Handbook_report from '../report/Handbook_report.tsx'
import Handbook_report1 from '../report/Handbook_report1.tsx'

type Props = {}

const AppRoute = (props: Props) => {
  return (
    <Routes>      
        <Route path='/Handbook_report' element={ <Handbook_report/> }/>
        <Route path='/Handbook_report1' element={ <Handbook_report1/> }/>
        
    </Routes>
  )
}

export default AppRoute