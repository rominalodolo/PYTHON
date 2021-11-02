extends Node

const CAR = preload("res://car/car.tscn")

func _on_Timer_timeout():
	var car = CAR.instance()
	car.position = $"CarStart1".position
	add_child(car)
