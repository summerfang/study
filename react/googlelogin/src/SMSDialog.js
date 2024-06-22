import { Container, Row, Col, Card, Stack } from "react-bootstrap";
import Button from 'react-bootstrap/Button';
import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap-icons/font/bootstrap-icons.css";

const SentText = ({ children }: { children: React.ReactNode }) => {
    return (
        <div
            style={{
                background: 'ForestGreen',
                height: 'auto',
                color: 'white',
                borderRadius: '25px 25px 0px 25px',
                padding: '10pt',
                marginBottom: '10pt',
                marginLeft: '40pt',
                textAlign: 'left'
            }}
        >
            {children}
        </div>
    );
};

const ReceivedText = ({ children }: { children: React.ReactNode }) => {
    return (
        <div
            style={{
                background: 'lightgrey',
                height: 'auto',
                color: 'black',
                borderRadius: '0px 25px 25px 25px',
                padding: '10px',
                marginBottom: '10px',
                marginRight: '40px',
                textAlign: 'left'
            }}
        >
            {children}
        </div>
    );
};

const headerStyle = {
    backgroundColor: 'WhiteSmoke',
};

export default function SMSDialog({ children }: { children: React.ReactNode }) {
    return (
        <Card className="text-center" style={{ height: '500px' }}>
            <Card.Header style={headerStyle}>
                <Card.Title>
                    <Stack>
                        <h2><i class="bi bi-person-circle"></i></h2>{children.name}
                    </Stack>
                </Card.Title>
            </Card.Header>
            <Card.Body style={{ height: '200px', overflowY: 'auto' }}>
                <SentText>{children.draft}</SentText>
            </Card.Body>
            <Card.Footer className="text-muted">2 days ago</Card.Footer>
        </Card>
    )
}