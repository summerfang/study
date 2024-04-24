import * as React from "react";
import * as ReactDOM from "react-dom/client";
import {
  createBrowserRouter,
  RouterProvider,
} from "react-router-dom";
import Root, { loader as rootLoader, action as rootAction} from "./routes/root";
import './index.css'
import ErrorPage from "./error-page";
import Contact, {loader as contactLoader, action as contactAction} from "./routes/contact";
import EditContact, {action as editAction} from "./routes/edit";
import Test from "./routes/test";
import {action as destroyAction} from "./routes/destroy";
import Index from "./routes";
import { loader as testLoader, action as testAction } from "./routes/test";
import {action as deleteAction} from "./routes/testdelete"


const router = createBrowserRouter([
  {
    path: "/",
    element: <Root />,
    errorElement: <ErrorPage />,
    loader: rootLoader,
    action: rootAction,
    children: [
      { index: true, element: <Index /> },
      {
        path: "contacts/:contactId",
        element: <Contact />,
        loader: contactLoader,
        action: contactAction,
      },
      {
        path: "contacts/:contactId/edit",
        element: <EditContact />,
        loader: contactLoader,
        action: editAction,
      },{
        path: "contacts/:contactId/destroy",
        action: destroyAction,
      }, {
        path: "/test",
        element: <Test />,
        loader: testLoader,
        action: testAction,
      }, {
        path: "/test/delete",
        action: deleteAction,
      }
    ]
  },
]);

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <RouterProvider router={router} />
  </React.StrictMode>,
)
