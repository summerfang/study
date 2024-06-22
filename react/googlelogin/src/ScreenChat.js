import { Card, Col, Container, Row } from "react-bootstrap";
import "bootstrap/dist/css/bootstrap.min.css";
import { customers } from './customer';

import SMSDialog from "./SMSDialog";

export default function ScreenChat() {
    return (
        <Container className="px-0">
            <Row
                noGutters
                className="pt-2 pt-md-5 w-100 
                        px-4 px-xl-0 position-relative"
            >
                {
                    customers.map((customer) => (
                        <Col
                            xs={{ order: 2 }}
                            md={{ size: 4, order: 1 }}
                            tag="aside"
                            className="pb-5 mb-5 pb-md-0 
                            mb-md-0 mx-auto mx-md-0"
                        >
                            <SMSDialog>{customer}</SMSDialog>
                        </Col>
                    ))
                }
            </Row>

        </Container>
    )
}