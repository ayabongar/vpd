from tornado.httpclient import AsyncHTTPClient, HTTPRequest, HTTPError
import json
import tornado.web


class WhatsappInboundHandler(tornado.web.RequestHandler):
    async def post(self):
        print("received whatsapp message")
        whatsapp_message = json.loads(self.request.body)
        whatsapp_result = whatsapp_message["results"][0]
        data = {
            "session_id": whatsapp_result["from"],
            "text": whatsapp_result["message"]["text"],
            "metadata": {}
        }

        asyncHttp = AsyncHTTPClient()
        try:
            asyncHttp.fetch(
                HTTPRequest(
                    "http://localhost:5002/webhooks/vumatelwhatsapp/webhook",
                    method="POST",
                    body=json.dumps(data),
                ),
                raise_error=False
            )
        except HTTPError as http_err:
            print("HTTPError", http_err)
        except Exception as err:
            print("General Exception", err)

        print("Message forwarded to bot.")

        self.set_status(200)
        self.finish()
