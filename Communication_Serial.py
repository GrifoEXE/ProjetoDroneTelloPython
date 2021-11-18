from serial import Serial


class classSerial:
    port_serial = Serial('COM3', 115200)

    def Start(self):
        self.Close()
        self.Open()
        self.Process()

    def Open(self):
        self.port_serial.open()

    def Close(self):
        self.port_serial.close()

    def Process(self):
        self.textTemp = ""

        t = self.port_serial.readline()
        temp = t.decode('utf-8')

        for c in temp:
            if c != "\n":
                self.textTemp += str(c)

        if self.textTemp == "Mensagem: Detected":
            print(self.textTemp)
            return True
        else:
            return False

