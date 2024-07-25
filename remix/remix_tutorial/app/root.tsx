import type { LinksFunction } from "@remix-run/node";
import { json, redirect } from "@remix-run/node";
import {
  Form,
  Link,
  Links,
  Meta,
  NavLink,
  Outlet,
  Scripts,
  ScrollRestoration,
  useLoaderData,
  useNavigation,
} from "@remix-run/react";

import appStylesHref from "./app.css?url";

export const links: LinksFunction = () => [
  { rel: "stylesheet", href: appStylesHref },

];

// import "./app.css";
import { createEmptyContact, getContacts } from "./data";

export const loader = async () => {
  const contacts = await getContacts();
  console.log("contact.length:" + contacts.length);
  return contacts;
};

export const action = async () => {
  const contact = await createEmptyContact();
  // return contact;
  return redirect(`/contacts/${contact.id}/edit`);
}

export default function App() {
  const contacts = useLoaderData<typeof loader>();
  // const navigation = useNavigation();
  const navigation = useNavigation();

  return (
    <html lang="en">
      <head>
        <meta charSet="utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <Meta />
        <Links />
      </head>
      <body>
        <div id="sidebar">
          <h1>Remix Contacts</h1>
          <div>
            <Form id="search-form" role="search">
              <input
                id="q"
                aria-label="Search contacts"
                placeholder="Search"
                type="search"
                name="q"
              />
              <div id="search-spinner" aria-hidden hidden={true} />
            </Form>
            <Form method="post">
              <button type="submit">New</button>
            </Form>
          </div>
          <nav>
            {
              contacts.length ? (
                <ul>
                  {
                    contacts.map((contact) => (
                      <li key={contact.id}>
                        <NavLink className={
                          ({ isActive, isPending }) =>
                            isActive
                              ? "active"
                              : isPending
                                ? "pending"
                                : ""
                        } to={`contacts/${contact.id}`}>
                          {
                            contact.first || contact.last ? (
                              <>
                                {contact.first} {contact.last}
                              </>
                            ) : (
                              <i>No Name</i>
                            )
                          }
                          {" "}
                          {
                            contact.favorite ? (
                              <span aria-label="Favorite" role="img">⭐️</span>
                            ) : null
                          }
                        </NavLink>
                      </li>
                    ))
                  }
                </ul>
              ) : (
                <p>No contacts found.</p>
              )
            }
          </nav>
        </div>
        <div
          className={navigation.state === "loading" ? "loading" : ""}
          id="details"
        >
          <Outlet />
        </div>

        <ScrollRestoration />
        <Scripts />
      </body>
    </html>
  );
}
