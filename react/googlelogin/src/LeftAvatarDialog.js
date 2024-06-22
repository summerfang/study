import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import Image from "react-bootstrap/Image";

import { Text, InlineStack, Scrollable, } from '@shopify/polaris';
import { AppProvider, Card, Grid, Page, Box, BlockStack, Button, TextField, Avatar } from '@shopify/polaris';
import { Icon } from '@shopify/polaris';
import {
    SendIcon,
    XIcon, LayoutPopupIcon,
    ChatIcon,
} from '@shopify/polaris-icons';
import './shopchatui.css';
import { useCallback, useState, useEffect, createContext, useContext } from 'react';
// import VisitorDialogHeader from './VisitorDialogHeader';
// import { AgentContext } from './AgentContainer';
// import { UserContext } from '~/routes/visitor';

export const UserContextDialog = createContext('');

export default function LeftAvatarDialog() {

    // const [role, SetRole] = useContext(AgentContext);

    // const conversations = useContext(UserContext);
    const [conversations, setConversation] = useState({});

    const [dialogStatus, setDialogStatus] = useState('0') // 0 - normal; 1 - minimized; 2 - maximized

    const [value, setValue] = useState('');

    const handleChange = (e: string) => { setValue(e) }

    return dialogStatus === '0' ? (
        <UserContextDialog.Provider value={[dialogStatus, setDialogStatus]}>
            <AppProvider i18n={undefined}>
                    {/* <BlockStack> */}
                    <Container width="500">
<Row>                        <VisitorDialogHeader /> </Row>
<Row>
                        <VisitorDialogBody>
                            {/* <Scrollable shadow style={{ height: '400px' }} focusable> */}
                                {conversations.length ? (
                                    <div style={{ background: 'grey', padding: '10pt' }}>
                                        {conversations.map((conversation) => (
                                            <BlockStack key={conversation.id}>
                                                {conversation.role === 'agent' ? (
                                                    <InlineStack wrap={false}>
                                                        <Box>
                                                            <Avatar source={conversation.avater} />
                                                        </Box>
                                                        <Box>
                                                            <AgentText>
                                                                <Text as="p" variant="bodyMd">
                                                                    {conversation.content}
                                                                </Text>
                                                            </AgentText>
                                                        </Box>
                                                        <Box width='30pt'></Box>
                                                    </InlineStack>

                                                ) : (

                                                    <InlineStack wrap={false} align='end'>
                                                        <Box width='30pt'></Box>
                                                        <Box>
                                                            <CustomerText>
                                                                <Text as="p" variant="bodyMd">
                                                                    {conversation.content}
                                                                </Text>
                                                            </CustomerText>
                                                        </Box>
                                                    </InlineStack>
                                                )}

                                            </BlockStack>
                                        ))}
                                    </div>
                                ) : (
                                    <p>
                                        <i>No conversation</i>
                                    </p>
                                )}

                            {/* </Scrollable> */}
                        </VisitorDialogBody>
                        </Row>
                        <Row>
                        <VisitorDialogFooter>
                            <div style={{ width: '100%' }}>
                                <TextField
                                    label=""
                                    autoComplete='off'
                                    multiline={1}
                                    value={value}
                                    onChange={handleChange}
                                    placeholder='Type your message...'
                                    variant='borderless'
                                    autoFocus
                                // autoSize
                                />
                            </div>
                            <div>
                                <Button variant="plain" icon={SendIcon} />
                            </div>
                        </VisitorDialogFooter>
                        </Row>
                        </Container>

                    {/* </BlockStack> */}
            </AppProvider >
        </UserContextDialog.Provider>
    ) : (dialogStatus === '1' ? (
        <UserContextDialog.Provider value={[dialogStatus, setDialogStatus]}>
            <AppProvider i18n={undefined}>
                <div style={{ flexDirection: 'column', alignSelf: 'flex-start' }}>
                    <Button icon={ChatIcon} variant='plain' onClick={() => (setDialogStatus('0'))}>
                    </Button>
                </div>

            </AppProvider>
        </UserContextDialog.Provider>
    ) : (
        <h1>{dialogStatus}</h1>
    ))
};



const AgentText = ({ children }: { children: React.ReactNode }) => {
    return (
        <div
            style={{
                background: 'DodgerBlue',
                height: 'auto',
                color: 'white',
                borderRadius: '0px 25px 25px 22px',
                padding: '10pt',
                marginBottom: '10pt',
                marginLeft: '10pt'

            }}
        >
            {children}
        </div>
    );
};

const CustomerText = ({ children }: { children: React.ReactNode }) => {
    return (
        <div
            style={{
                background: 'black',
                height: 'auto',
                color: 'white',
                borderRadius: '0px 25px 0px 25px',
                padding: '10pt',
                marginBottom: '10pt',

            }}
        >
            {children}
        </div>
    );
};


const VisitorDialogHeader = () => {
    // const status = useContext(UserContext)
    // const [dialogStatus, setDialogStatus] = useContext(UserContext);

    const [dialogStatus, setDialogStatus] = useContext(UserContextDialog);

    return (
        <div style={{ display: 'flex', alignItems: 'flex-start', justifyContent: 'space-between', background: 'white' }}>
            <div style={{ display: 'flex', alignItems: 'center' }}>
                {/* <Image src="https://cdn.vectorstock.com/i/1000x1000/32/23/user-sign-icon-person-symbol-human-avatar-vector-12693223.webp" roundedCircle width={50}/>  */}
                <i class="bi bi-person-circle"></i>
                <div style={{ marginLeft: 10 }}>
                    <Text variant='bodyMd' as={'p'}>
                        <b>Christopher Campell</b>
                    </Text>
                    <Text variant='bodyMd' as={'p'}>
                        Last seen 02:55 PM
                    </Text>
                </div>
            </div>
        </div>
    );
};

const VisitorDialogBody = ({ children }: { children: React.ReactNode }) => {
    return (
        <div
            style={{
                background: 'grey',
                height: 'auto',
            }}
        >
            {children}
        </div>
    );
};

const VisitorDialogFooter = ({ children }: { children: React.ReactNode }) => {
    return (
        <div
            style={{
                background: 'white',
                height: 'auto',
                padding: '10px 10px 0px 0px',
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'space-between'
            }}
        >
            {children}
        </div>
    );
};

const Placeholder = ({
    children,
    label = '',
    height = 'auto',
    width = 'auto',
    align = 'begin'

}: {
    children: React.ReactNode;
    label: string;
    height: string;
    width: string;
    align: string;

}) => {
    return (
        <div
            style={{
                // padding: '0px 10px ',
                // background: 'var(--p-color-text-info)',
                height: height,
                width: width,
            }}
        >
            <InlineStack align={align}>
                <div
                    style={{
                        color: 'var(--p-color-text-info-on-bg-fill)',
                    }}
                >
                    <Text
                        as="h2"
                        variant="bodyMd"
                        fontWeight='semibold'
                    // tone="text-inverse"
                    >
                        {label}
                    </Text>
                    {children}
                </div>
            </InlineStack>
        </div>
    );
};