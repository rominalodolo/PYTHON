extends Node

const CAR = preload("res://car/car.tscn")


func car_spawn():	
	var car = CAR.instance()
	car.position = $"StartPositions/CarStart1".position
	add_child(car)	


func _on_Timer1_timeout():
	car_spawn()

func _on_Timer2_timeout():
	pass # Replace with function body.

func _on_Timer3_timeout():
	pass # Replace with function body.

func _on_Timer4_timeout():
	pass # Replace with function body.

func _on_Timer5_timeout():
	pass # Replace with function body.
