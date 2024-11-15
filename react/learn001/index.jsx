import { createBrowserRouter, RouteObject } from 'react-router-dom';
import { Link } from 'react-router-dom';
import React from 'react';

const router = createBrowserRouter([
    {
        path: '/',
        element: (
            <div>
                <h1>Home</h1>
                <Link to="/about">About</Link>
            </div>
        ),
    },
]);

export default router;
