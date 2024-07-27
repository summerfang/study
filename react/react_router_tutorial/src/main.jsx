import React from 'react'
import ReactDOM from 'react-dom/client'
import { createBrowserRouter, RouterProvider } from 'react-router-dom'

import Root, { loader as rootLoader, action as rootAction } from './routes/root'
import ErrorPage from './routes/error-page'
import './index.css'
import Contact, { loader as ContactLoader } from './routes/contact'
import EditContact, { action as EditContactAction } from './routes/edit'
import { action as destroyAction } from './routes/destroy'
import Index from './routes/index'
import { action as contactAction } from './routes/contact'
const router = createBrowserRouter([
  {
    path: '/',
    element: <Root />,
    errorElement: <ErrorPage />,
    loader: rootLoader,
    action: rootAction,
    children: [{
      errorElement: <ErrorPage />,
      children: [

        { index: true, element: <Index /> },
        {
          path: 'contacts/:id',
          element: <Contact />,
          loader: ContactLoader,
          action: contactAction,
        },
        {
          path: 'contacts/:id/edit',
          element: <EditContact />,
          loader: ContactLoader,
          action: EditContactAction
        },// Add this line
        {
          path: "contacts/:id/destroy",
          action: destroyAction,
        },

      ],
    }
    ]
  }
])
ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <RouterProvider router={router}>
    </RouterProvider>
  </React.StrictMode>,
)
