import { useLoaderData } from "@remix-run/react";
import { json } from "@remix-run/node"


export const loader = async ( {request, params}) => {
    const city = params.city;
    const date = params.date;

    return json( { 'city' : city, 'date': date})
}

export default function ConcertsInCityOnDate() {
    const {city, date} = useLoaderData()

    return (
        <>
        <h1>THis is app/routes/concert.$city.$date.jsx. </h1>
        <p>concerts/{city}/{date}</p>
        </>
    );
}