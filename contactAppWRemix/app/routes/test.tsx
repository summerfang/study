import { ActionFunctionArgs, redirect } from "@remix-run/node";
import { Form } from "@remix-run/react";

export function action({  }) {
    return redirect('/')
}

// export function loader1() {

// }

export default function Test() {
    return (
        <>
            <h1>Hello World! Test!</h1>

            <Form method="post">
                <label>
                    <span>First</span>
                    <input type="text" name="first" />
                </label>
                <label>
                    <span>Last</span>
                    <input type="text" name="last" />
                </label>
                <button type="submit">Save</button>
            </Form>
        </>
    )
}