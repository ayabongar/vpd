import tornado.web
import json
from tornado.httpclient import AsyncHTTPClient, HTTPRequest

payload = {
    "from": "447860099299",
    "to": "27692440233",
    "messageId": "a28dd97c-1ffb-4fcf-99f1-0b557ed381da",
    "content": {
        "body": {
            "text": "Some plain text goes here"
        },
        "action": {
            "title": "Main menu options",
            "sections": [
                {
                    "rows": [
                        {
                            "id": "1",
                            "title": "🌍 row title 🍯",
                            "description": "Example of a description"
                        }
                    ]
                }
            ]
        }
    }
}

base_url = "https://n81lz5.api.infobip.com"
api_key = "0ea5af038bdcb18825ec5d64ae3bb44c-b04237e8-b5d7-4359-828a-ef7f14ed8654"


class WhatsappOutboundHandler(tornado.web.RequestHandler):
    async def post(self):
        print("starting outbound process...")
        bot_response = json.loads(self.request.body)
        print(f"response from rasa: {bot_response}")

        asyncHttp = AsyncHTTPClient()
        asyncHttp.fetch(
            HTTPRequest(
                base_url + "/whatsapp/1/message/interactive/list",
                headers={"Authorization": f"App {api_key}", "Content-Type": "application/json"},
                method="POST",
                body=json.dumps(payload),
            ),
            raise_error=False
        )
        print("outbound process complete")

        self.set_status(200)
        self.finish()
