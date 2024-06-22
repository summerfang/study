// import { Container } from "react-bootstrap";

// export default function CustomerList() {
//     return (
//         <main className="my-5 py-5">
//             <Container className="px-0">
//                 <h1>Custom</h1>
//             </Container>
//         </main>
//     )
// }

// import { Container } from "react-bootstrap"

// export default function CustomerList() {
//     return (
//         <main className="my-5 py-5">
//             <Container className="px-0">
//                 <h1>Launch a </h1>

//                     <textarea class="form-control" rows="5" id="comment" name="text" placeholder="I want to ... "></textarea>
//                     <button>Next</button>
//             </Container>
//         </main>
//             )
// }

import React, { useState } from 'react';
import { Container } from 'react-bootstrap';
// import { useNavigate } from '@remix-run/react';
import { useNavigate } from 'react-router-dom';
import { customers } from './customer';

export default function CustomerList() {
    const navgiate = useNavigate();

    const [selectedCustomers, setSelectedCustomers] = useState([]);
    const [filter, setFilter] = useState('');

    const filteredCustomers = customers.filter((customer) =>
        customer.name.toLowerCase().includes(filter.toLowerCase())
    );

    const handleCheckboxChange = (customerId) => {
        setSelectedCustomers((prevSelected) =>
            prevSelected.includes(customerId)
                ? prevSelected.filter((id) => id !== customerId)
                : [...prevSelected, customerId]
        );
    };

    function handleButtonClick(event: MouseEvent<HTMLButtonElement, MouseEvent>): void {
        navgiate('/screenchat')
    }

    return (
        <main className="my-5 py-5">
            <Container className="px-0">

                <div>
                    <input
                        type="text"
                        placeholder="Filter by name..."
                        value={filter}
                        onChange={(e) => setFilter(e.target.value)}
                    />
                    <table class="table">
                        <thead>
                            <tr>
                                <th>Select</th>
                                <th>Name</th>
                                <th>Phone</th>
                                <th>Email</th>
                                <th>Last Visit</th>
                                <th>Service Appointed</th>
                                <th>Message preview</th>
                            </tr>
                        </thead>
                        <tbody>
                            {filteredCustomers.map((customer) => (
                                <tr key={customer.id}>
                                    <td>
                                        <input
                                            type="checkbox"
                                            checked={selectedCustomers.includes(customer.id)}
                                            onChange={() => handleCheckboxChange(customer.id)}
                                        />
                                    </td>
                                    <td>{customer.name}</td>
                                    <td>{customer.phone}1234567890</td>
                                    <td>{customer.email}abc@efg.com</td>
                                    <td>{customer.lastVisit}</td>
                                    <td>{customer.serviceAppointed}</td>
                                    <td>{customer.draft}</td>

                                </tr>
                            ))}
                        </tbody>
                    </table>
                </div>
                <div>
                    <button onClick={handleButtonClick}>Next</button>
                </div>
            </Container>
        </main>
    );
}

// export default CustomerList;
