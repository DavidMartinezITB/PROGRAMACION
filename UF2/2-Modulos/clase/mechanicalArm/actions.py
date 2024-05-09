import status

def toggle():
    status.status['turnedOn'] = not status.status['turnedOn']
    print(status.getStatus())

def updateAngle(angle):
    res = float(status.getResultantAngle(angle))
    if status.isValidAngle(res):
        status.status['openAngle'] = res
        print(status.getStatus())
    else:
        print('Not a valid angle!')

def updateAltitude(altitude):
    res = float(status.getResultantAltitude(altitude))
    if status.isValidAltitude(res):
        status.status['altitude'] = res
        print(status.getStatus())
    else:
        print('Not a valid altitude')