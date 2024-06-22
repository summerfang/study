import FloatChatDialog from "../floatchatdialog";
import VisitorDialog from "../ui/LeftAvatarDialog";
import CardDefault from "../ui/CardDefault"
import BoxWithColorExample from "../ui/BoxWithColorExample"
import CardWithSubduedBackground from "../ui/CardWithSubduedBackground"
import { AppProvider, Card, Layout, Page } from "@shopify/polaris";
// import en from "@shopify/polaris/locales/en.json";
import "@shopify/polaris/build/esm/styles.css";
import Draggable from "react-draggable";
import UnifiedAvatarsDialog from "~/ui/UnifiedAvatarsDialog";
import LeftAvatarDialog from "../ui/LeftAvatarDialog";
import BilateralAvatarDialog from "~/ui/BilateralAvatarDialog";
import { getConversations } from "~/ui/conversations";
import { json } from "@remix-run/node";
import { useLoaderData } from "@remix-run/react";
import { createContext } from "react";

export const UserContext = createContext('');


export const loader = async () => {
    const conversations = await getConversations();
    return json({ conversations });
};

export default function Visitor() {

    const {conversations} = useLoaderData<typeof loader>();

    return (
        // <Draggable>
        //     <div className='askDialogDiv'>
        //         <VisitorDialog />
        //     </div>
        // </Draggable>
        <UserContext.Provider value={conversations}>
        <Page fullWidth>
            <Layout>
                <Layout.Section variant="oneThird">
                    <UnifiedAvatarsDialog />
                </Layout.Section>
                <Layout.Section variant="oneThird">
                    <LeftAvatarDialog />
                </Layout.Section>
                <Layout.Section variant="oneThird">
                    <BilateralAvatarDialog />
                </Layout.Section>
            </Layout>

        </Page>
        </UserContext.Provider>
    )
}