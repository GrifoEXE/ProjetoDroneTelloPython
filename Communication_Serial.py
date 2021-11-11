from serial import Serial


class classSerial:
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
        self.var_serial.inWaiting()
        text = self.var_serial.readline()
        for c in text:
            if c == "\n":
                self.tempText = ""
            else:
                self.tempText += str(c)

        array_text = self.tempText.split(" ")
        print(array_text[1])
       # return True

