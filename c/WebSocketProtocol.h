#ifndef __WebSocketProtocol_H__
#define __WebSocketProtocol_H__

#include <string>

using std::string;

class CWebSocketProtocol
{
public:
    enum WS_Status
    {
        WS_STATUS_CONNECT = 0,
        WS_STATUS_UNCONNECT = 1,
    };

    enum WS_FrameType
    {
        WS_EMPTY_FRAME = 0xF0,
        WS_ERROR_FRAME = 0xF1,
        WS_TEXT_FRAME = 0x01,
        WS_BINARY_FRAME = 0x02,
        WS_PING_FRAME = 0x09,
        WS_PONG_FRAME = 0x0A,
        WS_OPENING_FRAME = 0xF3,
        WS_CLOSING_FRAME = 0x08
    };

    static CWebSocketProtocol * getInstance();

    int getResponseHttp(string &request, string &response);
    int wsDecodeFrame(string inFrame, string &outMessage);    //解码帧
    int wsEncodeFrame(string inMessage, string &outFrame, enum WS_FrameType frameType);    //编码帧打包

private:
    CWebSocketProtocol();
    ~CWebSocketProtocol();

    class CGrabo
    {
    public:
        ~CGrabo()
        {
            if (m_inst != 0)
            {
                delete m_inst;
                m_inst = 0;
            }
        }
    };

    static CGrabo m_grabo;
    static    CWebSocketProtocol * m_inst;
};

#endif