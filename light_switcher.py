#!/usr/bin/python3.4
if __name__ == '__main__':
	import RPi.GPIO as GPIO
	import argparse

	TURN_ON = '1'
	TURN_OFF = '0'
	PIN_HEAT = 32
	PIN_LIGHT = 36

	parser = argparse.ArgumentParser()
	parser.add_argument("heat")
	parser.add_argument("light")
	args = parser.parse_args()

	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(PIN_HEAT, GPIO.OUT)
	GPIO.setup(PIN_LIGHT, GPIO.OUT)

	if args.heat == TURN_ON:
		GPIO.output(PIN_HEAT, 1)
		print("Heat ON")
	elif args.heat == TURN_OFF:
		GPIO.output(PIN_HEAT, 0)
		print("Heat OFF")

	if args.light == TURN_ON:
		GPIO.output(PIN_LIGHT, 1)
		print("Light ON")
	elif args.light == TURN_OFF:
		GPIO.output(PIN_LIGHT, 0)
		print("Light OFF")
