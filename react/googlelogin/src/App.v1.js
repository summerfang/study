/*App.js*/

import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'

// import { googleLogout, useGoogleLogin } from '@react-oauth/google';
// import axios from 'axios';
import Layout from "./Layout";
import Home from './Home';
import About from './About';
import Contact from './Contact';

function App() {
  // const [user, setUser] = useState([]);
  // const [profile, setProfile] = useState([]);

  // const login = useGoogleLogin({
  //   onSuccess: (codeResponse) => setUser(codeResponse),
  //   onError: (error) => console.log('Login Failed:', error)
  // });

  // useEffect(
  //   () => {
  //     if (user) {
  //       axios
  //         .get(`https://www.googleapis.com/oauth2/v1/userinfo?access_token=${user.access_token}`, {
  //           headers: {
  //             Authorization: `Bearer ${user.access_token}`,
  //             Accept: 'application/json'
  //           }
  //         })
  //         .then((res) => {
  //           setProfile(res.data);
  //         })
  //         .catch((err) => console.log(err));
  //     }
  //   },
  //   [user]
  // );

  // // log out function to log the user out of google and set the profile array to null
  // const logOut = () => {
  //   googleLogout();
  //   setProfile(null);
  // };

  // return (
  //     <div>
  //         <h2>React Google Login</h2>
  //         {profile ? (
  //             <div>
  //                 <img src={profile.picture} alt="user image" />
  //                 <h3>User Logged in</h3>
  //                 <p>Name: {profile.name}</p>
  //                 <p>Email Address: {profile.email}</p>

  //                 <button onClick={logOut}>Log out</button>
  //             </div>
  //         ) : (
  //             <button onClick={login}>Sign in with Google 🚀 </button>
  //         )}
  //     </div>
  // );

  return (
    <Router>
      <Routes>
        <Route path='/' element={<Layout />}>
        <Route index element={<Home />} />
        <Route path='/about' element={<About />} />
        <Route path='/contact' element={<Contact />} />
        </Route>
      </Routes>
    </Router>
  );
}
export default App;