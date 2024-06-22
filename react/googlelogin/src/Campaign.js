import React, { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';

import { Container, Row, Col, Form, Button } from "react-bootstrap";
import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap-icons/font/bootstrap-icons.css";

import axios from 'axios';

import SMSDialog from './SMSDialog';

export default function Campaign() {
    const initJson = {
        "id": "",
        "name": "alessandra olivares",
        "phone": "",
        "email": "",
        "lastVisit": "2024-01-21T14:30:00.000Z",
        "serviceAppointed": "G-signature facial (valid with new client)",
        "draft": "Hi Alessandra,\n\nIt's been a while since your last G-signature facial with us on 2024-01-21. We miss you and would love to see you again soon!\n\nBook your next appointment today and receive 10% off.\n\n[business name]"
    }

    const [initMsg, setInitMsg] = useState(initJson)
    useEffect(() => { },
        [])

    const navigate = useNavigate();

    const handleNextButtonClick = () => {
        navigate("/customerlist")
    }

    const fetchData = async () => {
        try {
            const response = await fetch('https://jsonplaceholder.typicode.com/todos/1');
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            const jsonData = await response.json();

            setInitMsg(previousInitMsg => {return {...previousInitMsg, draft: jsonData.title}});
        } catch (error) {
            console.error('Error fetching data:', error);
        }
    };

    const handleRefreshButtonClick = () => {
        fetchData();
    }

    return (
        <Container className="px-0">
            <Row>
                <Col className='col-sm-6'>
                    <h1>Launch a business compaign</h1>
                    <Form>
                        <Form.Group className="mb-3" controlId="ci1">
                            <Form.Label>Campaign Name:</Form.Label>
                            <Form.Control placeholder='Name of campaign' />
                        </Form.Group>

                        <Form.Group className="mb-3" controlId="ci2">
                            <Form.Label>Campaign Name:</Form.Label>
                            <Form.Control as="textarea" rows={14} placeholder='I want to ...' />
                        </Form.Group>

                    </Form></Col>
                <Col className='col-sm-6'>
                    <Button variant="danger" onClick={handleRefreshButtonClick} >Refresh</Button>
                    <SMSDialog>{initMsg}</SMSDialog>
                </Col>
            </Row>
            <Row>
                <Button variant="primary" onClick={handleNextButtonClick} >Next</Button>
            </Row>
        </Container>
    )
}