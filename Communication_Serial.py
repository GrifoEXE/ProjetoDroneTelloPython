from serial import Serial

class Class_Serial:
    var_serial = Serial('COM3', 115200)
    tempText = ""

    def Start(self):
        self.Close()
        self.Open()
        self.Process()

    def Open(self):
        self.var_serial.open()

    def Close(self):
        self.var_serial.close()

    def Process(self):

        global tempText
        while True:
            text = self.var_serial.readline()

            for c in text:
                if c == "\n":
                    self.text_received(tempText)
                    tempText = ""
                else:
                    tempText += c

    @staticmethod
    def text_received(text):
        array_text = text.split(' ')

        if array_text[1] == "Detected":
            print(array_text[1])