import model,view,controller,time

while True:
    time.sleep(1/60)
    controller.event()
    model.model()
    view.view()