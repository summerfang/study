import { useState } from 'react';
// import ReactDOM from "react-dom/client";

const Car2 = () => {
    const [car, setCar] = useState({
        color: 'red',
        model: 'Tesla',
        year: 2021,
        make: 'Model S'
    });

    const updateColor = () => { 
        setCar(previousState => {
            return {
                ...previousState,
                color: 'blue'
            };
        });
    };

    return (
        <>
            <h1>My car is a {car.color} {car.model} which is made in {car.year} {car.make}</h1>
            <button 
                onClick={updateColor}
            >Blue</button>    
        </>
    );

};

export default Car2;