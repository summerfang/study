import React, { Fragment } from "react";
// import { useNavigate } from "react";
 
import {
    Button,
    Alert,
    Card,
    CardImg,
    CardBody,
    CardTitle,
    CardSubtitle,
    CardText,
} from "react-bootstrap";
 
const BANNER = "https://i.imgur.com/CaKdFMq.jpg";
 
const LeftCard = () => {

    // const navigate = useNavigate();

    const handleButtonClick = () => {
        // navigate("/campaign/prompt")
    }
    
    return (<Fragment>
        <Alert color="danger" className="d-none d-lg-block">
            <strong>Account not activated.</strong>
        </Alert>
 
        <Card>
            <CardImg
                top
                width="100%"
                src={BANNER}
                alt="banner"
            />
            <CardBody>
                <CardTitle
                    className="h3 mb-2 pt-2 
                    font-weight-bold text-secondary"
                >
                    How to start a Campaign
                </CardTitle>
                <CardSubtitle
                    className="text-secondary mb-3 
                        font-weight-light text-uppercase"
                    style={{ fontSize: "0.8rem" }}
                >
                    The easiest way to boost your sales
                </CardSubtitle>
                <CardText
                    className="text-secondary mb-4"
                    style={{ fontSize: "0.75rem" }}
                >
                    Ture up is a best AI native tool to help your business
                </CardText>
                <Button
                    color="success"
                    className="font-weight-bold"
                    onClick={handleButtonClick}
                >
                    Start a new Campaign
                </Button>
            </CardBody>
        </Card>
    </Fragment>
    )
};
 
export default LeftCard;