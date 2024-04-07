import { useState } from 'react';
import ReactDOM from "react-dom/client";

export default function Car() {
    const [color, setColor] = useState('red');
    const [model, setModel] = useState('Tesla');
    const [year, setYear] = useState(2021);
    const [make, setMake] = useState('Model S');

    return (
    <>
        <h1>My car is {model}!</h1>

        <p>
            It is {color} {make} and was made in {year}.
        </p>
    </>
  );
}