

import React from 'react';
import ReactDOM from 'react-dom';

import Button from '@mui/material/Button';

import App from './App.tsx';

export function ButtonUsage() {
  return <Button variant="contained">Hello world</Button>;
}

export function AnotherButton() {
  return <Button variant="outlined">Hello world</Button>;

}
// import './index.css'; // Optional: Import your global CSS styles
// import App from './App'; // Import your main application component
// import * as serviceWorker from './serviceWorker'; // Optional: Service worker for progressive web apps

ReactDOM.render(
  <React.StrictMode>
    {/* <ButtonUsage></ButtonUsage>
    <AnotherButton></AnotherButton> */}
    <App />
  </React.StrictMode>,
  document.getElementById('root')
);