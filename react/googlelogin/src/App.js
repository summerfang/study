/*App.js*/

import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'

import Layout from "./Layout";
import Home from './Home';
import About from './About';
import Contact from './Contact';
import Campaign from './Campaign';
import CustomerList from './CustomerList';
import ScreenChat from './ScreenChat';

function App() {
  return (
    <Router>
      <Routes>
        <Route path='/' element={<Layout />}>
          <Route index element={<Home />} />
          <Route path='/about' element={<About />} />
          <Route path='/customerlist' element={<CustomerList />} />
          <Route path='/campaign' element={<Campaign />} />
          <Route path='/screenchat' element={<ScreenChat />} />

          <Route path='/contact' element={<Contact />} />
        </Route>
      </Routes>
    </Router>
  );
}
export default App;