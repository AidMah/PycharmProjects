from abc import ABC, abstractmethod


class UIControl(ABC):
    @abstractmethod  # Just to make all the other classes to have draw method
    def draw(self):
        pass


class TextBox(UIControl):
    def draw(self):
        print("TextBox")


class DropDownList(UIControl):
    def draw(self):
        print("DropDownList")


"""
def draw(control):  # If you pass a parameter here it will make it local object
    control.draw()  # then here the draw method inside the control will be called here.
"""


def draw(controls):
    """
    an example of polymorphism (Many Forms) which takes different forms inside and calls its draw
    methods, in order to achieve polymorphic behavior, you start by defining the case class. And in this class,
    we define the common behavior, or the common method that we need in this derivative, with this we achieve,
    polymorphic behavior in our draw function on line 22.
    in another way, if pass to draw methods any object which has draw method the python happy but having a UI class with
    an @abstractmethod draw is a good practice as it enforces all driven classes to have its own draw method.
    """
    for control in controls:
        control.draw()  # then here the draw method inside the control will be called here.


ddl = DropDownList()
print(isinstance(ddl, UIControl))
draw([ddl,ddl])  # pass ddl object which is instance of DropDownList and again instance of UIControl

textbox = TextBox()
#draw(textbox)
draw([textbox,ddl])
draw([textbox, textbox])
