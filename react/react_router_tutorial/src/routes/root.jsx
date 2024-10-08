import { Form, json, Link, NavLink, Outlet, redirect, useLoaderData, useSubmit } from "react-router-dom";
import { createContact, getContacts } from "../contacts";
import { useEffect } from "react";

export async function loader( {request}) {
  const url = new URL(request.url);
  const q = url.searchParams.get("q");
  const contacts = await getContacts(q);
  console.info(`root.jsx::loader contacts: \n${JSON.stringify(contacts)}\n q: ${q}`);
  return { contacts, q };
}

export async function action() {
  const contact = await createContact();
  // return { contact };
  return redirect(`/contacts/${contact.id}/edit`);
}

export default function Root() {
  const { contacts, q } = useLoaderData();

  const submit = useSubmit();

  useEffect(() => {
    document.getElementById("q").value = q;

  },[q]);

    return (
      <>
        <div id="sidebar">
          <h1>React Router Contacts</h1>
          <div>
            <Form id="search-form" role="search">
              <input
                id="q"
                aria-label="Search contacts"
                placeholder="Search"
                type="search"
                name="q"
                defaultValue={q}
                onChange={(e)=> {
                  submit(e.currentTarget.form);
                }}
              />
              <div
                id="search-spinner"
                aria-hidden
                hidden={true}
              />
              <div
                className="sr-only"
                aria-live="polite"
              ></div>
            </Form>
            <Form method="post">
              <button type="submit">New</button>
            </Form>
          </div>
          <nav>
            {contacts.length > 0 ? (
              <ul>
                {contacts.map((contact) => (
                  <li key={contact.id}>
                    <NavLink to={`/contacts/${contact.id}`} className={
                      ({isActive, isPending}) => 
                        isActive ? "active" : isPending ? "pending" : ""
                    }>
                    {contact.first || contact.last ? (
                      `${contact.first} ${contact.last}`
                    ) : (
                      <i>No Name</i>
                    )}{" "}
                    {contact.favorite && <span>⭐️</span>}
                    </NavLink>
                  </li>
                ))}
              </ul>
            ) : (<p>No contacts found</p>)}
            {/* <ul>
              <li>
                <Link to="/contacts/1">Your Name</Link>
              </li>
              <li>
                <Link to="/contacts/2">Your Friend</Link>
              </li>
            </ul> */}
          </nav>
        </div>
        <div id="detail">
            <Outlet />
        </div>
      </>
    );
  }