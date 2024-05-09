status = {
    "openAngle": 0.0,
    "altitude": 0.0,
    "turnedOn": False
}

def getStatus():
    return 'MechanicalArm{{openAngle={}, altitude={}, turnedOn={}}}'.format(
        status['openAngle'],
        status['altitude'],
        status['turnedOn']
    )

def isTurnedOn():
    return status['turnedOn']

def isValidAngle(angle):
    return angle >= 0 and angle <= 360

def getResultantAngle(angle):
    return status['openAngle'] + angle

def isValidAltitude(altitude):
    return altitude >= 0

def getResultantAltitude(altitude):
    return status['altitude'] + altitude