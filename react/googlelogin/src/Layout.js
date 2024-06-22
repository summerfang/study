import React from 'react';
// import "bootstrap/dist/css/bootstrap.min.css";

import { Outlet } from 'react-router-dom';
import Header from './header';
// import { Container, Row, Col } from "react-bootstrap";

export default function Layout() {
    return (
        <div>
            <Header />
            <Outlet />
        </div>
    );
}