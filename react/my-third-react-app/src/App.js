// import logo from './logo.svg';
// import './App.css';
// import { BrowserRouter, Routes, Route } from 'react-router-dom';
// import Layout from './pages/Layout';
// import Home from './pages/Home';
// import Blogs from './pages/Blogs';
// import Contact from './pages/Contact';
// import NoPage from './pages/NoPage';
// import FavoriteColor from './pages/FavoriteColor';
// import Car from './pages/Car';
import Garage  from './pages/Garage'; 

function App() {
  return (
    <Garage />
    // <BrowserRouter>
    //   <Routes>
    //     <Route path="/" element={<Layout />} >
    //       <Route index element={<Home />} />
    //       <Route path="blogs" element={<Blogs />} />
    //       <Route path="contact" element={<Contact />} />
    //       <Route path="Favorate Color" element={<FavoriteColor />} />
    //       <Route path="Car" element={<Car />} />
    //       <Route path="*" element={<NoPage />} />
    //       <Garage />
    //     </Route>
    //   </Routes>
    // </BrowserRouter >
  );
}

export default App;
