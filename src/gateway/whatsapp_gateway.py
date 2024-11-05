import tornado.ioloop
import tornado.web
from whatsapp_inbound_handler import WhatsappInboundHandler
from whatsapp_outbound_handler import WhatsappOutboundHandler


def make_app():
    return tornado.web.Application([
        (r"/outbound", WhatsappOutboundHandler),
        (r"/inbound", WhatsappInboundHandler),
    ])


if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    print("Server running on http://localhost:8888")
    tornado.ioloop.IOLoop.current().start()
