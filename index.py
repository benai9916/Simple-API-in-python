import tornado.web
import tornado.ioloop
import json


class mainRequestHandler(tornado.web.RequestHandler):
  def get(self):
    self.render("index.html")

class listRequestHandler(tornado.web.RequestHandler):
  def get(self):
    listFile = open("list.txt", 'r')
    fruits = listFile.read().splitlines()
    listFile.close()
    self.write(json.dumps(fruits))

  def post(self):
    addFruits = self.get_argument('addFruit')
    fh = open('list.txt', 'a')
    fh.write(f"{addFruits}\n")
    fh.close()
    self.write(json.dumps({"message" : "Fruit is added"}))


if __name__ == "__main__":
  app = tornado.web.Application([
    (r"/", mainRequestHandler),
    (r"/list", listRequestHandler),
  ])


  port = 8882
  app.listen(port)
  print(f"application is ready an litening on port- {port}")
  tornado.ioloop.IOLoop.current().start()