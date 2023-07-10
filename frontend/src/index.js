import React from 'react';
import ReactDOM from 'react-dom/client';
import { createRoot } from 'react-dom/client';
import './index.css';
import { BrowserRouter } from 'react-router-dom';
import App from './App';

import reportWebVitals from './reportWebVitals';

const root = createRoot(document.getElementById('root' ) );

root.render(
    <BrowserRouter>
        <App/>
    </BrowserRouter>
    
)
// Если вы хотите начать измерение производительности в своем приложении, передайте функцию
// для регистрации результатов (например: reportWebVitals(console.log))
// или отправить на конечную точку аналитики. Узнайте больше: https://bit.ly/CRA-vitals
reportWebVitals();
