// import localforage from "localforage"
import { redirect, useLoaderData } from "react-router-dom"
import { Link, Form } from "react-router-dom";

let testData = []

export async function loader() {
    return { testData }
}

export async function action({request, params}) {

    const formData = await request.formData();
    const newTest = Object.fromEntries(formData);
    testData.unshift(newTest);

    return redirect(`/test`)
}

export default function Test() {
    const { testData } = useLoaderData();

    return (
        <>
            <h1>Hellow, Test</h1>
            <ul>
                {
                    testData.map((test) => (
                        <li key={test.first+test.last}>
                        <Link to={`test/${test.first}`}>
                            <>
                                {test.first}{test.last}
                            </>
                        </Link>
                        </li>
                    ))
                }
            </ul>
            <Form method="post">
                <label><span>First</span><input name="first"/></label>
                <label><span>Last</span><input name="last"/></label>
                <button type="submit">save</button>
            </Form>
            <Form method="post" action="delete">
            <p><button>Delete</button></p>

            </Form>
        </>
    )
}