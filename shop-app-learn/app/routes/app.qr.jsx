import { Page, Card, Link, Form, Button, IndexTable } from "@shopify/polaris"
import { json } from "@remix-run/node"
import { useLoaderData, useNavigate } from "@remix-run/react"
import { authenticate } from "../shopify.server";
import { getQRCodes } from "../models/QRCode.server";


export async function loader({ request, params }) {
    const { admin, session } = await authenticate.admin(request);

    const QRs = await getQRCodes(session.shop, admin.graphql)
    return json({ QRs });
}

export default function Qr() {
    const { QRs } = useLoaderData();
    const navigate = useNavigate();
    return (
        <Page>
            <ui-title-bar title="Test">
                <button variant="primary" onClick={() => navigate("/test1")}>
                   /test
                </button>
                <button onClick={() => navigate("/test1/")}>/test/</button>
                <button onClick={() => navigate("/test1/abc")}>/test/abc</button>

            </ui-title-bar>

            {/* <Card>
                <ur>
                    {
                        QRs.length === 0 ? (
                            <li>
                                <h1>Hello, the length of QRs is {QRs.length}</h1>
                            </li>
                        ) : (
                            QRs.map(
                                (qr) => (
                                    <li key={qr.id}><Link to={qr.title}>{qr.title}</Link></li>
                                )
                            )
                        )
                    }

                </ur>
            </Card>
            <Card>
                <button variant="primary" onClick={() => navigate("/test")}>Go test</button>
            </Card> */}
        </Page>
    )
}