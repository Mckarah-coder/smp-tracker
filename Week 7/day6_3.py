def predict_delivery_risk(crew_size, days_remaining, tasks_left):
    efficiency = tasks_left / (crew_size * days_remaining)

    if efficiency > 1.5:
        return "High risk"
    elif efficiency > 0.8:
        return "Medium risk"
    else:
        return "Low risk"


print(predict_delivery_risk(3, 5, 25))
print(predict_delivery_risk(4, 10, 18))
print(predict_delivery_risk(2, 4, 8))