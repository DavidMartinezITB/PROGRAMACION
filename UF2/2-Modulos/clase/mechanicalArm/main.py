import actions

def main():
    actions.toggle()
    actions.updateAltitude(3)
    actions.updateAngle(180)
    actions.updateAltitude(-3)
    actions.updateAngle(-180)
    actions.updateAltitude(3)
    actions.toggle()

if __name__ == "__main__":
    main()