import { Outlet, useLoaderData } from "@remix-run/react";
import { json } from "@remix-run/node";

export const loader = async ( {request, params} ) => {
    const cityName = params.city;
    return json({'cityName': cityName});
}

export default function ConcertCity() {
    const {cityName} = useLoaderData();

    return (
        <>
        <h1>This is app/routes/concerts.$city.jsx: $city = {cityName}, the url is /concerts/{cityName}</h1>
        <Outlet />
        </>
    );
}