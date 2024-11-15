import path from 'path';
import * as React from 'react';
import { createRoot } from 'react-dom/client';
import {
    createBrowserRouter,
    RouterProvider,
    Route,
    Link,
} from 'react-router-dom';

const router = createBrowserRouter([
    {
        path: '/',
        element: (
            <div>
                <h1>Home</h1>
                <Link to="/about">About</Link>
            </div>
        ),
    }
]);