import tornado.web
import tornado.ioloop


class basicRequestHandler(tornado.web.RequestHandler):
  def get(self):
    self.write("this is python command executed in the backend")

class listEmpRequestHandler(tornado.web.RequestHandler):
  def get(self):
    self.render("index.html")

class queryParamRequestHandler(tornado.web.RequestHandler):
  def get(self):
    num = self.get_argument("num")
    if (num.isdigit()):
      checkNumber = "odd" if int(num) % 2 else "even"
      self.write(f"The {num} is {checkNumber}")
    else:
      self.write(f"{num} This is not a number")

class resourceParamRequestHandler(tornado.web.RequestHandler):
  def get(self, studentName, courseId):
    self.write(F"Welcome {studentName} the course you enroll is {courseId}")


if __name__ == "__main__":
  app = tornado.web.Application([
    (r"/", basicRequestHandler),
    (r"/employee", listEmpRequestHandler),
    (r'/isEven', queryParamRequestHandler),
    (r"/student/([a-zA-Z]+)/([0-9]+)", resourceParamRequestHandler)
  ])


  port = 8882
  app.listen(port)
  print(f"application is ready an litening on port- {port}")
  tornado.ioloop.IOLoop.current().start()