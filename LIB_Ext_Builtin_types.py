class Text(str):
    # Object which is in this case an instance of a string class.
    def pr(self):
        print(self)

    def duplicate(self):
        return self + self

    def append(self, object):
        print("Append called")


super().append(object)
list = TrackableList()


text = Text("Python")
print(text.pr())
print(text.duplicate())
print(text.lower())
