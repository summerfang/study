/*Header.js*/

import React, { useState, useEffect } from 'react';
import { googleLogout, useGoogleLogin } from '@react-oauth/google';
import axios from 'axios';

import Container from 'react-bootstrap/Container';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
import NavDropdown from 'react-bootstrap/NavDropdown';
import Image from 'react-bootstrap/Image';

function Header() {
  const [user, setUser] = useState([]);
  const [profile, setProfile] = useState(null);

  const login = useGoogleLogin({
    onSuccess: (codeResponse) => setUser(codeResponse),
    onError: (error) => console.log('Login Failed:', error)
  });

  useEffect(
    () => {
      if (user) {
        axios
          .get(`https://www.googleapis.com/oauth2/v1/userinfo?access_token=${user.access_token}`, {
            headers: {
              Authorization: `Bearer ${user.access_token}`,
              Accept: 'application/json'
            }
          })
          .then((res) => {
            setProfile(res.data);
          })
          .catch((err) => console.log(err));
      }
    },
    [user]
  );

  // log out function to log the user out of google and set the profile array to null
  const logOut = () => {
    googleLogout();
    setProfile(null);
  };

  return (
    <Navbar expand="lg" className="bg-body-tertiary">
      <Container>

        <Navbar.Brand href="#home"><Image src='trueup.jpg' width={100} /></Navbar.Brand>
        <Navbar.Toggle aria-controls="basic-navbar-nav" />
        <Navbar.Collapse id="basic-navbar-nav">
          <Nav className="me-auto">
            <Nav.Link href="/">Home</Nav.Link>
            <Nav.Link href="/campaign">New Campaign</Nav.Link>
            <NavDropdown title="Campaign" id="basic-nav-dropdown">
              <NavDropdown.Item href="/compaign">Start a new campaign</NavDropdown.Item>
              <NavDropdown.Item href="/about">
                Manage campaign
              </NavDropdown.Item>

              <NavDropdown.Divider />
              <NavDropdown.Item href="#action/3.4">
                Recent campaign
              </NavDropdown.Item>
            </NavDropdown>

          </Nav>
        </Navbar.Collapse>
        <Navbar.Collapse>
        </Navbar.Collapse>
        <Navbar.Brand href="#home">
          {profile ? (<span>
            {/* <Image src={profile.picture} alt="user image" width={50} roundedCircle />{profile.name} */}
            <NavDropdown title={profile.name}>
                  <NavDropdown.Item onClick={logOut}>Log out</NavDropdown.Item>
                </NavDropdown>
          </span>
          ) : (
            <button onClick={login}>Sign in with Google 🚀 </button>
          )}
        </Navbar.Brand>
      </Container>
    </Navbar>
  );
}
export default Header;