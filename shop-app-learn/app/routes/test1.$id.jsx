import { useLoaderData } from "@remix-run/react";
import { json } from "@remix-run/node";

export const loader = async ( {request, params} ) => {
    const id = params.id;
    return json({'id': id});
}

export default function Test() {
    const {id} = useLoaderData();

    return (
        <>
        <h1> This is from test.${id}.jsp</h1>
    </>
    );


}