
import React from 'react';
import { Switch, Route, Link, Routes } from 'react-router-dom';
import './App.css';
import Login from './components/Login.tsx';
import MainPage from '../src/pages/MainPage/MainPage.tsx'
import Handbook_report from './components/report/Handbook_report.tsx'
import  Home, { Handbook_report1 }  from './components/report/Handbook_report1.tsx'
import Menu from './components/Menu.tsx';
import AppRoute from './components/AppRoute/AppRoute.tsx'

function App() {
  return (
    <div className='App'>
      <Menu/>
      <AppRoute/>
      
    </div>

  );
}

export default App;
