import { Outlet } from "@remix-run/react"

export default function TestPage() {
    return (
      <>
        <div>This is the app/routes/test1.jsx page!</div>
        <Outlet />
      </>
    )
  }