import subprocess
import sys

class ClassLibraries:
    def __init__(self):
        pass

    def Pip(self):
        try:
            # Install or Upgrade Pip
            subprocess.run([sys.executable, '-m', 'pip', '--version'], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        except subprocess.CalledProcessError:
            subprocess.run([sys.executable, '-m', 'ensurepip', '--default-pip'], check=True)
    
    def List(self):
        StandardLibraries = ['atexit', 'calendar', 'csv', 'datetime', 'locale', 'math', 'os', 'smtplib', 'ssl', 'sys', 'threading', 'time']
        ExternalLibraries = ['clipboard', 'opencv-python', 'email_validator', 'folium', 'keyboard', 'numpy', 'pafy', 'pyautogui', 'pygame', 'requests', 'pyserial', 'serial', 'socket', 'webbrowser', 'xml.etree.ElementTree']

        MissingLibraries = []

        # Import Libraries or Mark Missing
        for Library in StandardLibraries + ExternalLibraries:
            try:
                __import__(Library)
            except ImportError:
                MissingLibraries.append(Library)

        self.Check(MissingLibraries)
    
    def Check(self, MissingLibraries):
        if not MissingLibraries:
            return

        for Library in MissingLibraries:
            self.Install(Library)
        
        sys.exit()

    def Install(self, LibraryName):
        try:
            # Install Third-Party Libraries
            subprocess.run([sys.executable, '-m', 'pip', 'install', LibraryName], check=True)
        except subprocess.CalledProcessError:
            pass

InstanceLibraries = ClassLibraries()

try:
    # Standard Libraries
    import atexit
    import calendar
    import csv
    import datetime
    import json
    import locale
    import math
    import os
    import random
    import smtplib
    import ssl
    import threading
    import time

    # Third-Party Libraries
    import clipboard
    import cv2
    from email.message import EmailMessage
    import folium
    import keyboard
    import numpy as np
    import pyautogui
    import pygame
    import pygame.gfxdraw
    from pygame.locals import QUIT
    import requests
    import serial.tools.list_ports
    import socket
    import webbrowser
    import xml.etree.ElementTree as ET

except:
    InstanceLibraries.List()

class ClassSystem:
    def __init__(self):
        # Initialize Pygame
        pygame.font.init()
        pygame.mixer.init()
        pygame.joystick.init()
        pygame.init()

        # Settings and Resources
        self.Running = True
        self.Metric = False
        self.Clock = pygame.time.Clock()
        self.Lock = threading.Lock()
        self.W = pygame.display.Info().current_w
        self.H = self.W * (9/16)
        self.Window = pygame.display.set_mode((self.W, self.H))
        self.SF = min(self.W / 1920, self.H / 1080)
        self.DataList = ''
        self.Manual = False
        self.AutoCOM = True

        self.ColorBlack = (10, 10, 10, 0.8)
        self.ColorGray = (30, 30, 30, 0.6)
        self.ColorWhite = (255, 255, 255)
        self.ColorGreen = (0, 200, 0, 0.8)
        self.ColorRed = (120, 0, 0, 0.2)

        self.Directory = os.path.dirname(os.path.abspath(__file__))
        self.Resources = os.path.join(self.Directory, "Resources")
        self.Videos = os.path.join(self.Directory, "Videos")

        # Images
        self.ButtonHelp = pygame.image.load(os.path.join(self.Resources, "ButtonHelp.png"))
        self.ButtonPower = pygame.image.load(os.path.join(self.Resources, "ButtonPower.png"))
        self.ButtonSettings = pygame.image.load(os.path.join(self.Resources, "ButtonSettings.png"))
        self.ButtonFullscreenA = pygame.image.load(os.path.join(self.Resources, "ButtonFullscreenA.png"))
        self.ButtonFullscreenB = pygame.image.load(os.path.join(self.Resources, "ButtonFullscreenB.png"))
        self.HintOn = pygame.image.load(os.path.join(self.Resources, "HintOn.png"))
        self.HintOff = pygame.image.load(os.path.join(self.Resources, "HintOff.png"))
        self.LogoMNSGC = pygame.image.load(os.path.join(self.Resources, "LogoMNSGC.png"))
        self.LogoNASA = pygame.image.load(os.path.join(self.Resources, "LogoNASA.png"))
        self.LogoNEBP = pygame.image.load(os.path.join(self.Resources, "LogoNEBP.png"))
        self.WifiOn = pygame.image.load(os.path.join(self.Resources, "WifiOn.png"))
        self.WifiOff = pygame.image.load(os.path.join(self.Resources, "WifiOff.png"))
        self.TrackingOn = pygame.image.load(os.path.join(self.Resources, "TrackingOn.png"))
        self.TrackingOff = pygame.image.load(os.path.join(self.Resources, "TrackingOff.png"))
        self.CaptureOn = pygame.image.load(os.path.join(self.Resources, "CaptureOn.png"))
        self.CaptureOff = pygame.image.load(os.path.join(self.Resources, "CaptureOff.png"))
        self.DPad = pygame.image.load(os.path.join(self.Resources, "DPad.png"))
        self.DPadDown = pygame.image.load(os.path.join(self.Resources, "DPadDown.png"))
        self.DPadLeft = pygame.image.load(os.path.join(self.Resources, "DPadLeft.png"))
        self.DPadRight = pygame.image.load(os.path.join(self.Resources, "DPadRight.png"))
        self.DPadUp = pygame.image.load(os.path.join(self.Resources, "DPadUp.png"))
        self.DPadCenter = pygame.image.load(os.path.join(self.Resources, "DPadCenter.png"))
        self.CircleBlack = pygame.image.load(os.path.join(self.Resources, "CircleBlack.png"))
        self.CircleWhite = pygame.image.load(os.path.join(self.Resources, "CircleWhite.png"))

        # Sounds
        self.Beep = os.path.join(self.Resources, "Beep.mp3")
        self.Blop = os.path.join(self.Resources, "Blop.mp3")
        self.Buzz = os.path.join(self.Resources, "Buzz.mp3")
        self.Launch00 = os.path.join(self.Resources, "Launch00.mp3")
        self.Launch10 = os.path.join(self.Resources, "Launch10.mp3")
        self.Launch30 = os.path.join(self.Resources, "Launch30.mp3")
        self.Launch60 = os.path.join(self.Resources, "Launch60.mp3")
        self.Static = os.path.join(self.Resources, "Static.mp3")
        self.Switch = os.path.join(self.Resources, "Switch.mp3")
        self.Tap = os.path.join(self.Resources, "Tap.mp3")

        # Reconfigure Resources
        self.HintOn = pygame.transform.smoothscale(self.HintOn, (int(50 * self.SF), int(60 * self.SF)))
        self.HintOff = pygame.transform.smoothscale(self.HintOff, (int(50 * self.SF), int(60 * self.SF)))
        self.LogoMNSGC = pygame.transform.smoothscale(self.LogoMNSGC, (int(800 * self.SF), int(800 * self.SF)))
        self.LogoNASA = pygame.transform.smoothscale(self.LogoNASA, (int(230 * self.SF), int(200 * self.SF)))
        self.LogoNEBP = pygame.transform.smoothscale(self.LogoNEBP, (int(200 * self.SF), int(200 * self.SF)))
        self.DPad = pygame.transform.smoothscale(self.DPad, (int(170 * self.SF), int(170 * self.SF)))
        self.DPadDown = pygame.transform.smoothscale(self.DPadDown, (int(170 * self.SF), int(170 * self.SF)))
        self.DPadLeft = pygame.transform.smoothscale(self.DPadLeft, (int(170 * self.SF), int(170 * self.SF)))
        self.DPadRight = pygame.transform.smoothscale(self.DPadRight, (int(170 * self.SF), int(170 * self.SF)))
        self.DPadUp = pygame.transform.smoothscale(self.DPadUp, (int(170 * self.SF), int(170 * self.SF)))
        self.DPadCenter = pygame.transform.smoothscale(self.DPadCenter, (int(100 * self.SF), int(100 * self.SF)))

        self.Icons = {
            "WifiOn": "WifiOn.png",
            "WifiOff": "WifiOff.png",
            "TrackingOn": "TrackingOn.png",
            "TrackingOff": "TrackingOff.png",
            "CaptureOn": "CaptureOn.png",
            "CaptureOff": "CaptureOff.png",
            "ButtonHelp": "ButtonHelp.png",
            "ButtonPower": "ButtonPower.png",
            "ButtonSettings": "ButtonSettings.png",
            "ButtonFullscreenA": "ButtonFullscreenA.png",
            "ButtonFullscreenB": "ButtonFullscreenB.png"
        }

        self.Indicators = {}
        self.Buttons = {}

        for Name, Path in self.Icons.items():
            Indicator = pygame.image.load(os.path.join(self.Resources, Path))
            Indicator = pygame.transform.smoothscale(Indicator, (int(60 * self.SF), int(60 * self.SF)))
            self.Indicators[Name] = Indicator
                
            if Name.startswith("Button"):
                Button = pygame.image.load(os.path.join(self.Resources, Path))
                Button = pygame.transform.smoothscale(Button, (int(45 * self.SF), int(45 * self.SF)))
                self.Buttons[Name] = Button

        # Window Title
        pygame.display.set_caption("HERMES Telemetry GUI")

        # Set Cursor
        pygame.mouse.set_pos((self.W, self.H))

        # Locale
        locale.setlocale(locale.LC_ALL, '')
    
    def Startup(self):
        LogoSurface = pygame.Surface((self.W, self.H))
        LogoSurface.fill((0, 0, 0))

        LogoRect = self.LogoMNSGC.get_rect(center=(self.W // 2, self.H // 2))
        LogoArea = LogoRect.inflate(20, 20)
        
        circles = []
        while len(circles) < 100:
            x = random.randint(0, self.W - 1)
            y = random.randint(0, self.H - 1)
            if not LogoArea.collidepoint(x, y):
                circles.append((x, y))

        for x, y in circles:
            pygame.draw.circle(LogoSurface, (255, 255, 255), (x, y), 1)

        for Alpha in range(0, 255, 5):
            LogoSurface.set_alpha(Alpha)
            self.Window.blit(LogoSurface, (0, 0))

            LogoAlphaSurface = self.LogoMNSGC.copy()
            LogoAlphaSurface.set_alpha(Alpha)

            self.Window.blit(LogoAlphaSurface, ((self.W - self.LogoMNSGC.get_width()) // 2,
                                                (self.H - self.LogoMNSGC.get_height()) // 2))

            pygame.display.flip()
            pygame.time.delay(40)

        LogoSurface.set_alpha(255)

        self.Window.blit(LogoSurface, (0, 0))
        self.Window.blit(self.LogoMNSGC, ((self.W - self.LogoMNSGC.get_width()) // 2,
                                           (self.H - self.LogoMNSGC.get_height()) // 2))

        pygame.display.flip()

        pygame.time.delay(1000)
        pygame.time.wait(1000)
    
    def Shutdown(self):
        if InstanceLogger.Map:
            InstanceLogger.Map.save(InstanceLogger.MapFile)
            InstanceLogger.Map = None
        InstanceLogger.MapFile = None

        if InstanceLogger.Recording:
            InstanceLogger.Recording = False
            InstanceLogger.Capture.release()
        InstanceLogger.Capture = None

        InstanceRFD.Close()
        InstanceIridium.Close()
        InstanceAPRS.Close()
        InstanceUbiquiti.Close()
        InstanceArduino.Close()

        time.sleep(0.1)

        pygame.quit()
        sys.exit()

InstanceSystem = ClassSystem()

# Messaging and Input
InputText = ''
InputWindowW = False
InputWindowH = False
InputTrackerLat = False
InputTrackerLon = False
InputTrackerAlt = False
InputPayloadLat = False
InputPayloadLon = False
InputPayloadAlt = False
InputTargetLat = False
InputTargetLon = False
InputAltOpen = False
InputAltClose = False
InputVelClose = False
InputIMEI = False
InputRFD = False
InputIridium = False
InputAPRS = False
InputUbiquiti = False
InputArduino = False
InputCOMRFD = False
InputCOMArduino = False

class ClassTracker:
    def __init__(self):
        self.Lat = 0
        self.Lon = 0
        self.Alt = 0
        self.Pan = 0
        self.Tilt = 0
        self.Distance2D = 0
        self.Distance3D = 0

InstanceTracker = ClassTracker()

class ClassPayload:
    def __init__(self):
        self.Lat = 0
        self.Lon = 0
        self.Alt = 0
        self.Pan = 0
        self.Tilt = 0
        self.Distance2D = 0
        self.Distance3D = 0

InstancePayload = ClassPayload()

class ClassTarget:
    def __init__(self):
        self.Lat = 0
        self.Lon = 0
        self.Alt = 0
        self.Pan = 0
        self.Tilt = 0
        self.Distance2D = 0
        self.Distance3D = 0

InstanceTarget = ClassTarget()

class ClassRFD:
    def __init__(self):
        self.Conditional = False
        self.Active = False
        self.SerialPort = None
        self.COMPort = None

        self.FileWrite = True
        self.Timestamp = None

        self.Lat = 0
        self.Lon = 0
        self.Alt = 0

    def Setup(self):
        self.Conditional = True

        try:
            RFDPorts = []
            Ports = serial.tools.list_ports.comports()

            for port in Ports:
                if 'RFD' in port.description:
                    RFDPorts.append(port.device)

            if RFDPorts:
                self.SerialPort = serial.Serial(
                    port=RFDPorts[0],
                    baudrate=57600,
                    parity=serial.PARITY_NONE,
                    stopbits=serial.STOPBITS_ONE,
                    bytesize=serial.EIGHTBITS,
                    timeout=None
                )

                pygame.mixer.music.load(InstanceSystem.Blop)
                pygame.mixer.music.play()

                InstanceOutput.Message = 'RFD Connected'
                self.Conditional = False
                self.Active = True

                InstanceRadio.Display()
                InstanceOutput.Display()

            else:
                ValidPorts = []

                for port in Ports:
                    if 'Arduino' not in port.description:
                        ValidPorts.append(port.device)

                if ValidPorts:
                    self.SerialPort = serial.Serial(
                        port=ValidPorts[0],
                        baudrate=57600,
                        parity=serial.PARITY_NONE,
                        stopbits=serial.STOPBITS_ONE,
                        bytesize=serial.EIGHTBITS,
                        timeout=None
                    )

                    pygame.mixer.music.load(InstanceSystem.Blop)
                    pygame.mixer.music.play()

                    InstanceOutput.Message = 'RFD Connected'
                    self.Conditional = False
                    self.Active = True

                    InstanceRadio.Display()
                    InstanceOutput.Display()
                else:
                    InstanceOutput.Message = 'RFD Unavailable'
                    self.Close()

        except Exception:
            InstanceOutput.Message = 'RFD Unavailable'
            self.Close()

    def Update(self):
        if self.SerialPort:
            try:
                self.SerialPort.timeout = 0.1
                RawData = self.SerialPort.readline()

                if RawData:
                    DecodedData = RawData.decode("utf-8")
                    InstanceSystem.DataList = DecodedData.split(",")

                    if len(InstanceSystem.DataList) >= 30:
                        packet, siv, fix, lat, lon, alt, year, month, day, hour, minute, sec, nedN, nedE, nedD, \
                        bat, bat33, bat51, bat52, aint, aext, ptemp, dint, dent, pres, ax, ay, az, pitch, roll, \
                        yaw = InstanceSystem.DataList[:31]

                        if lat != 0: self.Lat = round(float(lat) * .0000001, 6)
                        if lon != 0: self.Lon = round(float(lon) * .0000001, 6)
                        if alt != 0: self.Alt = float(alt) / 1000 * 3.28084

                        self.Timestamp = ''.join([year, month, day, hour, minute, sec])

                        DataRow = [packet, siv, fix, lat, lon, alt, year, month, day, hour, minute, sec, nedN, nedE, nedD,
                                    bat, bat33, bat51, bat52, aint, aext, ptemp, dint, dent, pres, ax, ay, az, pitch, roll, yaw]

                        if self.FileWrite:
                            InstanceSystem.Directory = os.path.join(os.getcwd(), "Data", "LogRFD")
                            os.makedirs(InstanceSystem.Directory, exist_ok=True)

                            DateString = datetime.datetime.now().strftime("%Y%m%d")
                            FileName = f"RFD_{DateString}.csv"
                            FilePath = os.path.join(InstanceSystem.Directory, FileName)

                            with open(FilePath, "a", newline='\n') as f:
                                writer = csv.writer(f, delimiter=',')
                                writer.writerow(DataRow)

            except (serial.SerialTimeoutException, Exception):
                InstanceOutput.Message = 'RFD Disconnected'
                self.Close()

        else:
            InstanceSystem.DataList = ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0',
                        '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', 'END\r\n']

    def Close(self):
        pygame.mixer.music.load(InstanceSystem.Static)
        pygame.mixer.music.play()

        self.Conditional = False
        self.Active = False

        if self.SerialPort and self.SerialPort.isOpen():
            self.SerialPort.close()
        
        self.SerialPort = None

InstanceRFD = ClassRFD()

class ClassIridium:
    def __init__(self):
        self.Conditional = False
        self.Active = False

        self.FileWrite = True
        self.Timestamp = None

        self.Modem = 0
        self.IMEI = 0

        self.BaseURL = "https://borealis.rci.montana.edu"
        self.Session = requests.Session()

        self.Lat = 0
        self.Lon = 0
        self.Alt = 0
        self.AscentRate = 0

    def Setup(self):
        self.Conditional = True
        
        try:
            req = requests.get("{}/api/meta/flights?modem_name={}".format(self.BaseURL, self.Modem))
            req.raise_for_status()
            
            pygame.mixer.music.load(InstanceSystem.Blop)
            pygame.mixer.music.play()
            
            InstanceOutput.Message = 'Iridium Connected'
            
            self.Conditional = False
            self.Active = True
            
            InstanceRadio.Display()
            InstanceOutput.Display()

        except (requests.exceptions.RequestException, IndexError, KeyError, Exception):
            InstanceOutput.Message = 'Iridium Unavailable'
            self.Close()

    def Update(self):
        if self.Active:
            try:
                URL = "{}/api/meta/flights?modem_name={}".format(self.BaseURL, self.Modem)
                Req = self.Session.get(URL)
                Req.raise_for_status()
                LatestFlight = Req.json()[-1]

                response_json = Req.json()

                latest_entry = response_json[-1]
                UID = latest_entry["uid"]

                URL = "{}/api/flight?uid={}".format(self.BaseURL, UID)
                Req = self.Session.get(URL)
                Req.raise_for_status()
                Data = Req.json()

                Fields = Data["fields"]
                Values = Data["data"]

                Entry = Values[0]
                
                self.Timestamp = datetime.datetime.fromtimestamp(Entry[Fields.index("datetime")]).strftime("%Y%m%d%H%M%S")
                
                self.Lat = Entry[Fields.index("latitude")]
                self.Lon = Entry[Fields.index("longitude")]
                self.Alt = Entry[Fields.index("altitude")]

                if self.FileWrite:
                    InstanceSystem.Directory = os.path.join(os.getcwd(), "Data", "LogIridium")
                    os.makedirs(InstanceSystem.Directory, exist_ok=True)

                    DateString = datetime.datetime.now().strftime("%Y%m%d")
                    FileName = f"Iridium_{DateString}.csv"
                    FilePath = os.path.join(InstanceSystem.Directory, FileName)

                    with open(FilePath, "a", newline='\n') as f:
                        Writer = csv.writer(f, delimiter=',')
                        Writer.writerow([self.Timestamp, self.Lat, self.Lon, self.Alt])

            except Exception:
                InstanceOutput.Message = 'Iridium Disconnected'
                self.Close()

    def Close(self):
        pygame.mixer.music.load(InstanceSystem.Static)
        pygame.mixer.music.play()

        self.Conditional = False
        self.Active = False

InstanceIridium = ClassIridium()

class ClassAPRS:
    def __init__(self):
        self.Conditional = False
        self.Active = False

        self.Callsign = None

        self.FileWrite = True
        self.Timestamp = None

        self.Session = requests.Session()

        self.Lat = 0
        self.Lon = 0
        self.Alt = 0

    def Setup(self):
        self.Conditional = True

        try:
            URL = "https://api.aprs.fi/api/get"
        
            Params = {
                'name': self.Callsign,
                'what': 'loc',
                'apikey': '186239.PvPtIQBgYaOM92d',
                'format': 'xml'
            }

            Response = requests.get(URL, params=Params)
            Response.raise_for_status()

            if Response.status_code == 200:
                root = ET.fromstring(Response.text)

                entry = root.find('entries/entry')
                name = entry.find('name').text
                lat = entry.find('lat').text
                lng = entry.find('lng').text
                alt = entry.find('altitude').text
                symbol = entry.find('symbol').text
                comment = entry.find('comment').text

            pygame.mixer.music.load(InstanceSystem.Blop)
            pygame.mixer.music.play()

            InstanceOutput.Message = 'APRS Connected'

            self.Conditional = False
            self.Active = True

            InstanceRadio.Display()
            InstanceOutput.Display()

        except (requests.exceptions.RequestException, IndexError, KeyError, Exception):
            InstanceOutput.Message = 'APRS Unavailable'
            self.Close()
    
    def Update(self):
        if self.Active:
            try:
                URL = "https://api.aprs.fi/api/get"
                Params = {
                    'name': self.Callsign,
                    'what': 'loc',
                    'apikey': '186239.PvPtIQBgYaOM92d',
                    'format': 'xml'
                }

                Response = self.Session.get(URL, params=Params)
                Response.raise_for_status()

                if Response.status_code == 200:
                    root = ET.fromstring(Response.text)
                    entry = root.find('entries/entry')
                    name = entry.find('name').text
                    lat = entry.find('lat').text
                    lon = entry.find('lng').text
                    alt = entry.find('altitude').text
                    symbol = entry.find('symbol').text
                    comment = entry.find('comment').text

                    if lat != 0: self.Lat = round(float(lat), 6)
                    if lon != 0: self.Lon = round(float(lon), 6)
                    if alt != 0: self.Alt = round(float(alt), 6)

                    self.Timestamp = datetime.datetime.fromtimestamp(int(entry.find('time').text)).strftime("%Y%m%d%H%M%S")

                    DataRow = [name, lat, lon, alt, symbol, comment]

                    if self.FileWrite:
                        InstanceSystem.Directory = os.path.join(os.getcwd(), "Data", "LogAPRS")
                        os.makedirs(InstanceSystem.Directory, exist_ok=True)

                        DateString = datetime.datetime.now().strftime("%Y%m%d")
                        FileName = f"APRS_{DateString}.csv"
                        FilePath = os.path.join(InstanceSystem.Directory, FileName)

                        with open(FilePath, "a", newline='\n') as f:
                            Writer = csv.writer(f, delimiter=',')
                            Writer.writerow(DataRow)

                else:
                    raise requests.exceptions.RequestException

            except (requests.exceptions.RequestException, ValueError, AttributeError, ET.ParseError, IndexError, Exception):
                InstanceOutput.Message = 'APRS Disconnected'
                self.Close()

    def Close(self):
        pygame.mixer.music.load(InstanceSystem.Static)
        pygame.mixer.music.play()

        self.Conditional = False
        self.Active = False

InstanceAPRS = ClassAPRS()

class ClassUbiquiti:
    def __init__(self):
        self.Conditional = False
        self.Active = False

        self.IP = 0
        self.Port = 0
        self.RTSP = 0
        self.FPS = 0
        self.Cap = None
        self.PreviousFrameSize = None
        self.PreviousFrameTime = None

    def Setup(self):
        self.Conditional = True

        self.Port = 8554
        self.FPS = 30

        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1)
            s.connect((self.IP, self.Port))
            s.shutdown(socket.SHUT_RDWR)
            s.close()

        except (socket.timeout, socket.gaierror, ConnectionRefusedError, Exception):
            InstanceOutput.Message = 'Ubiquiti Unavailable'
            self.Close()

            return

        self.RTSP = "rtsp://{}:{}/payload".format(self.IP, self.Port)

        try:
            self.Cap = cv2.VideoCapture(self.RTSP)
            if not self.Cap.isOpened():
                InstanceOutput.Message = 'Ubiquiti Unavailable'
                self.Close()
            else:
                InstanceOutput.Message = 'Ubiquiti Connected'

                self.Conditional = False
                self.Active = True

                InstanceScreen.Setting = 'Stream'

        except (cv2.error, Exception):
            InstanceOutput.Message = 'Ubiquiti Unavailable'
            self.Close()
    
    def Update(self):
        if self.Active:
            CurrentTime = pygame.time.get_ticks()
            if self.PreviousFrameTime is not None and CurrentTime - self.PreviousFrameTime < 1000 // self.FPS:
                return
            
            self.PreviousFrameTime = CurrentTime

            Ret, Frame = self.Cap.read()

            if not Ret:
                self.Cap.release()
                
                InstanceOutput.Message = 'Ubiquiti Downlink Failed'
                self.Close()

                return

            Frame = cv2.resize(Frame, (InstanceScreen.W, InstanceScreen.H))
            Frame = np.rot90(Frame, k=3)

            if PrevFrameSize != (InstanceScreen.W, InstanceScreen.H):
                Frame = cv2.cvtColor(Frame, cv2.COLOR_BGR2RGB)
                PrevFrameSize = (InstanceScreen.W, InstanceScreen.H)

            InstanceScreen.Frame = pygame.surfarray.make_surface(Frame)
        else:
            pass

    def Close(self):
        pygame.mixer.music.load(InstanceSystem.Static)
        pygame.mixer.music.play()

        self.Conditional = False
        self.Active = False

        InstanceScreen.Setting = 'Thumb'

InstanceUbiquiti = ClassUbiquiti()

class ClassArduino:
    def __init__(self):
        self.Conditional = False
        self.Active = False

        self.SerialPort = None
        self.COMPort = None

        self.Tracking = False
        self.Time1 = datetime.datetime.now()
        self.Time2 = datetime.datetime.now()

    def Setup(self):
        self.Conditional = True

        try:
            time.sleep(2)

            if InstanceSystem.AutoCOM:
                ArduinoPorts = []

                Ports = serial.tools.list_ports.comports()

                for port in Ports:
                    if 'Arduino' in port.description:
                        ArduinoPorts.append(port.device)
                    elif port.vid == 0x2341 and port.pid == 0x0043:
                        ArduinoPorts.append(port.device)
                    elif port.vid == 0x2341 and port.pid == 0x0001:
                        ArduinoPorts.append(port.device)
                    elif port.vid == 0x2A03 and port.pid == 0x0043:
                        ArduinoPorts.append(port.device)
                    elif port.vid == 0x2A03 and port.pid == 0x0001:
                        ArduinoPorts.append(port.device)

                if ArduinoPorts:
                    try:
                        self.SerialPort = serial.Serial(port=ArduinoPorts[0], baudrate=9600, timeout=0.1)

                        pygame.mixer.music.load(InstanceSystem.Blop)
                        pygame.mixer.music.play()

                        InstanceOutput.Message = 'Arduino Connected'
                        self.Conditional = False
                        self.Active = True

                        InstanceRadio.Display()
                        InstanceOutput.Display()
                    except:
                        pass
                else:
                    InstanceOutput.Message = 'Arduino Unavailable'
                    self.Close()

            else:
                self.SerialPort = serial.Serial(port=self.COMPort, baudrate=9600, timeout=.1) 

                pygame.mixer.music.load(InstanceSystem.Blop)
                pygame.mixer.music.play()

                InstanceOutput.Message = 'Arduino Connected'
                self.Conditional = False
                self.Active = True

                InstanceRadio.Display()
                InstanceOutput.Display()

        except Exception:
            InstanceOutput.Message = 'Arduino Unavailable'
            self.Close()

    def Update(self):
        if self.Active:
            try:
                if self.Tracking:
                    Command = '{:.2f}'.format(InstancePayload.Pan + InstanceCalculations.TweakPan) + "," + '{:.2f}'.format(InstancePayload.Tilt + InstanceCalculations.TweakTilt)
                else:
                    Command = '{:.2f}'.format(InstanceCalculations.TweakPan) + "," + '{:.2f}'.format(InstanceCalculations.TweakTilt)

                import datetime

                self.Time2 = datetime.datetime.now()
                if (self.Time2 - self.Time1) > datetime.timedelta(seconds=1):
                    self.SerialPort.write(Command.encode())
                    self.Time1 = self.Time2

            except (AttributeError, OSError, Exception):
                InstanceOutput.Message = 'Arduino Disconnected'
                self.Close()

    def Close(self):
        pygame.mixer.music.load(InstanceSystem.Static)
        pygame.mixer.music.play()

        self.Conditional = False
        self.Active = False

        if self.SerialPort and self.SerialPort.isOpen():
            self.SerialPort.close()
        
        self.SerialPort = None

InstanceArduino = ClassArduino()

class ClassCalculations():
    def __init__(self):
        self.TweakPan = 0
        self.TweakTilt = 0
        self.FileWrite = True

    def Calculate(self):
        if not InstanceSystem.Manual:
            WeightedRFD = 0.5
            WeightedAPRS = 0.5

            if InstanceIridium.Active and InstanceIridium.Lat != 0 and InstanceIridium.Lon != 0 and InstanceIridium.Alt != 0:
                InstancePayload.Lat = InstanceIridium.Lat
                InstancePayload.Lon = InstanceIridium.Lon
                InstancePayload.Alt = InstanceIridium.Alt

                if InstanceRFD.Active and InstanceAPRS.Active:
                    if abs(InstanceIridium.Lat - InstanceRFD.Lat) < 0.1 and abs(InstanceIridium.Lat - InstanceRFD.Lat) < 0.1:
                        CorrectedLatRFD = InstanceRFD.Lat - InstanceIridium.Lat
                        CorrectedLonRFD = InstanceRFD.Lon - InstanceIridium.Lon
                        CorrectedRFDAlt = InstanceRFD.Alt - InstanceIridium.Alt

                        CorrectedAPRSLat = InstanceAPRS.Lat - InstanceIridium.Lat
                        CorrectedAPRSLon = InstanceAPRS.Lon - InstanceIridium.Lon
                        CorrectedAPRSAlt = InstanceAPRS.Alt - InstanceIridium.Alt

                        if InstanceRFD.Lat != 0 and InstanceRFD.Lon != 0 and InstanceRFD.Alt != 0 and InstanceAPRS.Lat != 0 and InstanceAPRS.Lon != 0 and InstanceAPRS.Alt != 0:
                            InstancePayload.Lat = (WeightedRFD * CorrectedLatRFD + WeightedAPRS * CorrectedAPRSLat) / (WeightedRFD + WeightedAPRS)
                            InstancePayload.Lon = (WeightedRFD * CorrectedLonRFD + WeightedAPRS * CorrectedAPRSLon) / (WeightedRFD + WeightedAPRS)
                            InstancePayload.Alt = (WeightedRFD * CorrectedRFDAlt + WeightedAPRS * CorrectedAPRSAlt) / (WeightedRFD + WeightedAPRS)
                    
                    elif abs(InstanceIridium.Lat - InstanceRFD.Lat) >= 0.1 and abs(InstanceIridium.Lat - InstanceAPRS.Lat) < 0.1:
                        InstancePayload.Lat = (InstanceAPRS.Lat + InstanceIridium.Lat) / 2
                        InstancePayload.Lon = (InstanceAPRS.Lon + InstanceIridium.Lon) / 2
                        InstancePayload.Alt = (InstanceAPRS.Alt + InstanceIridium.Alt) / 2
                    elif abs(InstanceIridium.Lat - InstanceRFD.Lat) < 0.1 and abs(InstanceIridium.Lat - InstanceAPRS.Lat) >= 0.1:
                        InstancePayload.Lat = (InstanceRFD.Lat + InstanceIridium.Lat) / 2
                        InstancePayload.Lon = (InstanceRFD.Lon + InstanceIridium.Lon) / 2
                        InstancePayload.Alt = (InstanceRFD.Alt + InstanceIridium.Alt) / 2
                elif InstanceRFD.Active and not InstanceAPRS.Active:
                    if InstanceRFD.Lat != 0 and InstanceRFD.Lon != 0 and InstanceRFD.Alt != 0 and abs(InstanceIridium.Lat - InstanceRFD.Lat) < 0.1:
                        InstancePayload.Lat = (InstanceRFD.Lat + InstanceIridium.Lat) / 2
                        InstancePayload.Lon = (InstanceRFD.Lon + InstanceIridium.Lon) / 2
                        InstancePayload.Alt = (InstanceRFD.Alt + InstanceIridium.Alt) / 2
                elif not InstanceRFD.Active and InstanceAPRS.Active:
                    if InstanceAPRS.Lat != 0 and InstanceAPRS.Lon != 0 and InstanceAPRS.Alt != 0 and abs(InstanceIridium.Lat - InstanceAPRS.Lat) < 0.1:
                        InstancePayload.Lat = (InstanceAPRS.Lat + InstanceIridium.Lat) / 2
                        InstancePayload.Lon = (InstanceAPRS.Lon + InstanceIridium.Lon) / 2
                        InstancePayload.Alt = (InstanceAPRS.Alt + InstanceIridium.Alt) / 2

            if not InstanceIridium.Active:
                if InstanceRFD.Active and not InstanceAPRS.Active and InstanceRFD.Lat != 0 and InstanceRFD.Lon != 0 and InstanceRFD.Alt != 0:
                    InstancePayload.Lat = InstanceRFD.Lat
                    InstancePayload.Lon = InstanceRFD.Lon
                    InstancePayload.Alt = InstanceRFD.Alt
                if not InstanceRFD.Active and InstanceAPRS.Active and InstanceAPRS.Lat != 0 and InstanceAPRS.Lon != 0 and InstanceAPRS.Alt != 0:
                    InstancePayload.Lat = InstanceAPRS.Lat
                    InstancePayload.Lon = InstanceAPRS.Lon
                    InstancePayload.Alt = InstanceAPRS.Alt
                if InstanceRFD.Active and InstanceAPRS.Active and InstanceRFD.Lat != 0 and InstanceRFD.Lon != 0 and InstanceRFD.Alt != 0:
                    if InstanceAPRS.Lat != 0 and InstanceAPRS.Lon != 0 and InstanceAPRS.Alt != 0:
                        InstancePayload.Lat = (InstanceRFD.Lat + InstanceAPRS.Lat) / 2
                        InstancePayload.Lon = (InstanceRFD.Lon + InstanceAPRS.Lon) / 2
                        InstancePayload.Alt = (InstanceRFD.Alt + InstanceAPRS.Alt) / 2
                    elif InstanceAPRS.Lat == 0 and InstanceAPRS.Lon == 0 and InstanceAPRS.Alt == 0:
                        InstancePayload.Lat = InstanceRFD.Lat
                        InstancePayload.Lon = InstanceRFD.Lon
                        InstancePayload.Alt = InstanceRFD.Alt
                    elif InstanceRFD.Lat == 0 and InstanceRFD.Lon == 0 and InstanceRFD.Alt == 0:
                        InstancePayload.Lat = InstanceAPRS.Lat
                        InstancePayload.Lon = InstanceAPRS.Lon
                        InstancePayload.Alt = InstanceAPRS.Alt

        # Distance Calculation (Tracker to Payload)
        Pos1 = [InstanceTracker.Lat, InstanceTracker.Lon, InstanceTracker.Alt * 0.3048]
        Pos2 = [InstancePayload.Lat, InstancePayload.Lon, InstancePayload.Alt * 0.3048]

        Lat1, Lon1, Lat2, Lon2 = map(math.radians, [Pos1[0], Pos1[1], Pos2[0], Pos2[1]])
        Alt1, Alt2 = [Pos1[2], Pos2[2]]

        dLon = Lon2 - Lon1
        dLat = Lat2 - Lat1
        dAlt = Alt2 - Alt1

        R = 6371000.0
        a = math.sin(dLat / 2) ** 2 + math.cos(Lat1) * math.cos(Lat2) * math.sin(dLon / 2) ** 2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

        # Downrange Distance (mi)
        InstancePayload.Distance2D = 3958.8 * c

        # Line-of-Sight Distance (mi)
        InstancePayload.Distance3D = math.sqrt(InstancePayload.Distance2D ** 2 + (Pos2[2] - Pos1[2]) ** 2)

        # Intermediary Calculations
        p = (math.sin(dLat / 2)) ** 2 + math.cos(Lat1) * math.cos(Lat2) * (math.sin(dLon / 2)) ** 2
        q = 2 * math.atan2(math.sqrt(p), math.sqrt(1 - p))
        d = R * q

        # Azimuth
        y = math.sin(dLon) * math.cos(Lat2)
        x = math.cos(Lat1) * math.sin(Lat2) - math.sin(Lat1) * math.cos(Lat2) * math.cos(dLon)
        Alpha = math.atan2(y, x)

        # Heading
        if Alpha < 0:
            Alpha += 2 * math.pi

        Azimuth = (3 * math.pi / 2 - Alpha) % (2 * math.pi)
        if Azimuth >= math.pi:
            Azimuth -= 2 * math.pi

        if Alpha < 0:
            Alpha += 2 * math.pi

        Azimuth = (3 * math.pi / 2 - Alpha) % (2 * math.pi)

        if Azimuth >= math.pi and Azimuth < 2 * math.pi:
            Azimuth -= 2 * math.pi

        # Pan Angle (Deg)
        InstancePayload.Pan = (270) - math.degrees(Azimuth)

        if InstancePayload.Pan >= 360:
            InstancePayload.Pan -= 360

        # Tilt Angle (Deg)
        InstancePayload.Tilt = math.degrees(math.atan2(dAlt, d))

        # Tweak Offset
        if self.TweakPan >= 360:
            self.TweakPan -= 360
        if self.TweakTilt >= 360:
            self.TweakTilt -= 360

        if self.TweakPan <= -360:
            self.TweakPan += 360
        if self.TweakTilt <= -360:
            self.TweakTilt += 360

    def Log(self):
        HeaderRow = ["Tracker Lat (deg)", "Tracker Lon (deg)", "Tracker Alt (ft)", "Payload Lat (deg)", "Payload Lon (deg)", "Payload Alt (ft)", "2D Distance (mi)", "3D Distance (mi)", "Pan (deg)", "Tilt (deg)"]
        DataRow = [InstanceTracker.Lat, InstanceTracker.Lon, InstanceTracker.Alt, InstancePayload.Lat, InstancePayload.Lon, InstancePayload.Alt, InstancePayload.Distance2D, InstancePayload.Distance3D, InstancePayload.Pan, InstancePayload.Tilt]

        # Aggregate Data File
        if self.FileWrite:
            InstanceSystem.Directory = os.path.join(os.getcwd(), "Data", "Aggregate")
            os.makedirs(InstanceSystem.Directory, exist_ok=True)

            DateString = datetime.datetime.now().strftime("%Y%m%d")
            FileName = f"Aggregate_{DateString}.csv"
            FilePath = os.path.join(InstanceSystem.Directory, FileName)

            if DataRow[3] != 0 or DataRow[4] != 0 or DataRow[5] != 0:
                if not os.path.isfile(FilePath):
                    with open(FilePath, "w", newline='') as f:
                        Writer = csv.writer(f, delimiter=',')
                        Writer.writerow(HeaderRow)
                        Writer.writerow(DataRow)
                else:
                    with open(FilePath, "a", newline='') as f:
                        Writer = csv.writer(f, delimiter=',')
                        Writer.writerow(DataRow)
    
    def Update(self):
        self.Calculate()
        self.Log()

InstanceCalculations = ClassCalculations()

class ClassLogger:
    def __init__(self):
        self.Recording = False
        self.Capture = None

        self.Map = None
        self.MapFile = None
    
    def Update(self):
        try:
            # Launch Timer Start
            if InstanceLaunch.Launched and InstanceLaunch.LaunchTime is None:
                # Create New Map
                if self.Map is None:
                    self.Map = folium.Map()
                    Count = 1

                    if not os.path.exists("Maps"):
                        os.makedirs("Maps")

                    while os.path.exists(f"Maps/Map{Count}.html"):
                        Count += 1

                    self.MapFile = f"Maps/Map{Count}.html"

                # Create New Video
                Count = 1

                if not os.path.exists("Videos"):
                    os.makedirs("Videos")

                while os.path.exists(f"Videos/Video{Count}.mp4"):
                        Count += 1

                Timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
                Filename = f"Video{Count}.mp4"

                FourCC = cv2.self.Writer_fourcc(*"mp4v")
                self.Capture = cv2.self.Writer(os.path.join("Videos", Filename), FourCC, 20.0, (int(InstanceSystem.W), int(InstanceSystem.H)), isColor=True)
                self.Recording = True
            
            # Launch Timer Halt
            if not InstanceLaunch.Launched:
                if self.Map is not None:
                    self.Map.save(self.MapFile)
                    self.Map = None
                    self.MapFile = None

                if self.Recording:
                    self.Recording = False
                    self.Capture.release()
                    self.Capture = None

            if self.Recording:
                # Capture Frame
                Frame = pyautogui.screenshot(region=(0, 0, InstanceSystem.W, InstanceSystem.H))
                Frame = cv2.cvtColor(np.array(Frame), cv2.COLOR_RGB2BGR)
                self.Capture.write(Frame)

            # Update Map with Payload Location
            if InstanceLaunch.Launched and self.Map is not None:
                if InstancePayload.Lat != 0 and InstancePayload.Lon != 0:
                    folium.CircleMarker([InstancePayload.Lat, InstancePayload.Lon], radius=2, fill=True, color='black', fill_color='black', popup=f"{int(InstancePayload.Alt)}⠀ft").add_to(self.Map)

        except Exception:
            InstanceOutput.Message = 'Capture Error'

            if self.Recording:
                try:
                    Frame = pyautogui.screenshot(region=(0, 0, InstanceSystem.W, InstanceSystem.H))
                    Frame = cv2.cvtColor(np.array(Frame), cv2.COLOR_RGB2BGR)
                    self.Capture.write(Frame)
                except Exception:
                    InstanceOutput.Message = 'Frame Capture Error'

                if not InstanceLaunch.Launched:
                    self.Recording = False
                    self.Capture.release()
                    self.Capture = None

InstanceLogger = ClassLogger()

class ClassDescent():
    def __init__(self):
        self.Automatic = False

InstanceDescent = ClassDescent()

class ClassTitle():
    def __init__(self):
        self.MET = 0
        self.UTC = 0

    def Display(self):
        if not InstanceScreen.Fullscreen:
            # Draw Logos
            InstanceSystem.Window.blit(InstanceSystem.LogoNASA, (int(530 * InstanceSystem.SF), int(60 * InstanceSystem.SF)))
            InstanceSystem.Window.blit(InstanceSystem.LogoNEBP, (int(1180 * InstanceSystem.SF), int(60 * InstanceSystem.SF)))

            # Title
            Font = pygame.font.SysFont("Impact", int(120 * InstanceSystem.SF))
            Title = Font.render("HERMES", True, InstanceSystem.ColorWhite)
            TitleRect = Title.get_rect(center=(int(960 * InstanceSystem.SF), int(135 * InstanceSystem.SF)))
            InstanceSystem.Window.blit(Title, TitleRect)

            # Subtitle
            Font = pygame.font.SysFont("Bahnschrift", int(40 * InstanceSystem.SF))
            Subtitle = Font.render("Video Telemetry GUI", True, InstanceSystem.ColorWhite)
            SubtitleRect = Subtitle.get_rect(center=(int(InstanceSystem.W / 2), int(220 * InstanceSystem.SF)))
            InstanceSystem.Window.blit(Subtitle, SubtitleRect)

InstanceTitle = ClassTitle()

class ClassScreen:
    def __init__(self):
        self.W = 800 * InstanceSystem.SF
        self.H = 600 * InstanceSystem.SF
        self.X = (InstanceSystem.W - self.W) // 2
        self.Y = (InstanceSystem.H - self.H) // 2

        self.Frame = None

        self.Fullscreen = False
        self.Setting = 'Thumb'

        self.URL = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstley'
    
    def Display(self):
        if self.Fullscreen:
            self.W = int(InstanceSystem.W)
            self.H = int(InstanceSystem.H)
            self.X = 0
            self.Y = 0
        else:
            self.W = int(800 * InstanceSystem.SF)
            self.H = int(600 * InstanceSystem.SF)
            self.X = int(InstanceSystem.W / 2 - 400 * InstanceSystem.SF)
            self.Y = int(InstanceSystem.H / 2 - 250 * InstanceSystem.SF)

        ScreenOutline = InstanceSystem.ColorWhite
        ScreenOutlineWidth = int(6 * InstanceSystem.SF)
        ScreenDimensions = (self.X, self.Y, self.W, self.H)

        if self.Setting == 'Thumb':
            Thumb = pygame.image.load(os.path.join(InstanceSystem.Resources, "Thumb.png"))
            Thumb = pygame.transform.scale(Thumb, (self.W, self.H))
            InstanceSystem.Window.blit(Thumb, ScreenDimensions)
        
        if self.Setting == 'Stream':
            try:
                InstanceSystem.Window.blit(self.Frame, (self.X, self.Y + 50))
            except Exception:
                self.Setting = 'Thumb'
                pass
        
        pygame.draw.rect(InstanceSystem.Window, ScreenOutline, ScreenDimensions, ScreenOutlineWidth, border_radius=ScreenOutlineWidth)

InstanceScreen = ClassScreen()

class ClassAltitude:
    def __init__(self):
        self.X = 0
        self.Y = 0
        self.Enabled = True

    def Display(self):
        self.X = int(1420 * InstanceSystem.SF)
        self.Y = int(300 * InstanceSystem.SF)

        if not InstanceScreen.Fullscreen and self.Enabled:
            pygame.draw.rect(InstanceSystem.Window, InstanceSystem.ColorBlack, (self.X, self.Y, int(55 * InstanceSystem.SF), int(600 * InstanceSystem.SF)))
        
            # Indicator Marks
            for i in range(0, 120001, 1000):
                Altimeter = int(self.Y + (600 * InstanceSystem.SF) - (i * 0.005 * InstanceSystem.SF))
                if i % 5000 == 0:
                    pygame.draw.line(InstanceSystem.Window, InstanceSystem.ColorWhite, (self.X + int(22 * InstanceSystem.SF), Altimeter), (self.X + int(37 * InstanceSystem.SF), Altimeter), int(1 * InstanceSystem.SF))
                else:
                    pygame.draw.line(InstanceSystem.Window, InstanceSystem.ColorWhite, (self.X + int(25 * InstanceSystem.SF), Altimeter), (self.X + int(35 * InstanceSystem.SF), Altimeter), int(1 * InstanceSystem.SF))

            # Altitude Indicator
            Altimeter = int(self.Y + (600 * InstanceSystem.SF) - (InstancePayload.Alt * 0.005 * InstanceSystem.SF))
            pygame.draw.line(InstanceSystem.Window, InstanceSystem.ColorWhite, (self.X, Altimeter), (self.X + int(60 * InstanceSystem.SF), Altimeter), int(4 * InstanceSystem.SF))

            # Divider
            pygame.draw.line(InstanceSystem.Window, InstanceSystem.ColorWhite, (self.X + int(160 * InstanceSystem.SF), self.Y - int(20 * InstanceSystem.SF)), (self.X + int(160 * InstanceSystem.SF), self.Y + int(620 * InstanceSystem.SF)), int(4 * InstanceSystem.SF))

            # Text Markings
            Altitude = [
                (pygame.font.SysFont("Bahnschrift", int(20 * InstanceSystem.SF)), "0 ft", 595),
                (pygame.font.SysFont("Bahnschrift", int(20 * InstanceSystem.SF)), "15,000 ft", 517.5),
                (pygame.font.SysFont("Bahnschrift", int(20 * InstanceSystem.SF)), "50,000 ft", 342.5),
                (pygame.font.SysFont("Bahnschrift", int(20 * InstanceSystem.SF)), "80,000 ft", 192.5),
                (pygame.font.SysFont("Bahnschrift", int(20 * InstanceSystem.SF)), "110,000 ft", 42.5),
            ]

            for Font, Text, Offset in Altitude:
                TextSurface = Font.render(Text, True, InstanceSystem.ColorWhite)
                TextRect = TextSurface.get_rect(topleft=(self.X + int(65 * InstanceSystem.SF), self.Y + int(Offset * InstanceSystem.SF)))
                InstanceSystem.Window.blit(TextSurface, TextRect)

            # Reference Points
            Altitude = [
                (pygame.font.SysFont("Impact", int(20 * InstanceSystem.SF)), "SEA LEVEL", 595),
                (pygame.font.SysFont("Impact", int(20 * InstanceSystem.SF)), "HIGH CLOUDS", 512.5),
                (pygame.font.SysFont("Impact", int(20 * InstanceSystem.SF)), "STRATOSPHERE", 337.5),
                (pygame.font.SysFont("Impact", int(20 * InstanceSystem.SF)), "FLOAT ALTITUDE", 187.5),
                (pygame.font.SysFont("Impact", int(20 * InstanceSystem.SF)), "BURST ALTITUDE", 37.5),
            ]

            for Font, Text, Offset in Altitude:
                TextSurface = Font.render(Text, True, InstanceSystem.ColorWhite)
                TextRect = TextSurface.get_rect(topleft=(self.X + int(180 * InstanceSystem.SF), self.Y + int(Offset * InstanceSystem.SF)))
                InstanceSystem.Window.blit(TextSurface, TextRect)

            # Triangle Markers
            TriangleSize = int(10 * InstanceSystem.SF)
            TriangleColor = InstanceSystem.ColorWhite
            TriangleY = [self.Y + int(597.5 * InstanceSystem.SF), self.Y + int(520 * InstanceSystem.SF), self.Y + int(345 * InstanceSystem.SF), self.Y + int(195 * InstanceSystem.SF), self.Y + int(45 * InstanceSystem.SF)]
            TriangleX = self.X - TriangleSize + int(65 * InstanceSystem.SF)

            for Y, X in zip(TriangleY, [TriangleX] * len(TriangleY)):
                pygame.draw.polygon(InstanceSystem.Window, TriangleColor, [(X, Y), (X - TriangleSize, Y + TriangleSize / 2), (X, Y + TriangleSize)], 0)

            pygame.draw.line(InstanceSystem.Window, InstanceSystem.ColorWhite, (int(1380 * InstanceSystem.SF), int(950 * InstanceSystem.SF)), (int(1780 * InstanceSystem.SF), int(950 * InstanceSystem.SF)), 1)

            Font = pygame.font.SysFont("Bahnschrift", int(25 * InstanceSystem.SF))

            Text = Font.render("ALTITUDE", True, InstanceSystem.ColorWhite)
            TextRect = Text.get_rect(topleft=(int(1380 * InstanceSystem.SF), int(965 * InstanceSystem.SF)))
            InstanceSystem.Window.blit(Text, TextRect)

            Text = Font.render("DISTANCE", True, InstanceSystem.ColorWhite)
            TextRect = Text.get_rect(topleft=(int(1600 * InstanceSystem.SF), int(965 * InstanceSystem.SF)))
            InstanceSystem.Window.blit(Text, TextRect)

            Font = pygame.font.SysFont("Bahnschrift", int(15 * InstanceSystem.SF))

            Text = Font.render("ASCENT RATE", True, InstanceSystem.ColorWhite)
            TextRect = Text.get_rect(topleft=(int(1380 * InstanceSystem.SF), int(1005 * InstanceSystem.SF)))
            InstanceSystem.Window.blit(Text, TextRect)

            Text = Font.render("DOWNRANGE", True, InstanceSystem.ColorWhite)
            TextRect = Text.get_rect(topleft=(int(1600 * InstanceSystem.SF), int(1005 * InstanceSystem.SF)))
            InstanceSystem.Window.blit(Text, TextRect)

            Font = pygame.font.SysFont("Bahnschrift", int(20 * InstanceSystem.SF))

            if InstanceSystem.Metric:
                Text = Font.render(str("{:.0f}".format(InstancePayload.Alt * 0.3048)) + " m", True, InstanceSystem.ColorWhite)
                TextRect = Text.get_rect(topleft=(int(1505 * InstanceSystem.SF), int(970 * InstanceSystem.SF)))
                InstanceSystem.Window.blit(Text, TextRect)

                Text = Font.render(str("{:.1f}".format(InstancePayload.Distance3D * 1.60934)) + " km", True, InstanceSystem.ColorWhite)
                TextRect = Text.get_rect(topleft=(int(1725 * InstanceSystem.SF), int(970 * InstanceSystem.SF)))
                InstanceSystem.Window.blit(Text, TextRect)

                Font = pygame.font.SysFont("Bahnschrift", int(15 * InstanceSystem.SF))

                Text = Font.render(str("{:.1f}".format(InstanceIridium.AscentRate * 0.3048)) + " m/s", True, InstanceSystem.ColorWhite) if not InstanceSystem.Manual else Font.render("0 m/s", True, InstanceSystem.ColorWhite)
                TextRect = Text.get_rect(topleft=(int(1505 * InstanceSystem.SF), int(1005 * InstanceSystem.SF)))
                InstanceSystem.Window.blit(Text, TextRect)

                Text = Font.render(str("{:.1f}".format(InstancePayload.Distance2D * 1.60934)) + " km", True, InstanceSystem.ColorWhite)
                TextRect = Text.get_rect(topleft=(int(1725 * InstanceSystem.SF), int(1005 * InstanceSystem.SF)))
                InstanceSystem.Window.blit(Text, TextRect)

            else:
                Text = Font.render(str("{:.0f}".format(InstancePayload.Alt)) + " ft", True, InstanceSystem.ColorWhite)
                TextRect = Text.get_rect(topleft=(int(1505 * InstanceSystem.SF), int(970 * InstanceSystem.SF)))
                InstanceSystem.Window.blit(Text, TextRect)

                Text = Font.render(str("{:.1f}".format(InstancePayload.Distance3D)) + " mi", True, InstanceSystem.ColorWhite)
                TextRect = Text.get_rect(topleft=(int(1725 * InstanceSystem.SF), int(970 * InstanceSystem.SF)))
                InstanceSystem.Window.blit(Text, TextRect)

                Font = pygame.font.SysFont("Bahnschrift", int(15 * InstanceSystem.SF))

                Text = Font.render(str("{:.1f}".format(InstanceIridium.AscentRate)) + " ft/s", True, InstanceSystem.ColorWhite) if not InstanceSystem.Manual else Font.render("0 ft/s", True, InstanceSystem.ColorWhite)
                TextRect = Text.get_rect(topleft=(int(1505 * InstanceSystem.SF), int(1005 * InstanceSystem.SF)))
                InstanceSystem.Window.blit(Text, TextRect)

                Text = Font.render(str("{:.1f}".format(InstancePayload.Distance2D)) + " mi", True, InstanceSystem.ColorWhite)
                TextRect = Text.get_rect(topleft=(int(1725 * InstanceSystem.SF), int(1005 * InstanceSystem.SF)))
                InstanceSystem.Window.blit(Text, TextRect)

InstanceAltitude = ClassAltitude()

class ClassLocation():
    def __init__(self):
            self.X = 0
            self.Y = 0

            self.Enabled = True

            self.Mun = ''
            self.Cou = ''
            self.Sub = ''

            if InstanceSystem.Metric:
                self.Position = "0.00°N, 0.00°E | 0 m"
            else:
                self.Position = "0.00°N, 0.00°E | 0 ft"
            
            self.Location = "Location Not Set"

            self.OSM = True

            self.PreviousLat = 0
            self.PreviousLon = 0
            self.PreviousAlt = 0

    def Display(self):
        if not InstanceScreen.Fullscreen and self.Enabled:
            if (
                self.PreviousLat is None
                or self.PreviousLon is None
                or self.PreviousAlt is None
                or abs(InstancePayload.Lat - self.PreviousLat) >= 0.1
                or abs(InstancePayload.Lon - self.PreviousLon) >= 0.1
                or abs(InstancePayload.Alt - self.PreviousAlt) >= 100
            ):
                OSMData = None
                if self.OSM:
                    try:
                        Headers = {
                            'User-Agent': 'jrcook394'
                        }

                        Response = requests.get("https://nominatim.openstreetmap.org/reverse?format=json&lat={}&lon={}".format(InstancePayload.Lat, InstancePayload.Lon), headers=Headers)
                        Response.raise_for_status()
                        OSMData = Response.json()

                        if OSMData is not None:
                            Address = OSMData.get("address", {})
                            self.Mun = Address.get("town") or Address.get("city") or Address.get("nearest_town") or Address.get("nearest_city") or "Unknown"
                            self.Cou = Address.get("county")
                            self.Sub = Address.get("ISO3166-2-lvl4", "").split("-")[-1].strip()

                    except requests.exceptions.RequestException:
                        self.Location = "Location Unavailable"
                        self.OSM = False

                if InstancePayload.Lat >= 0:
                    LatDirection = "N"
                else:
                    LatDirection = "S"

                if InstancePayload.Lon >= 0:
                    LonDirection = "E"
                else:
                    LonDirection = "W"

                if InstanceSystem.Metric:
                    self.Position = "{:.2f}°{}, {:.2f}°{} | {:.0f} m".format(abs(InstancePayload.Lat), LatDirection, abs(InstancePayload.Lon), LonDirection, InstancePayload.Alt * 0.3048)
                else:
                    self.Position = "{:.2f}°{}, {:.2f}°{} | {:.0f} ft".format(abs(InstancePayload.Lat), LatDirection, abs(InstancePayload.Lon), LonDirection, InstancePayload.Alt)

                if OSMData is not None:
                    if self.Mun != "Unknown":
                        if self.Sub:
                            self.Location = "{}, {}".format(self.Mun, self.Sub)
                        else:
                            self.Location = self.Mun
                    else:
                        if self.Sub:
                            if self.Cou:
                                self.Location = "{}, {}".format(self.Cou, self.Sub)
                            else:
                                self.Location = "Rural {}".format(self.Sub)
                        else:
                            self.Location = "Location Not Set"

                    if len(self.Location) > 20:
                        self.Location = self.Location[:20] + "..."
                elif InstancePayload.Lat != 0 and InstancePayload.Lon != 0 and InstancePayload.Lon != 0:
                    self.Location = "Location Unavailable"
                else:
                    self.Location = "Location Not Set"

                self.PreviousLat = InstancePayload.Lat
                self.PreviousLon = InstancePayload.Lon
                self.PreviousAlt = InstancePayload.Alt

            if InstancePayload.Lat == 0 and InstancePayload.Lon == 0 and InstancePayload.Alt == 0:
                if InstanceSystem.Metric:
                    self.Position = "0.00°N, 0.00°E | 0 m"
                else:
                    self.Position = "0.00°N, 0.00°E | 0 ft"

            # Coordinate and Altitude Display
            Font = pygame.font.SysFont("Bahnschrift", int(25 * InstanceSystem.SF))
            Text = Font.render(self.Position, True, InstanceSystem.ColorWhite)
            TextRect = Text.get_rect(midright=(int(1372.5 * InstanceSystem.SF), int(842.5 * InstanceSystem.SF)))
            TextWidth = Text.get_width()

            RightEdge = int(1180 * InstanceSystem.SF) + 200 * InstanceSystem.SF
            RectWidth = TextWidth + int(20 * InstanceSystem.SF)
            LeftEdge = RightEdge - RectWidth

            pygame.draw.rect(InstanceSystem.Window, InstanceSystem.ColorGray, (600 * InstanceSystem.SF, 860 * InstanceSystem.SF, 780 * InstanceSystem.SF, 60 * InstanceSystem.SF))
            pygame.draw.rect(InstanceSystem.Window, InstanceSystem.ColorWhite, (600 * InstanceSystem.SF, 860 * InstanceSystem.SF, 780 * InstanceSystem.SF, 60 * InstanceSystem.SF), int(2 * InstanceSystem.SF))

            pygame.draw.rect(InstanceSystem.Window, InstanceSystem.ColorGray, (LeftEdge, 820 * InstanceSystem.SF, RectWidth, 40 * InstanceSystem.SF))
            pygame.draw.rect(InstanceSystem.Window, InstanceSystem.ColorWhite, (LeftEdge, 820 * InstanceSystem.SF, RectWidth, 40 * InstanceSystem.SF), int(2 * InstanceSystem.SF))

            pygame.draw.rect(InstanceSystem.Window, InstanceSystem.ColorGray, (LeftEdge + 2 * InstanceSystem.SF, 840 * InstanceSystem.SF, RectWidth - 4 * InstanceSystem.SF, 50 * InstanceSystem.SF))

            InstanceSystem.Window.blit(Text, TextRect)

            # Geographic Location Display
            if self.Location != '':
                Font = pygame.font.SysFont("Bahnschrift", int(40 * InstanceSystem.SF))
                Text = Font.render(self.Location, True, InstanceSystem.ColorWhite)
            else:
                Font = pygame.font.SysFont("Bahnschrift", int(30 * InstanceSystem.SF))
                Text = Font.render("Location Unavailable", True, InstanceSystem.ColorWhite)

            TextRect = Text.get_rect(midright=(int(1372.5 * InstanceSystem.SF), int(892.5 * InstanceSystem.SF)))
            InstanceSystem.Window.blit(Text, TextRect)

InstanceLocation = ClassLocation()

class ClassCompass():
    def __init__(self):
            self.X = 0
            self.Y = 0
            self.Enabled = True
            self.Setting = 1

    def Display(self):
        self.X = int(560 * InstanceSystem.SF)
        self.Y = int(890 * InstanceSystem.SF)

        if not InstanceScreen.Fullscreen and self.Enabled:
            LargeTicks = 24
            SmallTicks = 3

            LargeAngle = 2 * math.pi / LargeTicks
            SmallAngle = LargeAngle / SmallTicks

            NeedleLength = int(60 * InstanceSystem.SF)

            # Compass Outline
            InstanceSystem.CircleWhite = pygame.transform.smoothscale(InstanceSystem.CircleWhite, (int(160 * InstanceSystem.SF), int(160 * InstanceSystem.SF)))
            InstanceSystem.CircleBlack = pygame.transform.smoothscale(InstanceSystem.CircleBlack, (int(155 * InstanceSystem.SF), int(155 * InstanceSystem.SF)))
            InstanceSystem.Window.blit(InstanceSystem.CircleWhite, (int(self.X - 80 * InstanceSystem.SF), int(self.X + 250 * InstanceSystem.SF)))
            InstanceSystem.Window.blit(InstanceSystem.CircleBlack, (int(self.X - 77.5 * InstanceSystem.SF), int(self.X + 252.5 * InstanceSystem.SF)))

            # Large Circumferential Ticks
            for i in range(LargeTicks):
                Angle = LargeAngle * i
                X1 = self.X + math.cos(Angle) * int(60 * InstanceSystem.SF)
                Y1 = self.Y + math.sin(Angle) * int(60 * InstanceSystem.SF)
                X2 = self.X + math.cos(Angle) * int(70 * InstanceSystem.SF)
                Y2 = self.Y + math.sin(Angle) * int(70 * InstanceSystem.SF)

                pygame.draw.line(InstanceSystem.Window, InstanceSystem.ColorWhite, (int(X1), int(Y1)), (int(X2), int(Y2)), 1)

            # Small Radial Ticks
            for i in range(LargeTicks * SmallTicks):
                X1 = self.X + math.cos(SmallAngle * i) * int(70 * InstanceSystem.SF)
                Y1 = self.Y + math.sin(SmallAngle * i) * int(70 * InstanceSystem.SF)
                X2 = self.X + math.cos(SmallAngle * i) * int(72 * InstanceSystem.SF)
                Y2 = self.Y + math.sin(SmallAngle * i) * int(72 * InstanceSystem.SF)

                pygame.draw.line(InstanceSystem.Window, InstanceSystem.ColorWhite, (int(X1), int(Y1)), (int(X2), int(Y2)), 1)

            # Cardinal Directions
            font = pygame.font.SysFont("Bahnschrift", int(20 * InstanceSystem.SF))

            Directions = [
                ("N", (self.X, self.Y - int(40 * InstanceSystem.SF))),
                ("E", (self.X + int(40 * InstanceSystem.SF), self.Y)),
                ("S", (self.X, self.Y + int(40 * InstanceSystem.SF))),
                ("W", (self.X - int(40 * InstanceSystem.SF), self.Y)),
            ]

            for Dir, Pos in Directions:
                Text = font.render(Dir, True, InstanceSystem.ColorWhite)
                TextRect = Text.get_rect(center=Pos)
                InstanceSystem.Window.blit(Text, TextRect)

            Font = pygame.font.SysFont("Bahnschrift", int(25 * InstanceSystem.SF))

            CompassNeedleX = 0
            CompassNeedleY = 0
            CompassBaseX = 0
            CompassBaseY = 0

            # Compass Needle
            if self.Setting == 1:
                Text = Font.render("Tracker > Payload", True, InstanceSystem.ColorWhite)
                CompassNeedleX = self.X + math.cos(math.radians(InstancePayload.Pan) - math.pi / 2) * NeedleLength
                CompassNeedleY = self.Y + math.sin(math.radians(InstancePayload.Pan) - math.pi / 2) * NeedleLength
                CompassBaseX = self.X - math.cos(math.radians(InstancePayload.Pan) - math.pi / 2) * 10 * InstanceSystem.SF
                CompassBaseY = self.Y - math.sin(math.radians(InstancePayload.Pan) - math.pi / 2) * 10 * InstanceSystem.SF
            if self.Setting == 2:
                Text = Font.render("Payload > Target", True, InstanceSystem.ColorWhite)
                CompassNeedleX = self.X + math.cos(math.radians(InstanceTarget.Pan) - math.pi / 2) * NeedleLength
                CompassNeedleY = self.Y + math.sin(math.radians(InstanceTarget.Pan) - math.pi / 2) * NeedleLength
                CompassBaseX = self.X - math.cos(math.radians(InstanceTarget.Pan) - math.pi / 2) * 10 * InstanceSystem.SF
                CompassBaseY = self.Y - math.sin(math.radians(InstanceTarget.Pan) - math.pi / 2) * 10 * InstanceSystem.SF

            TextRect = Text.get_rect(topleft=(int(650 * InstanceSystem.SF), int(867.5 * InstanceSystem.SF)))
            InstanceSystem.Window.blit(Text, TextRect)

            Font = pygame.font.SysFont("Bahnschrift", int(15 * InstanceSystem.SF))

            Text = Font.render("Click Compass to Change", True, InstanceSystem.ColorWhite)
            TextRect = Text.get_rect(topleft=(int(650 * InstanceSystem.SF), int(897.5 * InstanceSystem.SF)))
            InstanceSystem.Window.blit(Text, TextRect)

            for Offset in range(-(int(3 * InstanceSystem.SF) // 2), int(3 * InstanceSystem.SF) // 2 + 1):
                pygame.draw.line(InstanceSystem.Window, (255, 0, 0), (int(CompassBaseX), int(CompassBaseY) + Offset), (int(CompassNeedleX), int(CompassNeedleY) + Offset))

            # Compass Center
            pygame.gfxdraw.filled_circle(InstanceSystem.Window, self.X, self.Y, int(10 * InstanceSystem.SF), InstanceSystem.ColorWhite)

InstanceCompass = ClassCompass()

class ClassTime():
    def __init__(self):
            self.X = 0
            self.Y = 0
            self.Enabled = True
            self.Previous = None
            self.Current = None
            self.Countdown1 = False
            self.Countdown2 = False
            self.Countdown3 = False

    def Display(self):
        try:
            # Launch Timer Start
            if InstanceLaunch.Launched and InstanceLaunch.LaunchTime is None:
                InstanceLaunch.LaunchTime = datetime.datetime.utcnow().strftime("%H:%M:%S")
                InstanceLaunch.StartTime = datetime.datetime.now()

                InstanceOutput.Message = "Launch Timer Commenced"

                if self.Countdown1:
                    pygame.mixer.music.load(InstanceSystem.Launch10)
                    pygame.mixer.music.play()
                    self.MET = "T  - 00:00:10"
                elif self.Countdown2:
                    pygame.mixer.music.load(InstanceSystem.Launch30)
                    pygame.mixer.music.play()
                    self.MET = "T  - 00:00:30"
                elif self.Countdown3:
                    pygame.mixer.music.load(InstanceSystem.Launch60)
                    pygame.mixer.music.play()
                    self.MET = "T  - 00:01:00"
                else:
                    pygame.mixer.music.load(InstanceSystem.Launch00)
                    pygame.mixer.music.play()
                    self.MET = "T  - 00:00:00"

            # Launch Timer Halt
            if not InstanceLaunch.Launched:
                InstanceLaunch.LaunchTime = None
                InstanceLaunch.StartTime = None

                self.MET = "T  - 00:00:00"

            # Update MET and UTC
            CurrentUTC = datetime.datetime.utcnow()

            if self.Previous is None or CurrentUTC.second != self.Previous:
                self.Previous = CurrentUTC.second

                if InstanceLaunch.Launched:
                    Elapsed = datetime.datetime.now() - InstanceLaunch.StartTime
                    S = Elapsed.total_seconds()

                    if self.Countdown1:
                        CountdownTime = 10
                    elif self.Countdown2:
                        CountdownTime = 30
                    elif self.Countdown3:
                        CountdownTime = 60
                    else:
                        CountdownTime = 0

                    if S < CountdownTime:
                        S = CountdownTime - S
                        H = int(S / 3600)
                        M = int((S % 3600) / 60)
                        S = int(S % 60)
                        self.MET = "T  - {:02d}:{:02d}:{:02d}".format(H, M, S)
                    else:
                        S -= CountdownTime - 1
                        H = int(S / 3600)
                        M = int((S % 3600) / 60)
                        S = int(S % 60)
                        self.MET = "T + {:02d}:{:02d}:{:02d}".format(H, M, S)

            self.UTC = CurrentUTC.strftime("%H:%M:%S")

            if not InstanceScreen.Fullscreen and self.Enabled:
                # Text Background
                pygame.draw.rect(InstanceSystem.Window, InstanceSystem.ColorGray, (int(810 * InstanceSystem.SF), int(270 * InstanceSystem.SF), int(300 * InstanceSystem.SF), int(95 * InstanceSystem.SF)))
                pygame.draw.rect(InstanceSystem.Window, InstanceSystem.ColorWhite, (int(810 * InstanceSystem.SF), int(270 * InstanceSystem.SF), int(300 * InstanceSystem.SF), int(95 * InstanceSystem.SF)), 2)

                # Text Boxes
                Font = pygame.font.SysFont("Calibri", int(50 * InstanceSystem.SF))

                if InstanceLaunch.Launched:
                    Text = Font.render(self.MET, True, InstanceSystem.ColorWhite)
                else:
                    if not self.Countdown1 and not self.Countdown2 and not self.Countdown3:
                        Text = Font.render("T  - 00:00:00", True, InstanceSystem.ColorWhite)
                    elif self.Countdown1:
                        Text = Font.render("T  - 00:00:10", True, InstanceSystem.ColorWhite)
                    elif self.Countdown2:
                        Text = Font.render("T  - 00:00:30", True, InstanceSystem.ColorWhite)
                    elif self.Countdown3:
                        Text = Font.render("T  - 00:01:00", True, InstanceSystem.ColorWhite)

                TextRect = Text.get_rect()
                TextRect.center = (int(960 * InstanceSystem.SF), int(300 * InstanceSystem.SF))
                InstanceSystem.Window.blit(Text, TextRect)

                Font = pygame.font.SysFont("Calibri", int(30 * InstanceSystem.SF))
                Text = Font.render("UTC " + self.UTC, True, InstanceSystem.ColorWhite)
                TextRect = Text.get_rect()
                TextRect.center = (int(960 * InstanceSystem.SF), int(345 * InstanceSystem.SF))
                InstanceSystem.Window.blit(Text, TextRect)

        except Exception:
            InstanceOutput.Message = 'Launch Timer Error'

InstanceTime = ClassTime()

class ClassRadio():
    def __init__(self):
        self.X = int(200 * InstanceSystem.SF)
        self.Y = int(350 * InstanceSystem.SF)
        self.W = int(60 * InstanceSystem.SF)
        self.H = int(30 * InstanceSystem.SF)
        self.S = int(70 * InstanceSystem.SF)

        self.Names = ["RFD", "Iridium", "APRS", "Ubiquiti", "Arduino"]
        self.Hovers = [False, False, False, False, False]
        self.Messages = ['RFD Connected' if InstanceRFD.Active else 'RFD Not Connected',
                         'Iridium Connected' if InstanceIridium.Active else 'Iridium Not Connected',
                         'APRS Connected' if InstanceAPRS.Active else 'APRS Not Connected',
                         'Ubiquiti Connected' if InstanceUbiquiti.Active else 'Ubiquiti Not Connected',
                         'Arduino Connected' if InstanceArduino.Active else 'Arduino Not Connected']

    def Display(self):
        if not InstanceScreen.Fullscreen:
            Font = pygame.font.SysFont("Bahnschrift", int(24 * InstanceSystem.SF))
            Text = Font.render("RADIO/SERIAL CONNECTIVITY", True, InstanceSystem.ColorWhite)
            TextRect = Text.get_rect()
            TextRect.center = (self.X + 105 * InstanceSystem.SF, 320 * InstanceSystem.SF)
            InstanceSystem.Window.blit(Text, TextRect)

            Font = pygame.font.SysFont("Bahnschrift", int(16 * InstanceSystem.SF))
            Colors = [(0, 200, 0, 0.8), (120, 0, 0, 0.2)]

            Connections = [InstanceRFD.Active, InstanceIridium.Active, InstanceAPRS.Active, InstanceUbiquiti.Active, InstanceArduino.Active]
            Conditionals = [InstanceRFD.Conditional, InstanceIridium.Conditional, InstanceAPRS.Conditional, InstanceUbiquiti.Conditional, InstanceArduino.Conditional]

            for i in range(5):
                ButtonX = int((i + 0.5) * self.S + self.X - 100 * InstanceSystem.SF)
                Color = (120, 0, 0, 0.6) if Conditionals[i] else (Colors[0] if Connections[i] else Colors[1])

                pygame.draw.rect(InstanceSystem.Window, Color, (ButtonX, self.Y, self.W, self.H))
                pygame.draw.rect(InstanceSystem.Window, (InstanceSystem.ColorGray if not self.Hovers[i] else InstanceSystem.ColorWhite), (ButtonX, self.Y, self.W, self.H), int(3 * InstanceSystem.SF))
                pygame.draw.rect(InstanceSystem.Window, InstanceSystem.ColorGray, (ButtonX, int(self.Y + 1.5 * self.H), self.W, self.H // 1.5))

                try:
                    self.Messages = ['Last Ping: {}'.format(f"{InstanceRFD.Timestamp[:4]}-{InstanceRFD.Timestamp[4:6]}-{InstanceRFD.Timestamp[6:8]} ({InstanceRFD.Timestamp[8:10]}:{InstanceRFD.Timestamp[10:12]}:{InstanceRFD.Timestamp[12:14]})") if InstanceRFD.Active and InstanceRFD.Timestamp is not None else 'RFD Not Connected',
                         'Last Ping: {}'.format(f"{InstanceIridium.Timestamp[:4]}-{InstanceIridium.Timestamp[4:6]}-{InstanceIridium.Timestamp[6:8]} ({InstanceIridium.Timestamp[8:10]}:{InstanceIridium.Timestamp[10:12]}:{InstanceIridium.Timestamp[12:14]})") if InstanceIridium.Active and InstanceIridium.Timestamp is not None else 'Iridium Not Connected',
                         'Last Ping: {}'.format(f"{InstanceAPRS.Timestamp[:4]}-{InstanceAPRS.Timestamp[4:6]}-{InstanceAPRS.Timestamp[6:8]} ({InstanceAPRS.Timestamp[8:10]}:{InstanceAPRS.Timestamp[10:12]}:{InstanceAPRS.Timestamp[12:14]})") if InstanceAPRS.Active and InstanceAPRS.Timestamp is not None else 'APRS Not Connected',
                         'Ubiquiti Connected' if InstanceUbiquiti.Active else 'Ubiquiti Not Connected',
                         'Arduino Connected' if InstanceArduino.Active else 'Arduino Not Connected']
                    
                    if self.Hovers[i]: InstanceOutput.Message = self.Messages[i]
                except Exception:
                    pass

                Text = Font.render(self.Names[i], True, InstanceSystem.ColorWhite)
                TextRect = Text.get_rect()
                TextRect.center = (ButtonX + int(self.W / 2), self.Y + int(1.8 * self.H))
                InstanceSystem.Window.blit(Text, TextRect)

            pygame.draw.line(InstanceSystem.Window, InstanceSystem.ColorWhite, (self.X - int(65 * InstanceSystem.SF), self.Y - int(12.5 * InstanceSystem.SF)), (self.X + int(275 * InstanceSystem.SF), self.Y - int(12.5 * InstanceSystem.SF)), int(3 * InstanceSystem.SF))
            pygame.draw.line(InstanceSystem.Window, InstanceSystem.ColorWhite, (self.X - int(65 * InstanceSystem.SF), self.Y + int(80 * InstanceSystem.SF)), (self.X + int(275 * InstanceSystem.SF), self.Y + int(80 * InstanceSystem.SF)), int(3 * InstanceSystem.SF))

InstanceRadio = ClassRadio()

class ClassOutput:
    def __init__(self):
        self.OutputX = int(135 * InstanceSystem.SF)
        self.OutputY = int(450 * InstanceSystem.SF)
        self.OutputW = int(340 * InstanceSystem.SF)
        self.OutputH = int(30 * InstanceSystem.SF)

        self.Message = ''

    def Display(self):
        if not InstanceScreen.Fullscreen:
            pygame.draw.rect(InstanceSystem.Window, InstanceSystem.ColorGray, (self.OutputX, self.OutputY, self.OutputW, self.OutputH))
            pygame.draw.rect(InstanceSystem.Window, InstanceSystem.ColorWhite, (self.OutputX, self.OutputY, self.OutputW, self.OutputH), 1)

            Font = pygame.font.SysFont("Bahnschrift", int(20 * InstanceSystem.SF))
            OutputText = Font.render(self.Message, True, InstanceSystem.ColorWhite)
            TextRect = OutputText.get_rect(center=(self.OutputX + self.OutputW / 2, self.OutputY + self.OutputH / 2))
            InstanceSystem.Window.blit(OutputText, TextRect)

InstanceOutput = ClassOutput()

class ClassControls():
    def __init__(self):
        self.X = int(300 * InstanceSystem.SF)
        self.Y = int(600 * InstanceSystem.SF)
        self.R = int(50 * InstanceSystem.SF)

        # D-Pad Arrows
        self.TriangleHeight = int(math.sqrt(3) * self.R / 2)
        self.TriangleShapes = [
            [(self.X, self.Y - 2 * self.TriangleHeight), (self.X - 0.75 * self.R, self.Y - self.TriangleHeight),
             (self.X + 0.75 * self.R, self.Y - self.TriangleHeight)],
            [(self.X, self.Y + 2 * self.TriangleHeight), (self.X - 0.75 * self.R, self.Y + self.TriangleHeight),
             (self.X + 0.75 * self.R, self.Y + self.TriangleHeight)],
            [(self.X + 2 * self.TriangleHeight, self.Y), (self.X + self.TriangleHeight, self.Y - 0.75 * self.R),
             (self.X + self.TriangleHeight, self.Y + 0.75 * self.R)],
            [(self.X - 2 * self.TriangleHeight, self.Y), (self.X - self.TriangleHeight, self.Y - 0.75 * self.R),
             (self.X - self.TriangleHeight, self.Y + 0.75 * self.R)]
        ]

    def Display(self):
        if not InstanceScreen.Fullscreen:
            InstanceSystem.Window.blit(InstanceSystem.DPad, (int(self.X - 85 * InstanceSystem.SF), int(self.Y - 85 * InstanceSystem.SF)))

            # Angle Displays
            FontBahnschrift28 = pygame.font.SysFont("Bahnschrift", int(28 * InstanceSystem.SF))
            FontBahnschrift20 = pygame.font.SysFont("Bahnschrift", int(20 * InstanceSystem.SF))
            FontBahnschrift25 = pygame.font.SysFont("Bahnschrift", int(25 * InstanceSystem.SF))
            FontCalibri = pygame.font.SysFont("Calibri", int(18 * InstanceSystem.SF))
            FontImpact = pygame.font.SysFont("Impact", int(32 * InstanceSystem.SF))

            Labels = [
                ("Pan: ", (self.X - 120 * InstanceSystem.SF, self.Y + 150 * InstanceSystem.SF)),
                ("Tilt: ", (self.X + 45 * InstanceSystem.SF, self.Y + 150 * InstanceSystem.SF))
            ]

            for Label, Pos in Labels:
                Text = FontBahnschrift28.render(Label, True, InstanceSystem.ColorWhite)
                TextRect = Text.get_rect(midleft=(int(Pos[0]), int(Pos[1])))
                InstanceSystem.Window.blit(Text, TextRect)

            Angles = [
                (str("{:.0f}°".format(int(InstancePayload.Pan))), (self.X - 60 * InstanceSystem.SF, self.Y + 145 * InstanceSystem.SF)),
                (str("{:.0f}°".format(int(InstancePayload.Tilt))), (self.X + 95 * InstanceSystem.SF, self.Y + 145 * InstanceSystem.SF))
            ]

            for Angle, Pos in Angles:
                Text = FontImpact.render(Angle, True, InstanceSystem.ColorWhite)
                TextRect = Text.get_rect(midleft=(int(Pos[0]), int(Pos[1])))
                InstanceSystem.Window.blit(Text, TextRect)

            Tweaks = [
                ("Tweak: {:.0f}°".format(int(InstanceCalculations.TweakPan)), (self.X - 120 * InstanceSystem.SF, self.Y + 180 * InstanceSystem.SF)),
                ("Tweak: {:.0f}°".format(int(InstanceCalculations.TweakTilt)), (self.X + 45 * InstanceSystem.SF, self.Y + 180 * InstanceSystem.SF))
            ]

            for Tweak, Pos in Tweaks:
                Text = FontCalibri.render(Tweak, True, InstanceSystem.ColorWhite)
                TextRect = Text.get_rect(midleft=(int(Pos[0]), int(Pos[1])))
                InstanceSystem.Window.blit(Text, TextRect)

            pygame.draw.line(InstanceSystem.Window, InstanceSystem.ColorWhite, (self.X - 20 * InstanceSystem.SF, self.Y - 20 * InstanceSystem.SF), (self.X - 70 * InstanceSystem.SF, self.Y - 70 * InstanceSystem.SF))
            pygame.draw.line(InstanceSystem.Window, InstanceSystem.ColorWhite, (self.X - 160 * InstanceSystem.SF, self.Y - 70 * InstanceSystem.SF), (self.X - 60 * InstanceSystem.SF, self.Y - 70 * InstanceSystem.SF))

            Text = FontBahnschrift20.render("TRACKING", True, InstanceSystem.ColorWhite)
            TextRect = Text.get_rect(midleft=(int(self.X - 160 * InstanceSystem.SF), int(self.Y - (80 * InstanceSystem.SF))))
            InstanceSystem.Window.blit(Text, TextRect)

            pygame.draw.line(InstanceSystem.Window, InstanceSystem.ColorWhite, (self.X - 70 * InstanceSystem.SF, self.Y), (self.X - 120 * InstanceSystem.SF, self.Y + 50 * InstanceSystem.SF))
            pygame.draw.line(InstanceSystem.Window, InstanceSystem.ColorWhite, (self.X - 260 * InstanceSystem.SF, self.Y + 50 * InstanceSystem.SF), (self.X - 110 * InstanceSystem.SF, self.Y + 50 * InstanceSystem.SF))

            Text = FontBahnschrift20.render("TWEAK OFFSET", True, InstanceSystem.ColorWhite)
            TextRect = Text.get_rect(midleft=(int(self.X - 260 * InstanceSystem.SF), int(self.Y + 40 * InstanceSystem.SF)))
            InstanceSystem.Window.blit(Text, TextRect)

            pygame.draw.line(InstanceSystem.Window, InstanceSystem.ColorWhite, (self.X - 150 * InstanceSystem.SF, self.Y + 140 * InstanceSystem.SF), (self.X - 150 * InstanceSystem.SF, self.Y + 180 * InstanceSystem.SF))
            pygame.draw.line(InstanceSystem.Window, InstanceSystem.ColorWhite, (self.X + 150 * InstanceSystem.SF, self.Y + 140 * InstanceSystem.SF), (self.X + 150 * InstanceSystem.SF, self.Y + 180 * InstanceSystem.SF))

            pygame.draw.line(InstanceSystem.Window, InstanceSystem.ColorWhite, (self.X - 155 * InstanceSystem.SF, self.Y + 160 * InstanceSystem.SF), (self.X - 150 * InstanceSystem.SF, self.Y + 160 * InstanceSystem.SF))
            pygame.draw.line(InstanceSystem.Window, InstanceSystem.ColorWhite, (self.X + 150 * InstanceSystem.SF, self.Y + 160 * InstanceSystem.SF), (self.X + 155 * InstanceSystem.SF, self.Y + 160 * InstanceSystem.SF))

            Text = FontBahnschrift25.render("{:.0f}°".format(InstancePayload.Pan + InstanceCalculations.TweakPan), True, InstanceSystem.ColorWhite)
            TextRect = Text.get_rect(midright=(int(self.X - 165 * InstanceSystem.SF), int(self.Y + 160 * InstanceSystem.SF)))
            InstanceSystem.Window.blit(Text, TextRect)

            Text = FontBahnschrift25.render("{:.0f}°".format(InstancePayload.Tilt + InstanceCalculations.TweakTilt), True, InstanceSystem.ColorWhite)
            TextRect = Text.get_rect(midleft=(int(self.X + 165 * InstanceSystem.SF), int(self.Y + 160 * InstanceSystem.SF)))
            InstanceSystem.Window.blit(Text, TextRect)

            pygame.draw.line(InstanceSystem.Window, InstanceSystem.ColorWhite, (self.X - 150 * InstanceSystem.SF, self.Y + 200 * InstanceSystem.SF), (self.X + 150 * InstanceSystem.SF, self.Y + 200 * InstanceSystem.SF))
            pygame.draw.line(InstanceSystem.Window, InstanceSystem.ColorWhite, (self.X, self.Y + 200 * InstanceSystem.SF), (self.X, self.Y + 210 * InstanceSystem.SF))

            Text = FontBahnschrift20.render("POINTING ANGLES", True, InstanceSystem.ColorWhite)
            TextRect = Text.get_rect(center=(int(self.X), int(self.Y + 230 * InstanceSystem.SF)))
            InstanceSystem.Window.blit(Text, TextRect)

            # Clear Buttons
            pygame.draw.rect(InstanceSystem.Window, InstanceSystem.ColorGray, (150 * InstanceSystem.SF, 1030 * InstanceSystem.SF, 95 * InstanceSystem.SF, 30 * InstanceSystem.SF))
            pygame.draw.rect(InstanceSystem.Window, InstanceSystem.ColorWhite, (150 * InstanceSystem.SF, 1030 * InstanceSystem.SF, 100 * InstanceSystem.SF, 30 * InstanceSystem.SF), int(1 * InstanceSystem.SF))

            Font = pygame.font.SysFont("Bahnschrift", int(13 * InstanceSystem.SF))
            Text = Font.render("CLEAR ANGLES", True, InstanceSystem.ColorWhite)
            TextRect = Text.get_rect()
            TextRect.center = (int(200 * InstanceSystem.SF), int(1044 * InstanceSystem.SF))
            InstanceSystem.Window.blit(Text, TextRect)

            pygame.draw.rect(InstanceSystem.Window, InstanceSystem.ColorGray, (255 * InstanceSystem.SF, 1030 * InstanceSystem.SF, 95 * InstanceSystem.SF, 30 * InstanceSystem.SF))
            pygame.draw.rect(InstanceSystem.Window, InstanceSystem.ColorWhite, (255 * InstanceSystem.SF, 1030 * InstanceSystem.SF, 100 * InstanceSystem.SF, 30 * InstanceSystem.SF), int(1 * InstanceSystem.SF))

            Font = pygame.font.SysFont("Bahnschrift", int(13 * InstanceSystem.SF))
            Text = Font.render("CLEAR TWEAKS", True, InstanceSystem.ColorWhite)
            TextRect = Text.get_rect()
            TextRect.center = (int(305 * InstanceSystem.SF), int(1044 * InstanceSystem.SF))
            InstanceSystem.Window.blit(Text, TextRect)

InstanceControls = ClassControls()

class ClassLaunch():
    def __init__(self):
        self.X = 0
        self.Y = 0
        self.W = 0
        self.H = 0
        self.S = 0
        
        self.Launched = False
        self.LaunchTime = None
        self.StartTime = None

        self.Launch1 = False
        self.Launch2 = False
        self.Reset1 = False
        self.Reset2 = False
        self.Reset3 = False
        self.Reset4 = False

        self.CountdownX = 0
        self.CountdownY = 0
        self.CountdownW = 0
        self.CountdownH = 0

        self.ResetX = 0
        self.ResetY = 0
        self.ResetW = 0
        self.ResetH = 0
        self.ResetR = 0

    def Display(self):
        # Launch Button Values
        self.X = int(960 * InstanceSystem.SF)
        self.Y = int(1020 * InstanceSystem.SF)
        self.W = int(30 * InstanceSystem.SF)
        self.H = int(30 * InstanceSystem.SF)
        self.S = int(40 * InstanceSystem.SF)

        # Reset Button Values
        self.ResetX = int(self.X + (140 * InstanceSystem.SF))
        self.ResetY = int(self.Y)
        self.ResetW = int(20 * InstanceSystem.SF)
        self.ResetH = int(20 * InstanceSystem.SF)
        self.ResetR = int(8 * InstanceSystem.SF)

        # Countdown Button Values
        self.CountdownX = 710 * InstanceSystem.SF
        self.CountdownY = 1005 * InstanceSystem.SF
        self.CountdownW = 50 * InstanceSystem.SF
        self.CountdownH = 30 * InstanceSystem.SF

        if not InstanceScreen.Fullscreen:
            BackgroundShapes = [
                ((self.X - self.S - self.W / 2, self.Y - 60 * InstanceSystem.SF), (self.W + 80 * InstanceSystem.SF, self.H + 10 * InstanceSystem.SF)),
                ((self.X - 55 * InstanceSystem.SF, self.Y + 20 * InstanceSystem.SF), (self.W + 80 * InstanceSystem.SF, self.H + 10 * InstanceSystem.SF)),
                ((self.X + 170 * InstanceSystem.SF, self.Y - 60 * InstanceSystem.SF), (self.W + 130 * InstanceSystem.SF, self.H + 90 * InstanceSystem.SF)),
                ((self.X - 250 * InstanceSystem.SF, self.Y - 60 * InstanceSystem.SF), (self.W + 130 * InstanceSystem.SF, self.H + 10 * InstanceSystem.SF)),
                ((self.X - 250 * InstanceSystem.SF, self.Y + 20 * InstanceSystem.SF), (self.W + 130 * InstanceSystem.SF, self.H + 10 * InstanceSystem.SF))
            ]

            for Rect in BackgroundShapes:
                pygame.draw.rect(InstanceSystem.Window, InstanceSystem.ColorGray, Rect)
                pygame.draw.rect(InstanceSystem.Window, (255, 255, 255, 1), Rect, int(1 * InstanceSystem.SF))

            Lines = [
                ((self.X - 60 * InstanceSystem.SF, self.Y - 60 * InstanceSystem.SF), (self.X - 60 * InstanceSystem.SF, 1080 * InstanceSystem.SF)),
                ((self.X + 60 * InstanceSystem.SF, self.Y - 60 * InstanceSystem.SF), (self.X + 60 * InstanceSystem.SF, 1080 * InstanceSystem.SF)),
                ((self.X + 65 * InstanceSystem.SF, self.Y), (self.X + 130 * InstanceSystem.SF, self.Y)),
                ((self.X + 135 * InstanceSystem.SF, self.Y - 60 * InstanceSystem.SF), (self.X + 135 * InstanceSystem.SF, self.Y + 60 * InstanceSystem.SF)),
                ((self.X + 165 * InstanceSystem.SF, self.Y - 60 * InstanceSystem.SF), (self.X + 165 * InstanceSystem.SF, self.Y + 60 * InstanceSystem.SF)),
                ((self.X - 85 * InstanceSystem.SF, self.Y - 60 * InstanceSystem.SF), (self.X - 85 * InstanceSystem.SF, self.Y + 60 * InstanceSystem.SF)),
                ((self.X - 255 * InstanceSystem.SF, self.Y - 60 * InstanceSystem.SF), (self.X - 255 * InstanceSystem.SF, self.Y + 60 * InstanceSystem.SF))
            ]

            for Line in Lines:
                pygame.draw.line(InstanceSystem.Window, InstanceSystem.ColorWhite, Line[0], Line[1])

            # Labels
            Font = pygame.font.SysFont("Bahnschrift", int(25 * InstanceSystem.SF))

            Text = Font.render("LAUNCH", True, InstanceSystem.ColorWhite)
            TextRect = Text.get_rect(center=(self.X, self.Y - int(40 * InstanceSystem.SF)))
            InstanceSystem.Window.blit(Text, TextRect)

            Text = Font.render("TIMER RESET", True, InstanceSystem.ColorWhite)
            TextRect = Text.get_rect(center=(self.X + int(250 * InstanceSystem.SF), self.Y - int(40 * InstanceSystem.SF)))
            InstanceSystem.Window.blit(Text, TextRect)

            Text = Font.render("SET CLOCK", True, InstanceSystem.ColorWhite)
            TextRect = Text.get_rect(center=(self.X - int(170 * InstanceSystem.SF), self.Y - int(40 * InstanceSystem.SF)))
            InstanceSystem.Window.blit(Text, TextRect)

            Font = pygame.font.SysFont("Bahnschrift", int(16 * InstanceSystem.SF))

            Text = Font.render("L1", True, InstanceSystem.ColorWhite)
            TextRect = Text.get_rect(center=(self.X - self.S, self.Y + int(40 * InstanceSystem.SF)))
            InstanceSystem.Window.blit(Text, TextRect)

            Text = Font.render("L2", True, InstanceSystem.ColorWhite)
            TextRect = Text.get_rect(center=(self.X + self.S, self.Y + int(40 * InstanceSystem.SF)))
            InstanceSystem.Window.blit(Text, TextRect)

            Text = Font.render("PRESS ALL FOUR", True, InstanceSystem.ColorWhite)
            TextRect = Text.get_rect(center=(self.X + int(250 * InstanceSystem.SF), self.Y + int(10 * InstanceSystem.SF)))
            InstanceSystem.Window.blit(Text, TextRect)

            Text = Font.render("TO HALT THE CLOCK", True, InstanceSystem.ColorWhite)
            TextRect = Text.get_rect(center=(self.X + int(250 * InstanceSystem.SF), self.Y + int(30 * InstanceSystem.SF)))
            InstanceSystem.Window.blit(Text, TextRect)

            # Launch Buttons
            if self.Launch1:
                Color = (0, 200, 0, 0.8)
            else:
                Color = (120, 0, 0, 0.2)

            pygame.draw.rect(InstanceSystem.Window, Color, (self.X - self.S - self.W / 2, self.Y - self.H / 2, self.W, self.H))

            if self.Launch2:
                Color = (0, 200, 0, 0.8)
            else:
                Color = (120, 0, 0, 0.2)

            pygame.draw.rect(InstanceSystem.Window, Color, (self.X + self.S - self.W / 2, self.Y - self.H / 2, self.W, self.H))

            Color = InstanceSystem.ColorWhite

            pygame.draw.rect(InstanceSystem.Window, Color, (self.X - self.S - self.W / 2, self.Y - self.H / 2, self.W, self.H), int(1 * InstanceSystem.SF))
            pygame.draw.rect(InstanceSystem.Window, Color, (self.X + self.S - self.W / 2, self.Y - self.H / 2, self.W, self.H), int(1 * InstanceSystem.SF))

            self.Launched = self.Launch1 and self.Launch2

            # Reset Buttons
            Reset = [
                (self.ResetX, self.ResetY - (-35) * InstanceSystem.SF),
                (self.ResetX, self.ResetY - (-5) * InstanceSystem.SF),
                (self.ResetX, self.ResetY - (25) * InstanceSystem.SF),
                (self.ResetX, self.ResetY - (55) * InstanceSystem.SF)
            ]

            for i in range(4):
                if [self.Reset1, self.Reset2, self.Reset3, self.Reset4][i]:
                    Color = (0, 200, 0, 0.8)
                else:
                    Color = (120, 0, 0, 0.2)

                pygame.draw.rect(InstanceSystem.Window, Color, (*Reset[i], self.ResetW, self.ResetH))

                Color = InstanceSystem.ColorWhite

                pygame.draw.rect(InstanceSystem.Window, Color, (*Reset[i], self.ResetW, self.ResetH), int(1 * InstanceSystem.SF))

            # Countdown Buttons
            Countdown = [
                (self.CountdownX, self.CountdownY),
                (self.CountdownX + 55 * InstanceSystem.SF, self.CountdownY),
                (self.CountdownX + 110 * InstanceSystem.SF, self.CountdownY)
            ]

            for i in range(3):
                if [InstanceTime.Countdown1, InstanceTime.Countdown2, InstanceTime.Countdown3][i]:
                    Color = (0, 200, 0, 0.8)
                else:
                    Color = (120, 0, 0, 0.2)

                pygame.draw.rect(InstanceSystem.Window, Color, (*Countdown[i], self.CountdownW, self.CountdownH))

                Color = InstanceSystem.ColorWhite

                pygame.draw.rect(InstanceSystem.Window, Color, (*Countdown[i], self.CountdownW, self.CountdownH), int(1 * InstanceSystem.SF))

            Text = Font.render("T-10", True, InstanceSystem.ColorWhite)
            TextRect = Text.get_rect(center=(735 * InstanceSystem.SF, 1020 * InstanceSystem.SF))
            InstanceSystem.Window.blit(Text, TextRect)

            Text = Font.render("T-30", True, InstanceSystem.ColorWhite)
            TextRect = Text.get_rect(center=(790 * InstanceSystem.SF, 1020 * InstanceSystem.SF))
            InstanceSystem.Window.blit(Text, TextRect)

            Text = Font.render("T-60", True, InstanceSystem.ColorWhite)
            TextRect = Text.get_rect(center=(845 * InstanceSystem.SF, 1020 * InstanceSystem.SF))
            InstanceSystem.Window.blit(Text, TextRect)

InstanceLaunch = ClassLaunch()

class ClassVent:
    def __init__(self):
        self.X = int(150 * InstanceSystem.SF)
        self.Y = int(940 * InstanceSystem.SF)
        self.W = int(100 * InstanceSystem.SF)
        self.H = int(30 * InstanceSystem.SF)

        self.Guard = True
        self.Manual = False
        self.Vented = False
        self.Cut = False

        self.AltOpen = None
        self.AltClose = None
        self.VelClose = None

        self.EmailSender = "nebpiridiumcommand@gmail.com"
        self.EmailPassword = "lfscbpdqtwcepffm"
        self.EmailReceiver = "data@sbd.iridium.com" # sbdservice@sbd.iridium.com 
        self.EmailSubject = str(InstanceIridium.Modem)
        self.EmailBody = ""

        self.em = EmailMessage()
        self.em['From'] = self.EmailSender
        self.em['To'] = self.EmailReceiver
        self.em['Subject'] = self.EmailSubject
        self.em.set_content(self.EmailBody)

        self.FileWrite = True

    def Display(self):
        if not InstanceScreen.Fullscreen:
            Font = pygame.font.SysFont("Bahnschrift", int(24 * InstanceSystem.SF))
            Text = Font.render("VENT COMMANDS", True, InstanceSystem.ColorWhite)
            TextRect = Text.get_rect()
            TextRect.topleft = (155 * InstanceSystem.SF, 890 * InstanceSystem.SF)
            InstanceSystem.Window.blit(Text, TextRect)

            pygame.draw.line(InstanceSystem.Window, InstanceSystem.ColorWhite, (int(150 * InstanceSystem.SF), int(920 * InstanceSystem.SF)), (int(355 * InstanceSystem.SF), int(920 * InstanceSystem.SF)), int(3 * InstanceSystem.SF))

            if self.Guard:
                pygame.draw.rect(InstanceSystem.Window, InstanceSystem.ColorGray, (self.X, self.Y - 5 * InstanceSystem.SF, 205 * InstanceSystem.SF, self.H + 10 * InstanceSystem.SF))
                pygame.draw.rect(InstanceSystem.Window, InstanceSystem.ColorWhite, (self.X, self.Y - 5 * InstanceSystem.SF, 205 * InstanceSystem.SF, self.H + 10 * InstanceSystem.SF), int(1 * InstanceSystem.SF))

                Font = pygame.font.SysFont("Bahnschrift", int(20 * InstanceSystem.SF))
                Text = Font.render("REMOVE GUARD", True, InstanceSystem.ColorWhite)
                TextRect = Text.get_rect()
                TextRect.center = (self.X + 105 * InstanceSystem.SF, self.Y + 15 * InstanceSystem.SF)

                InstanceSystem.Window.blit(Text, TextRect)
                InstanceSystem.Window.blit(Text, TextRect)

                pygame.draw.rect(InstanceSystem.Window, InstanceSystem.ColorGray, (self.X, self.Y + 40 * InstanceSystem.SF, 205 * InstanceSystem.SF, 40 * InstanceSystem.SF))
                pygame.draw.rect(InstanceSystem.Window, InstanceSystem.ColorWhite, (self.X, self.Y + 40 * InstanceSystem.SF, 205 * InstanceSystem.SF, 40 * InstanceSystem.SF), int(1 * InstanceSystem.SF))

                Font = pygame.font.SysFont("Bahnschrift", int(20 * InstanceSystem.SF))
                Text = Font.render("IRIDIUM IMEI", True, InstanceSystem.ColorWhite)
                TextRect = Text.get_rect()
                TextRect.center = (self.X + 105 * InstanceSystem.SF, self.Y + 60 * InstanceSystem.SF)

                InstanceSystem.Window.blit(Text, TextRect)
                InstanceSystem.Window.blit(Text, TextRect)
            else:
                pygame.draw.rect(InstanceSystem.Window, InstanceSystem.ColorGray, (self.X, self.Y + 40 * InstanceSystem.SF, 205 * InstanceSystem.SF, 40 * InstanceSystem.SF))
                pygame.draw.rect(InstanceSystem.Window, InstanceSystem.ColorWhite, (self.X, self.Y + 40 * InstanceSystem.SF, 205 * InstanceSystem.SF, 40 * InstanceSystem.SF), int(1 * InstanceSystem.SF))

                Font = pygame.font.SysFont("Bahnschrift", int(20 * InstanceSystem.SF))
                Text = Font.render("REPLACE GUARD", True, InstanceSystem.ColorWhite)
                TextRect = Text.get_rect()
                TextRect.center = (self.X + 105 * InstanceSystem.SF, self.Y + 60 * InstanceSystem.SF)
                InstanceSystem.Window.blit(Text, TextRect)

                if self.Vented:
                    pygame.draw.rect(InstanceSystem.Window, (0, 120, 0, 0.8), (self.X, self.Y, self.W, self.H))
                    pygame.draw.rect(InstanceSystem.Window, InstanceSystem.ColorWhite, (self.X, self.Y, self.W, self.H), int(1 * InstanceSystem.SF))
                else:
                    pygame.draw.rect(InstanceSystem.Window, (120, 0, 0, 0.8), (self.X, self.Y, self.W, self.H))
                    pygame.draw.rect(InstanceSystem.Window, InstanceSystem.ColorWhite, (self.X, self.Y, self.W, self.H), int(1 * InstanceSystem.SF))

                if self.Cut:
                    pygame.draw.rect(InstanceSystem.Window, (0, 120, 0, 0.8), (self.X + 105 * InstanceSystem.SF, self.Y, self.W, self.H))
                    pygame.draw.rect(InstanceSystem.Window, InstanceSystem.ColorWhite, (self.X + 105 * InstanceSystem.SF, self.Y, self.W, self.H), int(1 * InstanceSystem.SF))
                else:
                    pygame.draw.rect(InstanceSystem.Window, (120, 0, 0, 0.8), (self.X + 105 * InstanceSystem.SF, self.Y, self.W, self.H))
                    pygame.draw.rect(InstanceSystem.Window, InstanceSystem.ColorWhite, (self.X + 105 * InstanceSystem.SF, self.Y, self.W, self.H), int(1 * InstanceSystem.SF))

                Font = pygame.font.SysFont("Bahnschrift", int(20 * InstanceSystem.SF))
                Text = Font.render("VENT", True, InstanceSystem.ColorWhite)
                TextRect = Text.get_rect()
                TextRect.topleft = (self.X + 27.5 * InstanceSystem.SF, self.Y + 5 * InstanceSystem.SF)
                InstanceSystem.Window.blit(Text, TextRect)

                Font = pygame.font.SysFont("Bahnschrift", int(20 * InstanceSystem.SF))
                Text = Font.render("CUT", True, InstanceSystem.ColorWhite)
                TextRect = Text.get_rect()
                TextRect.topleft = (self.X + 137.5 * InstanceSystem.SF, self.Y + 5 * InstanceSystem.SF)
                InstanceSystem.Window.blit(Text, TextRect)

        if self.Vented:
            if InstanceOutput.Message == "-- VENTING --":
                 InstanceOutput.Message = ""
            else:
                InstanceOutput.Message = "-- VENTING --"
                pygame.mixer.music.load(InstanceSystem.Buzz)
                pygame.mixer.music.play()

    # Vent Opening
    def Open(self):
        if InstanceIridium.IMEI != 0:
            if InstanceIridium.Active:
                self.EmailSubject = str(InstanceIridium.Modem)

                try:
                    # Open Command
                    if os.path.exists("Resources/Commands/011.sbd"):
                        with open("Resources/Commands/011.sbd", "rb") as file:
                            FileData = file.read()

                    self.em.add_attachment(FileData, maintype="application", subtype="octet-stream", filename=os.path.basename("Resources/Commands/011.sbd"))
                    Context = ssl.create_default_context()

                    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context = Context) as smtp:
                        smtp.login(self.EmailSender, self.EmailPassword)
                        smtp.sendmail(self.EmailSender, self.EmailReceiver, self.em.as_string())

                    self.Log("Vent Opened")
                    InstanceOutput.Message = "Vent Opened"

                except Exception:
                    self.Log("Attempted Vent Open - Failed to Send Command")
                    InstanceOutput.Message = "Failed to Send Command"
            else:
                InstanceOutput.Message = "No Active Iridium"
        else:
            InstanceOutput.Message = "Input IMEI"

    # Vent Closing
    def Close(self):
        if InstanceIridium.Active:
            self.EmailSubject = str(InstanceIridium.Modem)

            try:
                # Close Command
                if os.path.exists("Resources/Commands/100.sbd"):
                    with open("Resources/Commands/100.sbd", "rb") as file:
                        FileData = file.read()

                self.em.add_attachment(FileData, maintype="application", subtype="octet-stream", filename=os.path.basename("Resources/Commands/100.sbd"))
                Context = ssl.create_default_context()

                with smtplib.SMTP_SSL('smtp.gmail.com', 465, context = Context) as smtp:
                    smtp.login(self.EmailSender, self.EmailPassword)
                    smtp.sendmail(self.EmailSender, self.EmailReceiver, self.em.as_string())

                # Idle Command
                if os.path.exists("Resources/Commands/000.sbd"):
                    with open("Resources/Commands/000.sbd", "rb") as file:
                        FileData = file.read()

                self.em.add_attachment(FileData, maintype="application", subtype="octet-stream", filename=os.path.basename("Resources/Commands/000.sbd"))
                Context = ssl.create_default_context()

                with smtplib.SMTP_SSL('smtp.gmail.com', 465, context = Context) as smtp:
                    smtp.login(self.EmailSender, self.EmailPassword)
                    smtp.sendmail(self.EmailSender, self.EmailReceiver, self.em.as_string())

                self.Log("Vent Closed")
                InstanceOutput.Message = "Vent Closed"

            except Exception:
                self.Log("Attempted Vent Close - Failed to Send Command")
                InstanceOutput.Message = "Failed to Send Command"
        else:
            InstanceOutput.Message = "No Active Iridium"
    
    # Vent Cutdown
    def Cutdown(self):
        if InstanceIridium.Active:
            self.EmailSubject = str(InstanceIridium.Modem)

            try:
                # Cut Command
                if os.path.exists("Resources/Commands/001.sbd"):
                    with open("Resources/Commands/001.sbd", "rb") as file:
                        FileData = file.read()

                self.em.add_attachment(FileData, maintype="application", subtype="octet-stream", filename=os.path.basename("Resources/Commands/001.sbd"))
                Context = ssl.create_default_context()

                with smtplib.SMTP_SSL('smtp.gmail.com', 465, context = Context) as smtp:
                    smtp.login(self.EmailSender, self.EmailPassword)
                    smtp.sendmail(self.EmailSender, self.EmailReceiver, self.em.as_string())

                # Idle Command
                if os.path.exists("Resources/Commands/000.sbd"):
                    with open("Resources/Commands/000.sbd", "rb") as file:
                        FileData = file.read()

                self.em.add_attachment(FileData, maintype="application", subtype="octet-stream", filename=os.path.basename("Resources/Commands/000.sbd"))
                Context = ssl.create_default_context()

                with smtplib.SMTP_SSL('smtp.gmail.com', 465, context = Context) as smtp:
                    smtp.login(self.EmailSender, self.EmailPassword)
                    smtp.sendmail(self.EmailSender, self.EmailReceiver, self.em.as_string())

                self.Cut = True

                self.Log("Cutdown Initiated")
                InstanceOutput.Message = "Cutdown Initiated"

            except Exception:
                self.Log("Attempted Cutdown - Failed to Send Command")
                InstanceOutput.Message = "Failed to Send Command"
        else:
            InstanceOutput.Message = "No Active Iridium"

    # Automatic Vent Control
    def Automatic(self):
        if InstanceIridium.Active and not self.Manual:
            if not self.Vented and self.AltOpen is not None and InstancePayload.Alt >= self.AltOpen - 100:
                self.Open()
            if (self.Vented and self.AltClose is not None and InstancePayload.Alt >= self.AltClose - 100) or (self.Vented and self.VelClose is not None and InstanceIridium.AscentRate <= self.VelClose + 0.5):
                self.Close()
    
    # Vent Data Log
    def Log(self, Action):
        if self.FileWrite:
            InstanceSystem.Directory = os.path.join(os.getcwd(), "Data", "Vent")
            os.makedirs(InstanceSystem.Directory, exist_ok=True)

            DateString = datetime.datetime.now().strftime("%Y%m%d")
            FileName = f"Vent_{DateString}.txt"
            FilePath = os.path.join(InstanceSystem.Directory, FileName)

            with open(FilePath, "a") as f:
                f.write("{} (MET: {}) | {}\n".format(InstanceTime.UTC, InstanceTime.MET, Action))

InstanceVent = ClassVent()

class ClassAttitude():
    def __init__(self):
        self.Heading = 0

class ClassIndicators():
    def Display(self):
        try:
            socket.create_connection(("www.google.com", 80))
            InstanceSystem.Window.blit(InstanceSystem.Indicators["WifiOn"], (int(30 * InstanceSystem.SF), int(30 * InstanceSystem.SF)))
        except Exception:
            InstanceSystem.Window.blit(InstanceSystem.Indicators["WifiOff"], (int(30 * InstanceSystem.SF), int(30 * InstanceSystem.SF)))

        if InstanceArduino.Tracking:
            InstanceSystem.Window.blit(InstanceSystem.Indicators["TrackingOn"], (int(120 * InstanceSystem.SF), int(30 * InstanceSystem.SF)))
        else:
            InstanceSystem.Window.blit(InstanceSystem.Indicators["TrackingOff"], (int(120 * InstanceSystem.SF), int(30 * InstanceSystem.SF)))

        if InstanceLaunch.Launched:
            InstanceSystem.Window.blit(InstanceSystem.Indicators["CaptureOn"], (int(210 * InstanceSystem.SF), int(30 * InstanceSystem.SF)))
        else:
            InstanceSystem.Window.blit(InstanceSystem.Indicators["CaptureOff"], (int(210 * InstanceSystem.SF), int(30 * InstanceSystem.SF)))

InstanceIndicators = ClassIndicators()

class ClassButtons:
    def __init__(self):
        self.PowerX = 0
        self.PowerY = 0
        self.PowerR = 0

        self.HelpX = 0
        self.HelpY = 0
        self.HelpR = 0

        self.SettingsX = 0
        self.SettingsY = 0
        self.SettingsR = 0

        self.FullscreenX = 0
        self.FullscreenY = 0
        self.FullscreenR = 0
    
    def Display(self):
        Coordinates = {
            "Power": {
                "x": int(1860 * InstanceSystem.SF),
                "y": int(60 * InstanceSystem.SF),
                "r": int(20 * InstanceSystem.SF)
            },
            "Help": {
                "x": int(1740 * InstanceSystem.SF),
                "y": int(60 * InstanceSystem.SF),
                "r": int(20 * InstanceSystem.SF)
            },
            "Settings": {
                "x": int(1800 * InstanceSystem.SF),
                "y": int(60 * InstanceSystem.SF),
                "r": int(20 * InstanceSystem.SF)
            },
            "Fullscreen": {
                "x": int(1300 * InstanceSystem.SF),
                "y": int(330 * InstanceSystem.SF),
                "r": int(30 * InstanceSystem.SF)
            },
            "Menu": {
                "x": int((InstanceSystem.W - InstanceSettings.MenuW) // 2),
                "y": int((InstanceSystem.H - InstanceSettings.MenuH) // 2),
                "w": int(InstanceSystem.W // 1.5),
                "h": int(InstanceSystem.H // 1.5)
            }
        }

        self.PowerX = Coordinates["Power"]["x"]
        self.PowerY = Coordinates["Power"]["y"]
        self.PowerR = Coordinates["Power"]["r"]

        InstanceSystem.Window.blit(InstanceSystem.Buttons["ButtonPower"], (int(self.PowerX - 20 * InstanceSystem.SF), int(self.PowerY - 20 * InstanceSystem.SF)))

        self.HelpX = Coordinates["Help"]["x"]
        self.HelpY = Coordinates["Help"]["y"]
        self.HelpR = Coordinates["Help"]["r"]

        InstanceSystem.Window.blit(InstanceSystem.Buttons["ButtonHelp"], (int(self.HelpX - 20 * InstanceSystem.SF), int(self.HelpY - 20 * InstanceSystem.SF)))

        self.SettingsX = Coordinates["Settings"]["x"]
        self.SettingsY = Coordinates["Settings"]["y"]
        self.SettingsR = Coordinates["Settings"]["r"]

        InstanceSystem.Window.blit(InstanceSystem.Buttons["ButtonSettings"], (int(self.SettingsX - 20 * InstanceSystem.SF), int(self.SettingsY - 20 * InstanceSystem.SF)))

        if InstanceScreen.Fullscreen:
            self.FullscreenX = int(1840 * InstanceSystem.SF)
            self.FullscreenY = int(130 * InstanceSystem.SF)
            self.FullscreenR = int(20 * InstanceSystem.SF)

            InstanceSystem.Window.blit(InstanceSystem.Indicators["ButtonFullscreenB"], (int(self.FullscreenX - 20 * InstanceSystem.SF), int(self.FullscreenY - 20 * InstanceSystem.SF)))
        else:
            self.FullscreenX = Coordinates["Fullscreen"]["x"]
            self.FullscreenY = Coordinates["Fullscreen"]["y"]
            self.FullscreenR = Coordinates["Fullscreen"]["r"]

            InstanceSystem.Window.blit(InstanceSystem.Indicators["ButtonFullscreenA"], (int(self.FullscreenX - 20 * InstanceSystem.SF), int(self.FullscreenY - 20 * InstanceSystem.SF)))

        InstanceSettings.MenuX = Coordinates["Menu"]["x"]
        InstanceSettings.MenuY = Coordinates["Menu"]["y"]
        InstanceSettings.MenuW = Coordinates["Menu"]["w"]
        InstanceSettings.MenuH = Coordinates["Menu"]["h"]

InstanceButtons = ClassButtons()

class ClassSettings:
    def __init__(self):
        self.Active = False
        self.MenuX = 0
        self.MenuY = 0
        self.MenuW = 0
        self.MenuH = 0
    
    def Display(self):
        if self.Active:
            # Draw Settings Menu
            pygame.draw.rect(InstanceSystem.Window, InstanceSystem.ColorBlack, (self.MenuX, self.MenuY, self.MenuW, self.MenuH))
            pygame.draw.rect(InstanceSystem.Window, InstanceSystem.ColorWhite, (self.MenuX, self.MenuY, self.MenuW, self.MenuH), 2)

            # Menu Title
            Font = pygame.font.SysFont("Impact", int(80 * InstanceSystem.SF))
            Text = Font.render("SETTINGS", True, InstanceSystem.ColorWhite)
            TextRect = Text.get_rect(center=(self.MenuX + self.MenuW // 2, self.MenuY))

            HeaderW = TextRect.width + int(15 * InstanceSystem.SF)
            HeaderH = TextRect.height + int(5 * InstanceSystem.SF)
            HeaderX = self.MenuX + (self.MenuW - HeaderW) // 2
            HeaderY = TextRect.centery - HeaderH // 2

            # Header Background
            pygame.draw.rect(InstanceSystem.Window, InstanceSystem.ColorBlack, (HeaderX, HeaderY, HeaderW, HeaderH))
            pygame.draw.rect(InstanceSystem.Window, InstanceSystem.ColorWhite, (HeaderX, HeaderY, HeaderW, HeaderH), int(2 * InstanceSystem.SF))

            InstanceSystem.Window.blit(Text, (TextRect.left, TextRect.top))

            Font = pygame.font.SysFont("Bahnschrift", int(30 * InstanceSystem.SF))
            Text = Font.render("UI SCALE", True, InstanceSystem.ColorWhite)
            TextRect = Text.get_rect(topleft=(int(360 * InstanceSystem.SF), int(265 * InstanceSystem.SF)))

            InstanceSystem.Window.blit(Text, (TextRect.left, TextRect.top))

            # UI Width Input
            pygame.draw.rect(InstanceSystem.Window, InstanceSystem.ColorBlack, (int(360 * InstanceSystem.SF), int(300 * InstanceSystem.SF), int(120 * InstanceSystem.SF), int(30 * InstanceSystem.SF)))
            pygame.draw.rect(InstanceSystem.Window, InstanceSystem.ColorWhite, (int(360 * InstanceSystem.SF), int(300 * InstanceSystem.SF), int(120 * InstanceSystem.SF), int(30 * InstanceSystem.SF)), int(1 * InstanceSystem.SF))

            Font = pygame.font.SysFont("Bahnschrift", int(16 * InstanceSystem.SF))
            Text = Font.render("UI WIDTH", True, InstanceSystem.ColorWhite)
            TextRect = Text.get_rect()
            TextRect.center = (int(420 * InstanceSystem.SF), int(315 * InstanceSystem.SF))

            InstanceSystem.Window.blit(Text, TextRect)

            # UI Height Input
            pygame.draw.rect(InstanceSystem.Window, InstanceSystem.ColorBlack, (int(490 * InstanceSystem.SF), int(300 * InstanceSystem.SF), int(120 * InstanceSystem.SF), int(30 * InstanceSystem.SF)))
            pygame.draw.rect(InstanceSystem.Window, InstanceSystem.ColorWhite, (int(490 * InstanceSystem.SF), int(300 * InstanceSystem.SF), int(120 * InstanceSystem.SF), int(30 * InstanceSystem.SF)), int(1 * InstanceSystem.SF))

            Font = pygame.font.SysFont("Bahnschrift", int(16 * InstanceSystem.SF))
            Text = Font.render("UI HEIGHT", True, InstanceSystem.ColorWhite)
            TextRect = Text.get_rect()
            TextRect.center = (int(550 * InstanceSystem.SF), int(315 * InstanceSystem.SF))

            InstanceSystem.Window.blit(Text, TextRect)

            # Peripherals
            Font = pygame.font.SysFont("Bahnschrift", int(30 * InstanceSystem.SF))
            Text = Font.render("PERIPHERALS", True, InstanceSystem.ColorWhite)
            TextRect = Text.get_rect(topleft=(int(360 * InstanceSystem.SF), int(380 * InstanceSystem.SF)))

            InstanceSystem.Window.blit(Text, (TextRect.left, TextRect.top))

            Font = pygame.font.SysFont("Bahnschrift", int(25 * InstanceSystem.SF))

            Text = Font.render("Altimeter", True, InstanceSystem.ColorWhite)
            TextRect = Text.get_rect(topleft=(int(390 * InstanceSystem.SF), int(420 * InstanceSystem.SF)))
            InstanceSystem.Window.blit(Text, (TextRect.left, TextRect.top))

            Text = Font.render("Navigator", True, InstanceSystem.ColorWhite)
            TextRect = Text.get_rect(topleft=(int(390 * InstanceSystem.SF), int(460 * InstanceSystem.SF)))

            InstanceSystem.Window.blit(Text, (TextRect.left, TextRect.top))

            Text = Font.render("Compass", True, InstanceSystem.ColorWhite)
            TextRect = Text.get_rect(topleft=(int(390 * InstanceSystem.SF), int(500 * InstanceSystem.SF)))

            InstanceSystem.Window.blit(Text, (TextRect.left, TextRect.top))

            Text = Font.render("Clock", True, InstanceSystem.ColorWhite)
            TextRect = Text.get_rect(topleft=(int(390 * InstanceSystem.SF), int(540 * InstanceSystem.SF)))

            InstanceSystem.Window.blit(Text, (TextRect.left, TextRect.top))

            if InstanceAltitude.Enabled:
                Color = (0, 200, 0, 0.8)
            else:
                Color = (120, 0, 0, 0.2)

            pygame.draw.rect(InstanceSystem.Window, Color, (int(360 * InstanceSystem.SF), int(420 * InstanceSystem.SF), int(20 * InstanceSystem.SF), int(20 * InstanceSystem.SF)))

            if InstanceLocation.Enabled:
                Color = (0, 200, 0, 0.8)
            else:
                Color = (120, 0, 0, 0.2)

            pygame.draw.rect(InstanceSystem.Window, Color, (int(360 * InstanceSystem.SF), int(460 * InstanceSystem.SF), int(20 * InstanceSystem.SF), int(20 * InstanceSystem.SF)))

            if InstanceCompass.Enabled:
                Color = (0, 200, 0, 0.8)
            else:
                Color = (120, 0, 0, 0.2)

            pygame.draw.rect(InstanceSystem.Window, Color, (int(360 * InstanceSystem.SF), int(500 * InstanceSystem.SF), int(20 * InstanceSystem.SF), int(20 * InstanceSystem.SF)))

            if InstanceTime.Enabled:
                Color = (0, 200, 0, 0.8)
            else:
                Color = (120, 0, 0, 0.2)

            pygame.draw.rect(InstanceSystem.Window, Color, (int(360 * InstanceSystem.SF), int(540 * InstanceSystem.SF), int(20 * InstanceSystem.SF), int(20 * InstanceSystem.SF)))

            pygame.draw.rect(InstanceSystem.Window, (255,255,255), (int(360 * InstanceSystem.SF), int(420 * InstanceSystem.SF), int(20 * InstanceSystem.SF), int(20 * InstanceSystem.SF)), 1)
            pygame.draw.rect(InstanceSystem.Window, (255,255,255), (int(360 * InstanceSystem.SF), int(460 * InstanceSystem.SF), int(20 * InstanceSystem.SF), int(20 * InstanceSystem.SF)), 1)
            pygame.draw.rect(InstanceSystem.Window, (255,255,255), (int(360 * InstanceSystem.SF), int(500 * InstanceSystem.SF), int(20 * InstanceSystem.SF), int(20 * InstanceSystem.SF)), 1)
            pygame.draw.rect(InstanceSystem.Window, (255,255,255), (int(360 * InstanceSystem.SF), int(540 * InstanceSystem.SF), int(20 * InstanceSystem.SF), int(20 * InstanceSystem.SF)), 1)

            # Metric Units
            Font = pygame.font.SysFont("Bahnschrift", int(25 * InstanceSystem.SF))
            Text = Font.render("Metric Units", True, InstanceSystem.ColorWhite)
            TextRect = Text.get_rect(topleft=(int(895 * InstanceSystem.SF), int(565 * InstanceSystem.SF)))

            InstanceSystem.Window.blit(Text, (TextRect.left, TextRect.top))

            if InstanceSystem.Metric:
                Color = (0, 200, 0)
            else:
                Color = (120, 0, 0)

            pygame.gfxdraw.filled_circle(InstanceSystem.Window, int(860 * InstanceSystem.SF), int(575 * InstanceSystem.SF), int(15 * InstanceSystem.SF), Color)
            pygame.gfxdraw.aacircle(InstanceSystem.Window, int(860 * InstanceSystem.SF), int(575 * InstanceSystem.SF), int(15 * InstanceSystem.SF), InstanceSystem.ColorWhite)

            # Automatic Tracking
            Font = pygame.font.SysFont("Bahnschrift", int(30 * InstanceSystem.SF))
            Text = Font.render("AUTOMATIC RADIO TRACKING", True, InstanceSystem.ColorWhite)
            TextRect = Text.get_rect(topleft=(int(360 * InstanceSystem.SF), int(620 * InstanceSystem.SF)))

            InstanceSystem.Window.blit(Text, (TextRect.left, TextRect.top))

            Font = pygame.font.SysFont("Bahnschrift", int(25 * InstanceSystem.SF))
            Text = Font.render("Disable for Manual Entry", True, InstanceSystem.ColorWhite)
            TextRect = Text.get_rect(topleft=(int(410 * InstanceSystem.SF), int(663 * InstanceSystem.SF)))

            InstanceSystem.Window.blit(Text, (TextRect.left, TextRect.top))

            if not InstanceSystem.Manual:
                Color = (0, 200, 0)
            else:
                Color = (120, 0, 0)

            pygame.gfxdraw.filled_circle(InstanceSystem.Window, int(375 * InstanceSystem.SF), int(675 * InstanceSystem.SF), int(15 * InstanceSystem.SF), Color)
            pygame.gfxdraw.aacircle(InstanceSystem.Window, int(375 * InstanceSystem.SF), int(675 * InstanceSystem.SF), int(15 * InstanceSystem.SF), InstanceSystem.ColorWhite)

            # Automatic Venting
            Font = pygame.font.SysFont("Bahnschrift", int(30 * InstanceSystem.SF))
            Text = Font.render("AUTOMATIC VENT COMMANDING", True, InstanceSystem.ColorWhite)
            TextRect = Text.get_rect(topleft=(int(845 * InstanceSystem.SF), int(620 * InstanceSystem.SF)))

            InstanceSystem.Window.blit(Text, (TextRect.left, TextRect.top))

            Font = pygame.font.SysFont("Bahnschrift", int(25 * InstanceSystem.SF))
            Text = Font.render("Enable for Automatic Float", True, InstanceSystem.ColorWhite)
            TextRect = Text.get_rect(topleft=(int(895 * InstanceSystem.SF), int(663 * InstanceSystem.SF)))

            InstanceSystem.Window.blit(Text, (TextRect.left, TextRect.top))

            if not InstanceVent.Manual:
                Color = (0, 200, 0)
            else:
                Color = (120, 0, 0)

            pygame.gfxdraw.filled_circle(InstanceSystem.Window, int(860 * InstanceSystem.SF), int(675 * InstanceSystem.SF), int(15 * InstanceSystem.SF), Color)
            pygame.gfxdraw.aacircle(InstanceSystem.Window, int(860 * InstanceSystem.SF), int(675 * InstanceSystem.SF), int(15 * InstanceSystem.SF), InstanceSystem.ColorWhite)

            # Coordinate Input
            if not InstanceSystem.Manual:
                Color = (150, 150, 150, 0.2)
            else:
                Color = InstanceSystem.ColorWhite

            Font = pygame.font.SysFont("Bahnschrift", int(16 * InstanceSystem.SF))
            Text = Font.render("PAYLOAD LAT", True, Color)
            TextRect = Text.get_rect()
            TextRect.center = (int(420 * InstanceSystem.SF), int(725 * InstanceSystem.SF))

            InstanceSystem.Window.blit(Text, TextRect)

            Font = pygame.font.SysFont("Bahnschrift", int(16 * InstanceSystem.SF))
            Text = Font.render("PAYLOAD LON", True, Color)
            TextRect = Text.get_rect()
            TextRect.center = (int(550 * InstanceSystem.SF), int(725 * InstanceSystem.SF))

            InstanceSystem.Window.blit(Text, TextRect)

            Font = pygame.font.SysFont("Bahnschrift", int(16 * InstanceSystem.SF))
            Text = Font.render("PAYLOAD ALT", True, Color)
            TextRect = Text.get_rect()
            TextRect.center = (int(680 * InstanceSystem.SF), int(725 * InstanceSystem.SF))

            InstanceSystem.Window.blit(Text, TextRect)

            pygame.draw.rect(InstanceSystem.Window, Color, (int(360 * InstanceSystem.SF), int(710 * InstanceSystem.SF), int(120 * InstanceSystem.SF), int(30 * InstanceSystem.SF)), 1)
            pygame.draw.rect(InstanceSystem.Window, Color, (int(490 * InstanceSystem.SF), int(710 * InstanceSystem.SF), int(120 * InstanceSystem.SF), int(30 * InstanceSystem.SF)), 1)
            pygame.draw.rect(InstanceSystem.Window, Color, (int(620 * InstanceSystem.SF), int(710 * InstanceSystem.SF), int(120 * InstanceSystem.SF), int(30 * InstanceSystem.SF)), 1)

            pygame.draw.line(InstanceSystem.Window, InstanceSystem.ColorWhite, (int(360 * InstanceSystem.SF), int(750 * InstanceSystem.SF)), (int(740 * InstanceSystem.SF), int(750 * InstanceSystem.SF)), int(4 * InstanceSystem.SF))

            Color = InstanceSystem.ColorWhite

            Font = pygame.font.SysFont("Bahnschrift", int(16 * InstanceSystem.SF))
            Text = Font.render("TRACKER LAT", True, Color)
            TextRect = Text.get_rect()
            TextRect.center = (int(420 * InstanceSystem.SF), int(780 * InstanceSystem.SF))

            InstanceSystem.Window.blit(Text, TextRect)

            Font = pygame.font.SysFont("Bahnschrift", int(16 * InstanceSystem.SF))
            Text = Font.render("TRACKER LON", True, Color)
            TextRect = Text.get_rect()
            TextRect.center = (int(550 * InstanceSystem.SF), int(780 * InstanceSystem.SF))

            InstanceSystem.Window.blit(Text, TextRect)

            Font = pygame.font.SysFont("Bahnschrift", int(16 * InstanceSystem.SF))
            Text = Font.render("TRACKER ALT", True, Color)
            TextRect = Text.get_rect()
            TextRect.center = (int(680 * InstanceSystem.SF), int(780 * InstanceSystem.SF))

            InstanceSystem.Window.blit(Text, TextRect)

            pygame.draw.rect(InstanceSystem.Window, Color, (int(360 * InstanceSystem.SF), int(765 * InstanceSystem.SF), int(120 * InstanceSystem.SF), int(30 * InstanceSystem.SF)), 1)
            pygame.draw.rect(InstanceSystem.Window, Color, (int(490 * InstanceSystem.SF), int(765 * InstanceSystem.SF), int(120 * InstanceSystem.SF), int(30 * InstanceSystem.SF)), 1)
            pygame.draw.rect(InstanceSystem.Window, Color, (int(620 * InstanceSystem.SF), int(765 * InstanceSystem.SF), int(120 * InstanceSystem.SF), int(30 * InstanceSystem.SF)), 1)

            Font = pygame.font.SysFont("Bahnschrift", int(16 * InstanceSystem.SF))
            
            if InstanceSystem.Metric:
                Text = Font.render("Tracker: ({:.2f}°, {:.2f}°) {:.0f} m".format(InstanceTracker.Lat, InstanceTracker.Lon, InstanceTracker.Alt * 0.3048), True, Color)
            else:
                Text = Font.render("Tracker: ({:.2f}°, {:.2f}°) {:.0f} ft".format(InstanceTracker.Lat, InstanceTracker.Lon, InstanceTracker.Alt), True, Color)
            
            TextRect = Text.get_rect()
            TextRect.center = (int(550 * InstanceSystem.SF), int(820 * InstanceSystem.SF))

            InstanceSystem.Window.blit(Text, TextRect)

            if InstanceSystem.Metric:
                Text = Font.render("Payload: ({:.2f}°, {:.2f}°) {:.0f} m".format(InstancePayload.Lat, InstancePayload.Lon, InstancePayload.Alt * 0.3048), True, Color)
            else:
                Text = Font.render("Payload: ({:.2f}°, {:.2f}°) {:.0f} ft".format(InstancePayload.Lat, InstancePayload.Lon, InstancePayload.Alt), True, Color)
            
            TextRect = Text.get_rect()
            TextRect.center = (int(550 * InstanceSystem.SF), int(840 * InstanceSystem.SF))

            InstanceSystem.Window.blit(Text, TextRect)

            # Float Input
            Font = pygame.font.SysFont("Bahnschrift", int(20 * InstanceSystem.SF))
            Text = Font.render("BEGIN VENTING AT", True, InstanceSystem.ColorWhite)
            TextRect = Text.get_rect()
            TextRect.center = (int(930 * InstanceSystem.SF), int(725 * InstanceSystem.SF))

            InstanceSystem.Window.blit(Text, TextRect)

            if InstanceVent.Manual:
                Color = (150, 150, 150, 0.2)
            else:
                Color = InstanceSystem.ColorWhite

            Font = pygame.font.SysFont("Bahnschrift", int(16 * InstanceSystem.SF))

            if InstanceSystem.Metric:
                Text = Font.render("ALTITUDE (m)", True, Color)
            else:
                Text = Font.render("ALTITUDE (ft)", True, Color)

            TextRect = Text.get_rect()
            TextRect.topleft = (int(1040 * InstanceSystem.SF), int(717.5 * InstanceSystem.SF))

            InstanceSystem.Window.blit(Text, TextRect)

            pygame.draw.rect(InstanceSystem.Window, Color, (int(1030 * InstanceSystem.SF), int(710 * InstanceSystem.SF), int(240 * InstanceSystem.SF), int(30 * InstanceSystem.SF)), 1)

            pygame.draw.line(InstanceSystem.Window, InstanceSystem.ColorWhite, (int(840 * InstanceSystem.SF), int(750 * InstanceSystem.SF)), (int(1275 * InstanceSystem.SF), int(750 * InstanceSystem.SF)), int(4 * InstanceSystem.SF))

            Font = pygame.font.SysFont("Bahnschrift", int(20 * InstanceSystem.SF))
            Text = Font.render("CLOSE AT            OR", True, InstanceSystem.ColorWhite)
            TextRect = Text.get_rect()
            TextRect.topleft = (int(845 * InstanceSystem.SF), int(770 * InstanceSystem.SF))

            InstanceSystem.Window.blit(Text, TextRect)

            Font = pygame.font.SysFont("Bahnschrift", int(16 * InstanceSystem.SF))

            if InstanceSystem.Metric:
                Text = Font.render("m/s", True, Color)
            else:
                Text = Font.render("ft/s", True, Color)

            TextRect = Text.get_rect()
            TextRect.topleft = (int(947.5 * InstanceSystem.SF), int(772.5 * InstanceSystem.SF))

            InstanceSystem.Window.blit(Text, TextRect)

            pygame.draw.rect(InstanceSystem.Window, Color, (int(940 * InstanceSystem.SF), int(765 * InstanceSystem.SF), int(40 * InstanceSystem.SF), int(30 * InstanceSystem.SF)), 1)

            Font = pygame.font.SysFont("Bahnschrift", int(16 * InstanceSystem.SF))

            if InstanceSystem.Metric:
                Text = Font.render("ALTITUDE (m)", True, Color)
            else:
                Text = Font.render("ALTITUDE (ft)", True, Color)

            TextRect = Text.get_rect()
            TextRect.topleft = (int(1040 * InstanceSystem.SF), int(772.5 * InstanceSystem.SF))

            InstanceSystem.Window.blit(Text, TextRect)

            pygame.draw.rect(InstanceSystem.Window, Color, (int(1030 * InstanceSystem.SF), int(765 * InstanceSystem.SF), int(240 * InstanceSystem.SF), int(30 * InstanceSystem.SF)), 1)

            Font = pygame.font.SysFont("Bahnschrift", int(16 * InstanceSystem.SF))

            if InstanceVent.AltOpen is None and InstanceVent.AltClose is None and InstanceVent.VelClose is None:
                Text = Font.render("Vent Alt: None  |  Float Alt: None  |  Float Vel: None", True, Color)
            if InstanceVent.AltOpen is not None and InstanceVent.AltClose is None and InstanceVent.VelClose is None:
                if InstanceSystem.Metric:
                    Text = Font.render("Vent Alt: {:.0f} m  |  Float Alt: None  |  Float Vel: None".format(InstanceVent.AltOpen * 0.3048), True, Color)
                else:
                    Text = Font.render("Vent Alt: {:.0f} ft  |  Float Alt: None  |  Float Vel: None".format(InstanceVent.AltOpen), True, Color)
            if InstanceVent.AltOpen is None and InstanceVent.AltClose is not None and InstanceVent.VelClose is None:
                Text = Font.render("Vent Alt: None  |  Float Alt: {:.0f} ft  |  Float Vel: None".format(InstanceVent.AltClose), True, Color)
            if InstanceVent.AltOpen is None and InstanceVent.AltClose is None and InstanceVent.VelClose is not None:
                if InstanceSystem.Metric:
                    Text = Font.render("Vent Alt: None  |  Float Alt: None  |  Float Vel: {:.1f} m/s".format(InstanceVent.VelClose * 0.3048), True, Color)
                else:
                    Text = Font.render("Vent Alt: None  |  Float Alt: None  |  Float Vel: {:.1f} ft/s".format(InstanceVent.VelClose), True, Color)
            if InstanceVent.AltOpen is not None and InstanceVent.AltClose is not None and InstanceVent.VelClose is None:
                if InstanceSystem.Metric:
                    Text = Font.render("Vent Alt: {:.0f} m  |  Float Alt: {:.0f} m  |  Float Vel: None".format(InstanceVent.AltOpen * 0.3048, InstanceVent.AltClose * 0.3048), True, Color)
                else:
                    Text = Font.render("Vent Alt: {:.0f} ft  |  Float Alt: {:.0f} ft  |  Float Vel: None".format(InstanceVent.AltOpen, InstanceVent.AltClose), True, Color)
            if InstanceVent.AltOpen is None and InstanceVent.AltClose is not None and InstanceVent.VelClose is not None:
                if InstanceSystem.Metric:
                    Text = Font.render("Vent Alt: None  |  Float Alt: {:.0f} m |  Float Vel: {:.1f} m/s".format(InstanceVent.AltClose * 0.3048, InstanceVent.VelClose * 0.3048), True, Color)
                else:
                    Text = Font.render("Vent Alt: None  |  Float Alt: {:.0f} ft  |  Float Vel: {:.1f} ft/s".format(InstanceVent.AltClose, InstanceVent.VelClose), True, Color)
            if InstanceVent.AltOpen is not None and InstanceVent.AltClose is None and InstanceVent.VelClose is not None:
                if InstanceSystem.Metric:
                    Text = Font.render("Vent Alt: {:.0f} m  |  Float Alt: None  |  Float Vel: {:.1f} m/s".format(InstanceVent.AltOpen * 0.3048, InstanceVent.VelClose * 0.3048), True, Color)
                else:
                    Text = Font.render("Vent Alt: {:.0f} ft  |  Float Alt: None  |  Float Vel: {:.1f} ft/s".format(InstanceVent.AltOpen, InstanceVent.VelClose), True, Color)
            if InstanceVent.AltOpen is not None and InstanceVent.AltClose is not None and InstanceVent.VelClose is not None:
                if InstanceSystem.Metric:
                    Text = Font.render("Vent Alt: {:.0f} m  |  Float Alt: {:.0f} m  |  Float Vel: {:.1f} m/s".format(InstanceVent.AltOpen * 0.3048, InstanceVent.AltClose * 0.3048, InstanceVent.VelClose * 0.3048), True, Color)
                else:
                    Text = Font.render("Vent Alt: {:.0f} ft  |  Float Alt: {:.0f} ft  |  Float Vel: {:.1f} ft/s".format(InstanceVent.AltOpen, InstanceVent.AltClose, InstanceVent.VelClose), True, Color)

            TextRect = Text.get_rect()
            TextRect.center = (int(1060 * InstanceSystem.SF), int(820 * InstanceSystem.SF))

            InstanceSystem.Window.blit(Text, TextRect)

            # Connection Input
            Font = pygame.font.SysFont("Bahnschrift", int(30 * InstanceSystem.SF))
            Text = Font.render("CONNECTIONS", True, InstanceSystem.ColorWhite)
            TextRect = Text.get_rect(topright=(int(1560 * InstanceSystem.SF), int(265 * InstanceSystem.SF)))

            InstanceSystem.Window.blit(Text, (TextRect.left, TextRect.top))

            pygame.draw.rect(InstanceSystem.Window, InstanceSystem.ColorWhite, (int(1365 * InstanceSystem.SF), int(300 * InstanceSystem.SF), int(200 * InstanceSystem.SF), int(30 * InstanceSystem.SF)), int(1 * InstanceSystem.SF))

            Font = pygame.font.SysFont("Bahnschrift", int(16 * InstanceSystem.SF))
            Text = Font.render("IRIDIUM MODEM", True, InstanceSystem.ColorWhite)
            TextRect = Text.get_rect()
            TextRect.center = (int(1465 * InstanceSystem.SF), int(315 * InstanceSystem.SF))

            InstanceSystem.Window.blit(Text, TextRect)

            pygame.draw.rect(InstanceSystem.Window, InstanceSystem.ColorWhite, (int(1365 * InstanceSystem.SF), int(345 * InstanceSystem.SF), int(200 * InstanceSystem.SF), int(30 * InstanceSystem.SF)), int(1 * InstanceSystem.SF))

            Font = pygame.font.SysFont("Bahnschrift", int(16 * InstanceSystem.SF))
            Text = Font.render("APRS CALLSIGN", True, InstanceSystem.ColorWhite)
            TextRect = Text.get_rect()
            TextRect.center = (int(1465 * InstanceSystem.SF), int(360 * InstanceSystem.SF))

            InstanceSystem.Window.blit(Text, TextRect)

            pygame.draw.rect(InstanceSystem.Window, InstanceSystem.ColorWhite, (int(1365 * InstanceSystem.SF), int(390 * InstanceSystem.SF), int(200 * InstanceSystem.SF), int(30 * InstanceSystem.SF)), int(1 * InstanceSystem.SF))

            Font = pygame.font.SysFont("Bahnschrift", int(16 * InstanceSystem.SF))
            Text = Font.render("STREAM IP", True, InstanceSystem.ColorWhite)
            TextRect = Text.get_rect()
            TextRect.center = (int(1465 * InstanceSystem.SF), int(405 * InstanceSystem.SF))

            InstanceSystem.Window.blit(Text, TextRect)

            Font = pygame.font.SysFont("Bahnschrift", int(20 * InstanceSystem.SF))
            Text = Font.render("RFD Data", True, InstanceSystem.ColorWhite)
            TextRect = Text.get_rect()
            TextRect.center = (int(1470 * InstanceSystem.SF), int(450 * InstanceSystem.SF))

            InstanceSystem.Window.blit(Text, TextRect)

            # Guided Descent System
            Font = pygame.font.SysFont("Bahnschrift", int(30 * InstanceSystem.SF))
            Text = Font.render("GUIDED DESCENT", True, InstanceSystem.ColorWhite)
            TextRect = Text.get_rect(topleft=(int(845 * InstanceSystem.SF), int(265 * InstanceSystem.SF)))

            InstanceSystem.Window.blit(Text, (TextRect.left, TextRect.top))

            pygame.draw.rect(InstanceSystem.Window, InstanceSystem.ColorWhite, (int(845 * InstanceSystem.SF), int(300 * InstanceSystem.SF), int(115 * InstanceSystem.SF), int(30 * InstanceSystem.SF)), int(1 * InstanceSystem.SF))

            Font = pygame.font.SysFont("Bahnschrift", int(16 * InstanceSystem.SF))
            Text = Font.render("TARGET LAT", True, InstanceSystem.ColorWhite)
            TextRect = Text.get_rect()
            TextRect.center = (int(902.5 * InstanceSystem.SF), int(315 * InstanceSystem.SF))

            InstanceSystem.Window.blit(Text, TextRect)

            pygame.draw.rect(InstanceSystem.Window, InstanceSystem.ColorWhite, (int(970 * InstanceSystem.SF), int(300 * InstanceSystem.SF), int(115 * InstanceSystem.SF), int(30 * InstanceSystem.SF)), int(1 * InstanceSystem.SF))

            Font = pygame.font.SysFont("Bahnschrift", int(16 * InstanceSystem.SF))
            Text = Font.render("TARGET LON", True, InstanceSystem.ColorWhite)
            TextRect = Text.get_rect()
            TextRect.center = (int(1027.5 * InstanceSystem.SF), int(315 * InstanceSystem.SF))

            InstanceSystem.Window.blit(Text, TextRect)

            Font = pygame.font.SysFont("Bahnschrift", int(16 * InstanceSystem.SF))
            Text = Font.render("SAME AS TRACKER", True, InstanceSystem.ColorWhite)
            TextRect = Text.get_rect(topleft=(int(870 * InstanceSystem.SF), int(340 * InstanceSystem.SF)))

            InstanceSystem.Window.blit(Text, (TextRect.left, TextRect.top))

            pygame.draw.rect(InstanceSystem.Window, (InstanceSystem.ColorGreen if InstanceDescent.Automatic else InstanceSystem.ColorRed), (int(845 * InstanceSystem.SF), int(340 * InstanceSystem.SF), int(15 * InstanceSystem.SF), int(15 * InstanceSystem.SF)))
            pygame.draw.rect(InstanceSystem.Window, InstanceSystem.ColorWhite, (int(845 * InstanceSystem.SF), int(340 * InstanceSystem.SF), int(15 * InstanceSystem.SF), int(15 * InstanceSystem.SF)), int(1 * InstanceSystem.SF))

            # Serial Communication
            Font = pygame.font.SysFont("Bahnschrift", int(30 * InstanceSystem.SF))
            Text = Font.render("SERIAL COMMUNICATION", True, InstanceSystem.ColorWhite)
            TextRect = Text.get_rect(topleft=(int(845 * InstanceSystem.SF), int(380 * InstanceSystem.SF)))

            InstanceSystem.Window.blit(Text, (TextRect.left, TextRect.top))

            pygame.draw.rect(InstanceSystem.Window, InstanceSystem.ColorWhite, (int(845 * InstanceSystem.SF), int(415 * InstanceSystem.SF), int(115 * InstanceSystem.SF), int(30 * InstanceSystem.SF)), int(1 * InstanceSystem.SF))

            if InstanceSystem.AutoCOM:
                Color = (150, 150, 150, 0.2)
            else:
                Color = InstanceSystem.ColorWhite

            Font = pygame.font.SysFont("Bahnschrift", int(16 * InstanceSystem.SF))
            Text = Font.render("RFD COM", True, Color)
            TextRect = Text.get_rect()
            TextRect.center = (int(902.5 * InstanceSystem.SF), int(430 * InstanceSystem.SF))

            InstanceSystem.Window.blit(Text, TextRect)

            pygame.draw.rect(InstanceSystem.Window, InstanceSystem.ColorWhite, (int(970 * InstanceSystem.SF), int(415 * InstanceSystem.SF), int(115 * InstanceSystem.SF), int(30 * InstanceSystem.SF)), int(1 * InstanceSystem.SF))

            Font = pygame.font.SysFont("Bahnschrift", int(16 * InstanceSystem.SF))
            Text = Font.render("ARDUINO COM", True, Color)
            TextRect = Text.get_rect()
            TextRect.center = (int(1027.5 * InstanceSystem.SF), int(430 * InstanceSystem.SF))

            InstanceSystem.Window.blit(Text, TextRect)

            # Auto COM Button
            Font = pygame.font.SysFont("Bahnschrift", int(16 * InstanceSystem.SF))
            Text = Font.render("AUTO COM PORT DETECTION", True, InstanceSystem.ColorWhite)
            TextRect = Text.get_rect(topleft=(int(870 * InstanceSystem.SF), int(455 * InstanceSystem.SF)))

            InstanceSystem.Window.blit(Text, (TextRect.left, TextRect.top))

            pygame.draw.rect(InstanceSystem.Window, (InstanceSystem.ColorGreen if InstanceSystem.AutoCOM else InstanceSystem.ColorRed), (int(845 * InstanceSystem.SF), int(455 * InstanceSystem.SF), int(15 * InstanceSystem.SF), int(15 * InstanceSystem.SF)))
            pygame.draw.rect(InstanceSystem.Window, InstanceSystem.ColorWhite, (int(845 * InstanceSystem.SF), int(455 * InstanceSystem.SF), int(15 * InstanceSystem.SF), int(15 * InstanceSystem.SF)), int(1 * InstanceSystem.SF))

            # RFD Data Display
            Font = pygame.font.SysFont("Bahnschrift", int(12 * InstanceSystem.SF))

            TextX = int(1400 * InstanceSystem.SF)
            TextY = int(470 * InstanceSystem.SF)

            Labels = ['Packet', 'Siv', 'Fix', 'Lat', 'Lon', 'Alt', 'Year', 'Month', 'Day', 'Hour', 'Minute', 'Sec', 'NED - N',
                    'NED - E', 'NED - D', 'Battery', 'Battery (33)', 'Battery (51)', 'Battery (52)', 'A (Internal)',
                    'A (External)', 'Temperature', 'D (Internal)', 'D (External)', 'Pressure', 'Acceleration (x)',
                    'Acceleration (y)', 'Acceleration (z)', 'Pitch', 'Roll', 'Yaw']

            LabelW = max(Font.render(Label, True, InstanceSystem.ColorWhite).get_width() for Label in Labels)

            for i, Item in enumerate(zip(InstanceSystem.DataList[:-1], Labels)):
                Value, Label = Item

                LabelText = f"{Label}: "
                LabelSurface = Font.render(LabelText, True, InstanceSystem.ColorWhite)
                LabelRect = LabelSurface.get_rect(top=TextY, right=TextX + LabelW)
                InstanceSystem.Window.blit(LabelSurface, LabelRect)

                ValueText = str(Value)
                ValueSurface = Font.render(ValueText, True, InstanceSystem.ColorWhite)
                ValueRect = ValueSurface.get_rect(top=TextY, left=TextX + LabelW)
                InstanceSystem.Window.blit(ValueSurface, ValueRect)

                TextY += max(LabelRect.height, ValueRect.height)

            Font = pygame.font.SysFont("Bahnschrift", int(14 * InstanceSystem.SF))
            Text = Font.render("HERMES RELEASE VERSION 1.12 | PRODUCED AND TESTED BY NASA'S MINNESOTA SPACE GRANT CONSORTIUM (MnSGC) AT THE UNIVERSITY OF MINNESOTA TWIN CITIES", True, InstanceSystem.ColorWhite)
            TextRect = Text.get_rect()
            TextRect.center = (int(960 * InstanceSystem.SF), int(880 * InstanceSystem.SF))

            InstanceSystem.Window.blit(Text, TextRect)

InstanceSettings = ClassSettings()

class ClassPopup():
    def __init__(self):
        self.Tracker = False
        self.Venting = False
        self.Connections = False

    def Display(self):
        if not InstanceScreen.Fullscreen:
            if not InstanceSettings.Active:
                # Tracking Help
                InstanceSystem.Window.blit(InstanceSystem.HintOn, (int(380 * InstanceSystem.SF), int(500 * InstanceSystem.SF))) if self.Tracker else InstanceSystem.Window.blit(InstanceSystem.HintOff, (int(380 * InstanceSystem.SF), int(500 * InstanceSystem.SF)))
            
            if not InstanceSettings.Active:
                # Venting Help
                InstanceSystem.Window.blit(InstanceSystem.HintOn, (int(380 * InstanceSystem.SF), int(875 * InstanceSystem.SF))) if self.Venting else InstanceSystem.Window.blit(InstanceSystem.HintOff, (int(380 * InstanceSystem.SF), int(875 * InstanceSystem.SF)))

            if InstanceSettings.Active: 
                # Connections Help
                InstanceSystem.Window.blit(InstanceSystem.HintOn, (int(1312.5 * InstanceSystem.SF), int(252.5 * InstanceSystem.SF))) if self.Connections else InstanceSystem.Window.blit(InstanceSystem.HintOff, (int(1312.5 * InstanceSystem.SF), int(252.5 * InstanceSystem.SF)))

            if self.Tracker and not InstanceSettings.Active:
                pygame.draw.rect(InstanceSystem.Window, InstanceSystem.ColorGray, (440 * InstanceSystem.SF, 500 * InstanceSystem.SF, 300 * InstanceSystem.SF, 290 * InstanceSystem.SF))
                pygame.draw.rect(InstanceSystem.Window, (255, 255, 255, 1), (440 * InstanceSystem.SF, 500 * InstanceSystem.SF, 300 * InstanceSystem.SF, 290 * InstanceSystem.SF), int(1 * InstanceSystem.SF))
                    
                Font = pygame.font.SysFont("Bahnschrift", int(25 * InstanceSystem.SF))

                Text = Font.render("Tracking with HERMES", True, InstanceSystem.ColorWhite)
                TextRect = Text.get_rect(center=(590 * InstanceSystem.SF, 525 * InstanceSystem.SF))
                InstanceSystem.Window.blit(Text, TextRect)

                Font = pygame.font.SysFont("Bahnschrift", int(15 * InstanceSystem.SF))

                Text = Font.render("Orient the ground station dish north", True, InstanceSystem.ColorWhite)
                TextRect = Text.get_rect(left=465 * InstanceSystem.SF, top=560 * InstanceSystem.SF)
                InstanceSystem.Window.blit(Text, TextRect)

                Text = Font.render("and level with the ground", True, InstanceSystem.ColorWhite)
                TextRect = Text.get_rect(left=465 * InstanceSystem.SF, top=580 * InstanceSystem.SF)
                InstanceSystem.Window.blit(Text, TextRect)

                Text = Font.render("This can be done manually or with", True, InstanceSystem.ColorWhite)
                TextRect = Text.get_rect(left=465 * InstanceSystem.SF, top=620 * InstanceSystem.SF)
                InstanceSystem.Window.blit(Text, TextRect)

                Text = Font.render("tweak controls", True, InstanceSystem.ColorWhite)
                TextRect = Text.get_rect(left=465 * InstanceSystem.SF, top=640 * InstanceSystem.SF)
                InstanceSystem.Window.blit(Text, TextRect)

                Text = Font.render("Ensure the ground station is plugged", True, InstanceSystem.ColorWhite)
                TextRect = Text.get_rect(left=465 * InstanceSystem.SF, top=680 * InstanceSystem.SF)
                InstanceSystem.Window.blit(Text, TextRect)

                Text = Font.render("into the computer and Arduino is ON", True, InstanceSystem.ColorWhite)
                TextRect = Text.get_rect(left=465 * InstanceSystem.SF, top=700 * InstanceSystem.SF)
                InstanceSystem.Window.blit(Text, TextRect)

                Text = Font.render("Click the center of the D-Pad to begin", True, InstanceSystem.ColorWhite)
                TextRect = Text.get_rect(left=465 * InstanceSystem.SF, top=740 * InstanceSystem.SF)
                InstanceSystem.Window.blit(Text, TextRect)

                Text = Font.render("automatic tracking", True, InstanceSystem.ColorWhite)
                TextRect = Text.get_rect(left=465 * InstanceSystem.SF, top=760 * InstanceSystem.SF)
                InstanceSystem.Window.blit(Text, TextRect)
        
        if self.Venting and not InstanceSettings.Active:
                pygame.draw.rect(InstanceSystem.Window, InstanceSystem.ColorGray, (440 * InstanceSystem.SF, 875 * InstanceSystem.SF, 300 * InstanceSystem.SF, 200 * InstanceSystem.SF))
                pygame.draw.rect(InstanceSystem.Window, (255, 255, 255, 1), (440 * InstanceSystem.SF, 875 * InstanceSystem.SF, 300 * InstanceSystem.SF, 200 * InstanceSystem.SF), int(1 * InstanceSystem.SF))
                    
                Font = pygame.font.SysFont("Bahnschrift", int(25 * InstanceSystem.SF))

                Text = Font.render("Venting and Floating", True, InstanceSystem.ColorWhite)
                TextRect = Text.get_rect(center=(590 * InstanceSystem.SF, 900 * InstanceSystem.SF))
                InstanceSystem.Window.blit(Text, TextRect)

                Font = pygame.font.SysFont("Bahnschrift", int(15 * InstanceSystem.SF))

                Text = Font.render("HERMES can send open, close, and cut", True, InstanceSystem.ColorWhite)
                TextRect = Text.get_rect(left=465 * InstanceSystem.SF, top=935 * InstanceSystem.SF)
                InstanceSystem.Window.blit(Text, TextRect)

                Text = Font.render("commands directly to the Iridium unit", True, InstanceSystem.ColorWhite)
                TextRect = Text.get_rect(left=465 * InstanceSystem.SF, top=955 * InstanceSystem.SF)
                InstanceSystem.Window.blit(Text, TextRect)

                Text = Font.render("Be sure to monitor the ascent rate", True, InstanceSystem.ColorWhite)
                TextRect = Text.get_rect(left=465 * InstanceSystem.SF, top=995 * InstanceSystem.SF)
                InstanceSystem.Window.blit(Text, TextRect)

                Text = Font.render("while the vent is open", True, InstanceSystem.ColorWhite)
                TextRect = Text.get_rect(left=465 * InstanceSystem.SF, top=1015 * InstanceSystem.SF)
                InstanceSystem.Window.blit(Text, TextRect)

                Text = Font.render("See SETTINGS for automatic controls", True, InstanceSystem.ColorWhite)
                TextRect = Text.get_rect(left=465 * InstanceSystem.SF, top=1055 * InstanceSystem.SF)
                InstanceSystem.Window.blit(Text, TextRect)
        
        if self.Connections and InstanceSettings.Active:
            pygame.draw.rect(InstanceSystem.Window, InstanceSystem.ColorGray, (1000 * InstanceSystem.SF, 252.5 * InstanceSystem.SF, 300 * InstanceSystem.SF, 270 * InstanceSystem.SF))
            pygame.draw.rect(InstanceSystem.Window, (255, 255, 255, 1), (1000 * InstanceSystem.SF, 252.5 * InstanceSystem.SF, 300 * InstanceSystem.SF, 270 * InstanceSystem.SF), int(1 * InstanceSystem.SF))

            Font = pygame.font.SysFont("Bahnschrift", int(25 * InstanceSystem.SF))

            Text = Font.render("Accessing Radios", True, InstanceSystem.ColorWhite)
            TextRect = Text.get_rect(center=(1150 * InstanceSystem.SF, 277.5 * InstanceSystem.SF))
            InstanceSystem.Window.blit(Text, TextRect)

            Font = pygame.font.SysFont("Bahnschrift", int(15 * InstanceSystem.SF))

            Text = Font.render("Iridium and APRS are used for tracking", True, InstanceSystem.ColorWhite)
            TextRect = Text.get_rect(left=1025 * InstanceSystem.SF, top=312.5 * InstanceSystem.SF)
            InstanceSystem.Window.blit(Text, TextRect)

            Text = Font.render("The former expects a modem name;", True, InstanceSystem.ColorWhite)
            TextRect = Text.get_rect(left=1025 * InstanceSystem.SF, top=352.5 * InstanceSystem.SF)
            InstanceSystem.Window.blit(Text, TextRect)

            Text = Font.render("the latter expects a callsign", True, InstanceSystem.ColorWhite)
            TextRect = Text.get_rect(left=1025 * InstanceSystem.SF, top=372.5 * InstanceSystem.SF)
            InstanceSystem.Window.blit(Text, TextRect)

            Text = Font.render("RFD is likewise used for tracking, but", True, InstanceSystem.ColorWhite)
            TextRect = Text.get_rect(left=1025 * InstanceSystem.SF, top=412.5 * InstanceSystem.SF)
            InstanceSystem.Window.blit(Text, TextRect)

            Text = Font.render("it connects via serial", True, InstanceSystem.ColorWhite)
            TextRect = Text.get_rect(left=1025 * InstanceSystem.SF, top=432.5 * InstanceSystem.SF)
            InstanceSystem.Window.blit(Text, TextRect)

            Text = Font.render("Ubiquiti is the video streaming radio - ", True, InstanceSystem.ColorWhite)
            TextRect = Text.get_rect(left=1025 * InstanceSystem.SF, top=472.5 * InstanceSystem.SF)
            InstanceSystem.Window.blit(Text, TextRect)

            Text = Font.render("connect by entering the IP address", True, InstanceSystem.ColorWhite)
            TextRect = Text.get_rect(left=1025 * InstanceSystem.SF, top=492.5 * InstanceSystem.SF)
            InstanceSystem.Window.blit(Text, TextRect)

InstancePopup = ClassPopup()

class ClassInput:
    def Update(self):
        global InputRFD, InputIridium, InputAPRS, InputUbiquiti, InputArduino, InputCOMRFD, InputCOMArduino, InputText, InputTrackerLat, InputTrackerLon, InputTrackerAlt, InputPayloadLat, InputPayloadLon, InputPayloadAlt, InputTargetLat, InputTargetLon, InputAltOpen, InputAltClose, InputVelClose, InputIMEI, InputWindowW, InputWindowH

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                InstanceSystem.Shutdown()
            
            MouseX, MouseY = pygame.mouse.get_pos()
            MousePos = pygame.mouse.get_pos()

            # Tracking Popup Button
            Button = pygame.Rect(380 * InstanceSystem.SF, 500 * InstanceSystem.SF, 50 * InstanceSystem.SF, 50 * InstanceSystem.SF)
            if Button.collidepoint(MousePos) and not InstanceSettings.Active:
                InstancePopup.Tracker = True
            else:
                InstancePopup.Tracker = False
            
            # Venting Popup Bottom
            Button = pygame.Rect(380 * InstanceSystem.SF, 875 * InstanceSystem.SF, 50 * InstanceSystem.SF, 50 * InstanceSystem.SF)
            if Button.collidepoint(MousePos) and not InstanceSettings.Active:
                InstancePopup.Venting = True
            else:
                InstancePopup.Venting = False
            
            # Connections Popup Button
            Button = pygame.Rect(1312.5 * InstanceSystem.SF, 252.5 * InstanceSystem.SF, 50 * InstanceSystem.SF, 50 * InstanceSystem.SF)
            if Button.collidepoint(MousePos) and InstanceSettings.Active:
                InstancePopup.Connections = True
            else:
                InstancePopup.Connections = False
            
            # Radio Buttons
            Buttons = [
                pygame.Rect(int((i + 0.5) * InstanceRadio.S + InstanceRadio.X - 100 * InstanceSystem.SF), InstanceRadio.Y, InstanceRadio.W, InstanceRadio.H) 
                for i in range(5)
            ]

            for i, Button in enumerate(Buttons):
                if Button.collidepoint(MousePos) and not InstanceSettings.Active:
                    if i == 0:
                        InstanceRadio.Hovers[0] = True
                    elif i == 1:
                        InstanceRadio.Hovers[1] = True
                    elif i == 2:
                        InstanceRadio.Hovers[2] = True
                    elif i == 3:
                        InstanceRadio.Hovers[3] = True
                    elif i == 4:
                        InstanceRadio.Hovers[4] = True
                else:
                    if i == 0:
                        InstanceRadio.Hovers[0] = False
                    elif i == 1:
                        InstanceRadio.Hovers[1] = False
                    elif i == 2:
                        InstanceRadio.Hovers[2] = False
                    elif i == 3:
                        InstanceRadio.Hovers[3] = False
                    elif i == 4:
                        InstanceRadio.Hovers[4] = False
                    
                    InstanceOutput.Message = ''
            
            # Mouse Click
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pygame.mixer.music.load(InstanceSystem.Tap)
                pygame.mixer.music.play()

                # Power Button
                if (MouseX - InstanceButtons.PowerX) ** 2 + (MouseY - InstanceButtons.PowerY) ** 2 <= InstanceButtons.PowerR ** 2:
                    InstanceSystem.Shutdown()

                # Help Button
                if (MouseX - InstanceButtons.HelpX) ** 2 + (MouseY - InstanceButtons.HelpY) ** 2 <= InstanceButtons.HelpR ** 2:
                    URL = 'https://docs.google.com/document/d/1PRoLkXaMrUWXbg3vbNBbG_Q1igPCRx8imRnfndy7S-0/edit?usp=sharing'
                    webbrowser.open(URL)

                # Fullscreen Button
                if (MouseX - InstanceButtons.FullscreenX) ** 2 + (MouseY - InstanceButtons.FullscreenY) ** 2 <= InstanceButtons.FullscreenR ** 2:
                    if InstanceScreen.Fullscreen:
                        InstanceScreen.Fullscreen = False
                    else:
                        InstanceScreen.Fullscreen = True
                
                # Compass Button
                if (MouseX - InstanceCompass.X) ** 2 + (MouseY - InstanceCompass.Y) **2 <= int(4000 * InstanceSystem.SF):
                    if InstanceCompass.Setting < 2:
                        InstanceCompass.Setting += 1
                    else:
                        InstanceCompass.Setting = 1

                # Launch 1 Button
                Button = pygame.Rect(InstanceLaunch.X - InstanceLaunch.S - InstanceLaunch.W/2, InstanceLaunch.Y - InstanceLaunch.H/2, InstanceLaunch.W, InstanceLaunch.H)
                if Button.collidepoint(MousePos):
                    pygame.mixer.music.load(InstanceSystem.Switch)
                    pygame.mixer.music.play()
                    InstanceLaunch.Launch1 = True

                # Launch 2 Button
                Button = pygame.Rect(InstanceLaunch.X + InstanceLaunch.S - InstanceLaunch.W/2, InstanceLaunch.Y - InstanceLaunch.H/2, InstanceLaunch.W, InstanceLaunch.H)
                if Button.collidepoint(MousePos):
                    pygame.mixer.music.load(InstanceSystem.Switch)
                    pygame.mixer.music.play()
                    InstanceLaunch.Launch2 = True

                # Reset 1 Button
                Button = pygame.Rect(InstanceLaunch.ResetX, InstanceLaunch.ResetY + 35 * InstanceSystem.SF, InstanceLaunch.ResetW, InstanceLaunch.ResetH)
                if Button.collidepoint(MousePos):
                    pygame.mixer.music.load(InstanceSystem.Switch)
                    pygame.mixer.music.play()
                    InstanceLaunch.Reset1 = True

                # Reset 2 Button
                Button = pygame.Rect(InstanceLaunch.ResetX, InstanceLaunch.ResetY + 5 * InstanceSystem.SF, InstanceLaunch.ResetW, InstanceLaunch.ResetH)
                if Button.collidepoint(MousePos):
                    pygame.mixer.music.load(InstanceSystem.Switch)
                    pygame.mixer.music.play()
                    InstanceLaunch.Reset2 = True

                # Reset 3 Button
                Button = pygame.Rect(InstanceLaunch.ResetX, InstanceLaunch.ResetY - 25 * InstanceSystem.SF, InstanceLaunch.ResetW, InstanceLaunch.ResetH)
                if Button.collidepoint(MousePos):
                    pygame.mixer.music.load(InstanceSystem.Switch)
                    pygame.mixer.music.play()
                    InstanceLaunch.Reset3 = True

                # Reset 4 Button
                Button = pygame.Rect(InstanceLaunch.ResetX, InstanceLaunch.ResetY - 55 * InstanceSystem.SF, InstanceLaunch.ResetW, InstanceLaunch.ResetH)
                if Button.collidepoint(MousePos):
                    pygame.mixer.music.load(InstanceSystem.Switch)
                    pygame.mixer.music.play()
                    InstanceLaunch.Reset4 = True

                if InstanceLaunch.Reset1 and InstanceLaunch.Reset2 and InstanceLaunch.Reset3 and InstanceLaunch.Reset4:
                    Reset = [
                        (InstanceLaunch.ResetX, InstanceLaunch.ResetY - (-35) * InstanceSystem.SF),
                        (InstanceLaunch.ResetX, InstanceLaunch.ResetY - (-5) * InstanceSystem.SF),
                        (InstanceLaunch.ResetX, InstanceLaunch.ResetY - (25) * InstanceSystem.SF),
                        (InstanceLaunch.ResetX, InstanceLaunch.ResetY - (55) * InstanceSystem.SF)
                    ]

                    for i in range(4):
                        Color = (0, 200, 0, 0.8)
                        pygame.draw.rect(InstanceSystem.Window, Color, (*Reset[i], InstanceLaunch.ResetW, InstanceLaunch.ResetH))
                        Color = InstanceSystem.ColorWhite
                        pygame.draw.rect(InstanceSystem.Window, Color, (*Reset[i], InstanceLaunch.ResetW, InstanceLaunch.ResetH), int(1 * InstanceSystem.SF))

                    pygame.mixer.music.load(InstanceSystem.Switch)
                    pygame.mixer.music.play()
                    time.sleep(0.5)
                    pygame.mixer.music.load(InstanceSystem.Beep)
                    pygame.mixer.music.play()

                    InstanceOutput.Message = "Launch Timer Halted"
                    InstanceLaunch.Launch1 = False
                    InstanceLaunch.Launch2 = False
                    InstanceLaunch.Reset1 = False
                    InstanceLaunch.Reset2 = False
                    InstanceLaunch.Reset3 = False
                    InstanceLaunch.Reset4 = False

                # Countdown 1 Button
                Button = pygame.Rect(InstanceLaunch.CountdownX, InstanceLaunch.CountdownY, InstanceLaunch.CountdownW, InstanceLaunch.CountdownH)
                if Button.collidepoint(MousePos) and InstanceLaunch.Launched == False:
                    pygame.mixer.music.load(InstanceSystem.Switch)
                    pygame.mixer.music.play()
                    InstanceTime.Countdown2 = False
                    InstanceTime.Countdown3 = False
                    InstanceTime.Countdown1 = not InstanceTime.Countdown1

                # Countdown 2 Button
                Button = pygame.Rect(InstanceLaunch.CountdownX + 55 * InstanceSystem.SF, InstanceLaunch.CountdownY, InstanceLaunch.CountdownW, InstanceLaunch.CountdownH)
                if Button.collidepoint(MousePos) and InstanceLaunch.Launched == False:
                    pygame.mixer.music.load(InstanceSystem.Switch)
                    pygame.mixer.music.play()
                    InstanceTime.Countdown1 = False
                    InstanceTime.Countdown3 = False
                    InstanceTime.Countdown2 = not InstanceTime.Countdown2

                # Countdown 3 Button
                Button = pygame.Rect(InstanceLaunch.CountdownX + 110 * InstanceSystem.SF, InstanceLaunch.CountdownY, InstanceLaunch.CountdownW, InstanceLaunch.CountdownH)
                if Button.collidepoint(MousePos) and InstanceLaunch.Launched == False:
                    pygame.mixer.music.load(InstanceSystem.Switch)
                    pygame.mixer.music.play()
                    InstanceTime.Countdown1 = False
                    InstanceTime.Countdown2 = False
                    InstanceTime.Countdown3 = not InstanceTime.Countdown3

                # Radio Buttons
                Buttons = [
                    pygame.Rect(int((i + 0.5) * InstanceRadio.S + InstanceRadio.X - 100 * InstanceSystem.SF), InstanceRadio.Y, InstanceRadio.W, InstanceRadio.H) 
                    for i in range(5)
                ]

                Actions = [
                    (InstanceRFD.Conditional, InstanceRFD.Active, InstanceRFD.Setup, 'RFD Disconnected'),
                    (InstanceIridium.Conditional, InstanceIridium.Active, InstanceIridium.Setup, 'Iridium Disconnected'),
                    (InstanceAPRS.Conditional, InstanceAPRS.Active, InstanceAPRS.Setup, 'APRS Disconnected'),
                    (InstanceUbiquiti.Conditional, InstanceUbiquiti.Active, InstanceUbiquiti.Setup, 'Ubiquiti Disconnected'),
                    (InstanceArduino.Conditional, InstanceArduino.Active, InstanceArduino.Setup, 'Arduino Disconnected')
                ]

                for i, Button in enumerate(Buttons):
                    if Button.collidepoint(MousePos) and not InstanceSettings.Active:
                        pygame.mixer.music.load(InstanceSystem.Switch)
                        pygame.mixer.music.play()

                        Conditional, Connection, SetupFunction, Message = Actions[i]

                        if not Conditional and not Connection:
                            ButtonX = int((i + 0.5) * InstanceRadio.S + InstanceRadio.X - 100 * InstanceSystem.SF)
                            pygame.draw.rect(InstanceSystem.Window, (80, 0, 0, 0.8), (ButtonX, InstanceRadio.Y, InstanceRadio.W, InstanceRadio.H))
                            pygame.draw.rect(InstanceSystem.Window, InstanceSystem.ColorGray, (ButtonX, InstanceRadio.Y, InstanceRadio.W, InstanceRadio.H), int(3 * InstanceSystem.SF))

                            SetupFunction()
                        else:
                            if i == 0:
                                InstanceRFD.Close()
                            if i == 1:
                                InstanceIridium.Close()
                            if i == 2:
                                InstanceAPRS.Close()
                            if i == 3:
                                InstanceUbiquiti.Close()
                            if i == 4:
                                InstanceArduino.Close()
                                InstanceArduino.Tracking = False

                            InstanceRadio.Display()
                            InstanceOutput.Message = Message

                # Tracking Arrows
                Button = [
                    pygame.Rect(InstanceControls.X - 0.75 * InstanceControls.R, InstanceControls.Y - 2 * InstanceControls.TriangleHeight, 1.5 * InstanceControls.R, 2 * InstanceControls.TriangleHeight),
                    pygame.Rect(InstanceControls.X - 0.75 * InstanceControls.R, InstanceControls.Y + InstanceControls.TriangleHeight, 1.5 * InstanceControls.R, 2 * InstanceControls.TriangleHeight),
                    pygame.Rect(InstanceControls.X + InstanceControls.TriangleHeight, InstanceControls.Y - 0.75 * InstanceControls.R, 2 * InstanceControls.TriangleHeight, 1.5 * InstanceControls.R),
                    pygame.Rect(InstanceControls.X - 2 * InstanceControls.TriangleHeight, InstanceControls.Y - 0.75 * InstanceControls.R, 2 * InstanceControls.TriangleHeight, 1.5 * InstanceControls.R)
                ]

                for i, Polygon in enumerate(InstanceControls.TriangleShapes):
                    Polygon = [(int(X), int(Y)) for X, Y in Polygon]

                    if Button[i].collidepoint(pygame.mouse.get_pos()) and not (MouseX - InstanceControls.X) ** 2 + (MouseY - InstanceControls.Y) ** 2 <= InstanceControls.R ** 2 and not InstanceScreen.Fullscreen:
                        if i == 0:
                            InstanceSystem.Window.blit(InstanceSystem.DPadUp, (int(InstanceControls.X - 85 * InstanceSystem.SF), int(InstanceControls.Y - 85 * InstanceSystem.SF)))
                            if InstanceArduino.Active: InstanceCalculations.TweakTilt += 1
                        if i == 1:
                            InstanceSystem.Window.blit(InstanceSystem.DPadDown, (int(InstanceControls.X - 85 * InstanceSystem.SF), int(InstanceControls.Y - 85 * InstanceSystem.SF)))
                            if InstanceArduino.Active: InstanceCalculations.TweakTilt -= 1
                        if i == 2:
                            InstanceSystem.Window.blit(InstanceSystem.DPadRight, (int(InstanceControls.X - 85 * InstanceSystem.SF), int(InstanceControls.Y - 85 * InstanceSystem.SF)))
                            if InstanceArduino.Active: InstanceCalculations.TweakPan += 1
                        if i == 3:
                            InstanceSystem.Window.blit(InstanceSystem.DPadLeft, (int(InstanceControls.X - 85 * InstanceSystem.SF), int(InstanceControls.Y - 85 * InstanceSystem.SF)))
                            if InstanceArduino.Active: InstanceCalculations.TweakPan -= 1

                        pygame.draw.line(InstanceSystem.Window, InstanceSystem.ColorWhite, (InstanceControls.X - 20 * InstanceSystem.SF, InstanceControls.Y - 20 * InstanceSystem.SF), (InstanceControls.X - 70 * InstanceSystem.SF, InstanceControls.Y - 70 * InstanceSystem.SF))

                # Tracking Button
                if (MouseX - InstanceControls.X) ** 2 + (MouseY - InstanceControls.Y) ** 2 <= InstanceControls.R ** 2:
                    InstanceSystem.Window.blit(InstanceSystem.DPadCenter, (int(InstanceControls.X - 50 * InstanceSystem.SF), int(InstanceControls.Y - 50 * InstanceSystem.SF)))
                    pygame.draw.line(InstanceSystem.Window, InstanceSystem.ColorWhite, (InstanceControls.X - 20 * InstanceSystem.SF, InstanceControls.Y - 20 * InstanceSystem.SF), (InstanceControls.X - 70 * InstanceSystem.SF, InstanceControls.Y - 70 * InstanceSystem.SF))

                    if not InstanceArduino.Tracking and InstanceArduino.Active:
                        InstanceOutput.Message = 'Tracking Commencing'
                        InstanceArduino.Tracking = True
                    elif InstanceArduino.Tracking and InstanceArduino.Active:
                        InstanceOutput.Message = 'Tracking Terminating'
                        InstanceArduino.Tracking = False
                
                # Clear Buttons
                Button = pygame.Rect(150 * InstanceSystem.SF, 1030 * InstanceSystem.SF, 95 * InstanceSystem.SF, 30 * InstanceSystem.SF)
                if Button.collidepoint(MousePos):
                    InstanceRFD.Lat = 0
                    InstanceRFD.Lon = 0
                    InstanceRFD.Alt = 0

                    InstanceIridium.Lat = 0
                    InstanceIridium.Lon = 0
                    InstanceIridium.Alt = 0

                    InstanceAPRS.Lat = 0
                    InstanceAPRS.Lon = 0
                    InstanceAPRS.Alt = 0

                    InstancePayload.Lat = 0
                    InstancePayload.Lon = 0
                    InstancePayload.Alt = 0

                    if InstanceSystem.Metric:
                        self.Position = "0.00°N, 0.00°E | 0 m"
                    else:
                        self.Position = "0.00°N, 0.00°E | 0 ft"
                    
                    self.Location = "Location Not Set"

                Button = pygame.Rect(255 * InstanceSystem.SF, 1030 * InstanceSystem.SF, 95 * InstanceSystem.SF, 30 * InstanceSystem.SF)
                if Button.collidepoint(MousePos):
                    InstanceCalculations.TweakPan = 0
                    InstanceCalculations.TweakTilt = 0

                # Vent Guard
                Button = pygame.Rect(InstanceVent.X, InstanceVent.Y - 5 * InstanceSystem.SF, 205 * InstanceSystem.SF, 40 * InstanceSystem.SF)

                if Button.collidepoint(MousePos) and InstanceVent.Guard:
                    pygame.mixer.music.load(InstanceSystem.Switch)
                    pygame.mixer.music.play()

                    InstanceVent.Guard = False

                    break
                
                Button = pygame.Rect(InstanceVent.X, InstanceVent.Y + 40 * InstanceSystem.SF, 205 * InstanceSystem.SF, 40 * InstanceSystem.SF)

                if Button.collidepoint(MousePos) and not InstanceVent.Guard:
                    pygame.mixer.music.load(InstanceSystem.Switch)
                    pygame.mixer.music.play()

                    InstanceVent.Guard = True

                    break

                # Vent Button
                Button = pygame.Rect(InstanceVent.X, InstanceVent.Y, InstanceVent.W, InstanceVent.H)

                if Button.collidepoint(MousePos) and not InstanceVent.Guard:
                    pygame.mixer.music.load(InstanceSystem.Switch)
                    pygame.mixer.music.play()

                    if not InstanceVent.Vented:
                        InstanceVent.Open()
                        break

                    if InstanceVent.Vented:
                        InstanceVent.Close()
                        break

                # Cut Button
                Button = pygame.Rect(InstanceVent.X + 105 * InstanceSystem.SF, InstanceVent.Y, InstanceVent.W, InstanceVent.H)

                if Button.collidepoint(MousePos) and not InstanceVent.Guard:
                    pygame.mixer.music.load(InstanceSystem.Switch)
                    pygame.mixer.music.play()

                    InstanceVent.Cutdown()
                
                # IMEI Input
                Button = pygame.Rect(150 * InstanceSystem.SF, 980 * InstanceSystem.SF, 205 * InstanceSystem.SF, 40 * InstanceSystem.SF)

                if Button.collidepoint(MousePos) and InstanceVent.Guard:
                    InputIMEI = True

                # Settings Button
                if (MouseX - InstanceButtons.SettingsX) ** 2 + (MouseY - InstanceButtons.SettingsY) ** 2 <= InstanceButtons.SettingsR ** 2:
                    if InstanceSettings.Active == False:
                        InstanceSettings.Active = True

                        InputIMEI = False
                    else:
                        InstanceSettings.Active = False

                        InputPayloadLat = False
                        InputPayloadLon = False
                        InputPayloadAlt = False

                        InputTrackerLat = False
                        InputTrackerLon = False
                        InputTrackerAlt = False

                        InputRFD = False
                        InputIridium = False
                        InputAPRS = False
                        InputUbiquiti = False
                        InputArduino = False

                        InputCOMRFD = False
                        InputCOMArduino = False

                # Settings Menu
                if InstanceSettings.Active:
                    Peripherals = [
                        (pygame.Rect(int(360 * InstanceSystem.SF), int(420 * InstanceSystem.SF), int(20 * InstanceSystem.SF), int(20 * InstanceSystem.SF)), 'InstanceAltitude'),
                        (pygame.Rect(int(360 * InstanceSystem.SF), int(460 * InstanceSystem.SF), int(20 * InstanceSystem.SF), int(20 * InstanceSystem.SF)), 'InstanceLocation'),
                        (pygame.Rect(int(360 * InstanceSystem.SF), int(500 * InstanceSystem.SF), int(20 * InstanceSystem.SF), int(20 * InstanceSystem.SF)), 'InstanceCompass'),
                        (pygame.Rect(int(360 * InstanceSystem.SF), int(540 * InstanceSystem.SF), int(20 * InstanceSystem.SF), int(20 * InstanceSystem.SF)), 'InstanceTime')
                    ]

                    def Toggle(Instance):
                        for Button, _ in Peripherals:
                            if Button.collidepoint(MousePos):
                                Instance.Enabled = not Instance.Enabled
                    
                    Toggle(InstanceAltitude)
                    Toggle(InstanceLocation)
                    Toggle(InstanceCompass)
                    Toggle(InstanceTime)

                    # Manual Tracking
                    if ((MousePos[0] - int(375 * InstanceSystem.SF))**2 + (MousePos[1] - int(675 * InstanceSystem.SF))**2) <= (int(15 * InstanceSystem.SF)**2):
                        InstanceSystem.Manual = not InstanceSystem.Manual

                    # Manual Venting
                    if ((MousePos[0] - int(865 * InstanceSystem.SF))**2 + (MousePos[1] - int(675 * InstanceSystem.SF))**2) <= (int(15 * InstanceSystem.SF)**2):
                        InstanceVent.Manual = not InstanceVent.Manual
                    
                    # Auto COM Detection
                    Button = pygame.Rect(int(845 * InstanceSystem.SF), int(455 * InstanceSystem.SF), int(15 * InstanceSystem.SF), int(15 * InstanceSystem.SF))
                    if Button.collidepoint(MousePos):
                        InstanceSystem.AutoCOM = not InstanceSystem.AutoCOM
                    
                    # Metric Units
                    if ((MousePos[0] - int(860 * InstanceSystem.SF))**2 + (MousePos[1] - int(575 * InstanceSystem.SF))**2) <= (int(15 * InstanceSystem.SF)**2):
                        InstanceSystem.Metric = not InstanceSystem.Metric
                    
                    # Guided Descent
                    Button = pygame.Rect(int(845 * InstanceSystem.SF), int(340 * InstanceSystem.SF), int(15 * InstanceSystem.SF), int(15 * InstanceSystem.SF))
                    if Button.collidepoint(MousePos):
                        InstanceDescent.Automatic = not InstanceDescent.Automatic

                    Fields = [
                        (pygame.Rect(int(360 * InstanceSystem.SF), int(300 * InstanceSystem.SF), int(120 * InstanceSystem.SF), int(30 * InstanceSystem.SF)), 'InputWindowW'),
                        (pygame.Rect(int(490 * InstanceSystem.SF), int(300 * InstanceSystem.SF), int(120 * InstanceSystem.SF), int(30 * InstanceSystem.SF)), 'InputWindowH'),
                        (pygame.Rect(int(360 * InstanceSystem.SF), int(710 * InstanceSystem.SF), int(120 * InstanceSystem.SF), int(30 * InstanceSystem.SF)), 'InputPayloadLat'),
                        (pygame.Rect(int(490 * InstanceSystem.SF), int(710 * InstanceSystem.SF), int(120 * InstanceSystem.SF), int(30 * InstanceSystem.SF)), 'InputPayloadLon'),
                        (pygame.Rect(int(620 * InstanceSystem.SF), int(710 * InstanceSystem.SF), int(120 * InstanceSystem.SF), int(30 * InstanceSystem.SF)), 'InputPayloadAlt'),
                        (pygame.Rect(int(360 * InstanceSystem.SF), int(765 * InstanceSystem.SF), int(120 * InstanceSystem.SF), int(30 * InstanceSystem.SF)), 'InputTrackerLat'),
                        (pygame.Rect(int(490 * InstanceSystem.SF), int(765 * InstanceSystem.SF), int(120 * InstanceSystem.SF), int(30 * InstanceSystem.SF)), 'InputTrackerLon'),
                        (pygame.Rect(int(620 * InstanceSystem.SF), int(765 * InstanceSystem.SF), int(120 * InstanceSystem.SF), int(30 * InstanceSystem.SF)), 'InputTrackerAlt'),
                        (pygame.Rect(int(1365 * InstanceSystem.SF), int(300 * InstanceSystem.SF), int(200 * InstanceSystem.SF), int(30 * InstanceSystem.SF)), 'InputIridium'),
                        (pygame.Rect(int(1365 * InstanceSystem.SF), int(345 * InstanceSystem.SF), int(200 * InstanceSystem.SF), int(30 * InstanceSystem.SF)), 'InputAPRS'),
                        (pygame.Rect(int(1365 * InstanceSystem.SF), int(390 * InstanceSystem.SF), int(200 * InstanceSystem.SF), int(30 * InstanceSystem.SF)), 'InputUbiquiti'),
                        (pygame.Rect(int(1030 * InstanceSystem.SF), int(710 * InstanceSystem.SF), int(240 * InstanceSystem.SF), int(30 * InstanceSystem.SF)), 'InputAltOpen'),
                        (pygame.Rect(int(1030 * InstanceSystem.SF), int(765 * InstanceSystem.SF), int(240 * InstanceSystem.SF), int(30 * InstanceSystem.SF)), 'InputAltClose'),
                        (pygame.Rect(int(940 * InstanceSystem.SF), int(765 * InstanceSystem.SF), int(40 * InstanceSystem.SF), int(30 * InstanceSystem.SF)), 'InputVelClose'),
                        (pygame.Rect(int(150 * InstanceSystem.SF), int(980 * InstanceSystem.SF), int(205 * InstanceSystem.SF), int(40 * InstanceSystem.SF)), 'InputIMEI'),
                        (pygame.Rect(int(845 * InstanceSystem.SF), int(415 * InstanceSystem.SF), int(115 * InstanceSystem.SF), int(30 * InstanceSystem.SF)), 'InputCOMRFD'),
                        (pygame.Rect(int(970 * InstanceSystem.SF), int(415 * InstanceSystem.SF), int(115 * InstanceSystem.SF), int(30 * InstanceSystem.SF)), 'InputCOMArduino')
                    ]

                    for Field, Flag in Fields:
                        if Field.collidepoint(MousePos):
                            if 'InputPayload' in Flag and InstanceSystem.Manual:
                                globals()[Flag] = True
                            if 'Vent' in Flag and not InstanceVent.Manual:
                                globals()[Flag] = True
                            if 'InputCOM' in Flag and not InstanceSystem.AutoCOM:
                                globals()[Flag] = True
                            if not 'Payload' in Flag and not 'Vent' in Flag and not 'InputCOM' in Flag:
                                globals()[Flag] = True
                            
                            if 'InputIMEI' in Flag:
                                print("Hit")

            if event.type == pygame.KEYDOWN:
                if keyboard.is_pressed('w') and InstanceArduino.Active:
                    InstanceCalculations.TweakTilt += 1
                if keyboard.is_pressed('a') and InstanceArduino.Active:
                    InstanceCalculations.TweakPan -= 1
                if keyboard.is_pressed('s') and InstanceArduino.Active:
                    InstanceCalculations.TweakTilt -= 1
                if keyboard.is_pressed('d') and InstanceArduino.Active:
                    InstanceCalculations.TweakPan += 1

                if InputPayloadLat or InputPayloadLon or InputPayloadAlt or InputTrackerLat or InputTrackerLon or InputTrackerAlt or InputAltOpen or InputAltClose or InputVelClose or InputIMEI or InputWindowW or InputWindowH or InputRFD or InputIridium or InputAPRS or InputUbiquiti or InputArduino or InputCOMRFD or InputCOMArduino:
                    if event.key == pygame.K_ESCAPE:
                        InputWindowW = False
                        InputWindowH = False
                        InputPayloadLat = False
                        InputPayloadLon = False
                        InputPayloadAlt = False
                        InputTrackerLat = False
                        InputTrackerLon = False
                        InputTrackerAlt = False
                        InputAltOpen = False
                        InputAltClose = False
                        InputVelClose = False
                        InputIMEI = False
                        InputRFD = False
                        InputIridium = False
                        InputAPRS = False
                        InputUbiquiti = False
                        InputArduino = False
                        InputCOMRFD = False
                        InputCOMArduino = False

                        InputText = ""
                    elif event.key == pygame.K_RETURN:
                        try:
                            if InputWindowW:
                                if float(InputText) <= 1920 and float(InputText) >= 512:
                                    InstanceSystem.W = float(InputText)
                                    InstanceSystem.H = InstanceSystem.W * (9/16)
                                    InstanceSystem.SF = min(InstanceSystem.W / 1920, InstanceSystem.H / 1080)
                                    InputWindowW = False
                            
                            if InputWindowH:
                                if float(InputText) <= 1080 and float(InputText) >= 288:
                                    InstanceSystem.H = float(InputText)
                                    InstanceSystem.W = InstanceSystem.H * (16/9)
                                    InstanceSystem.SF = min(InstanceSystem.W / 1920, InstanceSystem.H / 1080)
                                    InputWindowH = False
                            
                            if InputPayloadLat:
                                InstancePayload.Lat = float(InputText)
                                InputPayloadLat = False
                            
                            if InputPayloadLon:
                                InstancePayload.Lon = float(InputText)
                                InputPayloadLon = False
                            
                            if InputPayloadAlt:
                                if InstanceSystem.Metric:
                                    InstancePayload.Alt = float(InputText) * 3.28084
                                else:
                                    InstancePayload.Alt = float(InputText)
                                InputPayloadAlt = False
                            
                            if InputTrackerLat:
                                InstanceTracker.Lat = float(InputText)
                                InputTrackerLat = False
                            
                            if InputTrackerLon:
                                InstanceTracker.Lon = float(InputText)
                                InputTrackerLon = False
                            
                            if InputTrackerAlt:
                                if InstanceSystem.Metric:
                                    InstanceTracker.Alt = float(InputText) * 3.28084
                                else:
                                    InstanceTracker.Alt = float(InputText)
                                InputTrackerAlt = False
                            
                            if InputAltOpen:
                                if InstanceSystem.Metric:
                                    InstanceVent.AltOpen = float(InputText) * 3.28084
                                else:
                                    InstanceVent.AltOpen = float(InputText)
                                InputAltOpen = False
                            
                            if InputAltClose:
                                InstanceVent.VelClose = None
                                if InstanceSystem.Metric:
                                    InstanceVent.AltClose = float(InputText) * 3.28084
                                else:
                                    InstanceVent.AltClose = float(InputText)
                                InputAltClose = False
                            
                            if InputVelClose:
                                InstanceVent.AltClose = None
                                if InstanceSystem.Metric:
                                    InstanceVent.VelClose = float(InputText) * 3.28084
                                else:
                                    InstanceVent.VelClose = float(InputText)
                                InputVelClose = False
                            
                            if InputIMEI:
                                InstanceIridium.IMEI = str(InputText)
                                InputIMEI = False
                            
                            if InputIridium:
                                InstanceIridium.Modem = str(InputText)
                                InputIridium = False
                            
                            if InputAPRS:
                                InstanceAPRS.Callsign = str(InputText)
                                InputAPRS = False
                            
                            if InputUbiquiti:
                                InstanceUbiquiti.IP = str(InputText)
                                InputUbiquiti = False
                            
                            if InputCOMRFD:
                                InstanceRFD.COMPort = str(InputText)
                                InputCOMRFD = False
                            
                            if InputCOMArduino:
                                InstanceArduino.COMPort = str(InputText)
                                InputCOMArduino = False

                            InputText = ""
                        except ValueError:
                            pass
                    elif event.key == pygame.K_BACKSPACE:
                        InputText = InputText[:-1]
                    elif event.key == pygame.K_v and pygame.key.get_mods() & pygame.KMOD_CTRL:
                        Clipboard = clipboard.paste()
                        Inputs = [InputWindowW, InputWindowH, InputPayloadLat, InputPayloadLon, InputPayloadAlt, InputTrackerLat, InputTrackerLon, InputTrackerAlt, InputAltOpen, InputAltClose, InputVelClose, InputIMEI, InputIridium, InputAPRS, InputUbiquiti, InputCOMRFD, InputCOMArduino]

                        while '\0' in Clipboard:
                            Clipboard = Clipboard.replace('\0', '')

                        for Condition in Inputs:
                            if Condition:
                                InputText += Clipboard
                                break
                        else:
                            InputText += event.unicode.replace('\0', '')
                    else:
                        InputText += event.unicode.replace('\0', '')

            try:
                # Joystick Handling
                if event.type == pygame.JOYDEVICEADDED:
                    try:
                        if pygame.joystick.get_count() > 0:
                            joystick = pygame.joystick.Joystick(0)
                            joystick.init()
                    except pygame.error:
                        InstanceOutput.Message = 'Controller Error'

                if event.type == pygame.JOYAXISMOTION:
                    if event.axis == JoystickX:
                        if event.value < -0.5:
                            InstanceCalculations.TweakPan -= 1
                        elif event.value > 0.5:
                            InstanceCalculations.TweakPan += 1
                    elif event.axis == JoystickY:
                        if event.value < -0.5:
                            InstanceCalculations.TweakTilt += 1
                        elif event.value > 0.5:
                            InstanceCalculations.TweakTilt -= 1
            except KeyError as e:
                if str(e) != '5':
                    raise

        Inputs = [
            (InputWindowW, (360, 300), (120, 30)),
            (InputWindowH, (490, 300), (120, 30)),
            (InputPayloadLat, (360, 710), (120, 30)),
            (InputPayloadLon, (490, 710), (120, 30)),
            (InputPayloadAlt, (620, 710), (120, 30)),
            (InputTrackerLat, (360, 765), (120, 30)),
            (InputTrackerLon, (490, 765), (120, 30)),
            (InputTrackerAlt, (620, 765), (120, 30)),
            (InputIMEI, (150, 980), (205, 40)),
            (InputIridium, (1365, 300), (200, 30)),
            (InputAPRS, (1365, 345), (200, 30)),
            (InputUbiquiti, (1365, 390), (200, 30)),
            (InputAltOpen, (1030, 710), (240, 30)),
            (InputAltClose, (1030, 765), (240, 30)),
            (InputVelClose, (940, 765), (40, 30)),
            (InputCOMRFD, (845, 415), (115, 30)),
            (InputCOMArduino, (970, 415), (115, 30))
        ]

        for Condition, Pos, Size in Inputs:
            if Condition:
                pygame.draw.rect(InstanceSystem.Window, InstanceSystem.ColorBlack, (int(Pos[0] * InstanceSystem.SF), int(Pos[1] * InstanceSystem.SF), int(Size[0] * InstanceSystem.SF), int(Size[1] * InstanceSystem.SF)))
                pygame.draw.rect(InstanceSystem.Window, (InstanceSystem.ColorGreen if Condition else InstanceSystem.ColorRed), (int(Pos[0] * InstanceSystem.SF), int(Pos[1] * InstanceSystem.SF), int(Size[0] * InstanceSystem.SF), int(Size[1] * InstanceSystem.SF)), int(2 * InstanceSystem.SF))

                Font = pygame.font.SysFont("Bahnschrift", int(20 * InstanceSystem.SF))
                InputTextLim = ''

                if len(InputText) > 8 and (InputTrackerLat or InputTrackerLon or InputTrackerAlt or InputPayloadLat or InputPayloadLon or InputPayloadAlt):
                    InputTextLim = InputText[:8] + "..."

                InputSurface = Font.render(InputTextLim if InputTextLim else InputText, True, InstanceSystem.ColorWhite)
                InputRect = InputSurface.get_rect()

                if InputIMEI:
                    InputRect.topleft = InputRect.topleft = (int((Pos[0] + 30) * InstanceSystem.SF), int((Pos[1] + 10) * InstanceSystem.SF))
                else:
                    InputRect.topleft = (int((Pos[0] + 5) * InstanceSystem.SF), int((Pos[1] + 5) * InstanceSystem.SF))
                
                InstanceSystem.Window.blit(InputSurface, InputRect)

                if InputText == '':
                    Prompt = ''
                    Font = pygame.font.SysFont("Bahnschrift", int(16 * InstanceSystem.SF))

                    if Pos == (1365, 300):
                        Prompt = "ex: UOM002"
                    elif Pos == (1365, 345):
                        Prompt = "ex: KD0AWK-3"
                    elif Pos == (1365, 390):
                        Prompt = "ex: 192.168.2.101"
                    elif Pos == (845, 415):
                        Prompt = "ex: COM3"
                    elif Pos == (970, 415):
                        Prompt = "ex: COM6"
                    elif Pos == (150, 980):
                        Prompt = "ex: 123456789012345"

                    if Prompt:
                        if InputIMEI:
                            InputSurface = Font.render(Prompt, True, (100, 100, 100, 0.8))
                            InputRect = InputSurface.get_rect()
                            InputRect.topleft = (int((Pos[0] if Pos[0] == 1365 else Pos[0] + 30) * InstanceSystem.SF), int((Pos[1] + 12.5) * InstanceSystem.SF))
                        else:
                            InputSurface = Font.render(Prompt, True, (100, 100, 100, 0.8))
                            InputRect = InputSurface.get_rect()
                            InputRect.topleft = (int((Pos[0] + 25 if Pos[0] == 1365 else Pos[0] + 45) * InstanceSystem.SF), int((Pos[1] + 7.5) * InstanceSystem.SF))

                        InstanceSystem.Window.blit(InputSurface, InputRect)

InstanceInput = ClassInput()

def Cleanup():
    InstanceSystem.Shutdown()

atexit.register(Cleanup)

InstanceSystem.Startup()

while InstanceSystem.Running:
    # Handle Quit Events
    for event in pygame.event.get():
        if event.type == QUIT:
            InstanceSystem.Shutdown()

    # Initialize Joystick
    if pygame.joystick.get_count() > 0:
        joystick = pygame.joystick.Joystick(0)
        joystick.init()
        JoystickX, JoystickY = 0, 1

    # Clear InstanceSystem.Window
    InstanceSystem.Window.fill(InstanceSystem.ColorBlack)

    #Initialize Threads
    ThreadRFD = threading.Thread(target=InstanceRFD.Update)
    ThreadIridium = threading.Thread(target=InstanceIridium.Update)
    ThreadAPRS = threading.Thread(target=InstanceAPRS.Update)
    ThreadUbiquiti = threading.Thread(target=InstanceUbiquiti.Update)
    ThreadArduino = threading.Thread(target=InstanceArduino.Update)
    ThreadCalculations = threading.Thread(target=InstanceCalculations.Update)
    ThreadLogger = threading.Thread(target=InstanceLogger.Update)

    # Start Threads
    ThreadRFD.start()
    ThreadIridium.start()
    ThreadAPRS.start()
    ThreadUbiquiti.start()
    ThreadArduino.start()
    ThreadCalculations.start()
    ThreadLogger.start()

    # Join Threads
    ThreadRFD.join()
    ThreadIridium.join()
    ThreadAPRS.join()
    ThreadUbiquiti.join()
    ThreadArduino.join()
    ThreadCalculations.join()

    InstanceTitle.Display()
    InstanceScreen.Display()

    InstanceAltitude.Display()
    InstanceLocation.Display()
    InstanceCompass.Display()
    InstanceTime.Display()

    InstanceRadio.Display()
    InstanceOutput.Display()
    InstanceControls.Display()
    InstanceLaunch.Display()
    InstanceVent.Display()

    InstanceIndicators.Display()
    InstanceButtons.Display()
    InstanceSettings.Display()
    InstancePopup.Display()
    InstanceInput.Update()

    # Window Background
    pygame.draw.rect(InstanceSystem.Window, InstanceSystem.ColorWhite, (0, 0, InstanceSystem.W, InstanceSystem.H), int(3 * InstanceSystem.SF))

    # Refresh Display
    pygame.display.update()

    # Loop Frequency
    InstanceSystem.Clock.tick(30)

# Close GUI
InstanceSystem.Shutdown()