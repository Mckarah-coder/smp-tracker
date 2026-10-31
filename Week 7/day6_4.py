def simp_alert(money_spent, texts_sent, texts_replied, dates_asked, dates_replied):
    reply_rate = texts_replied / texts_sent
    date_rate = dates_replied / dates_asked
    score = (reply_rate + date_rate) / 2

    if score >= 0.5:
        return "She likes you"
    elif score >= 0.2:
        return "Lukewarm"
    else:
        return "You are simping"

print(simp_alert(45000, 80, 2, 10, 0))
print(simp_alert(8000, 20, 14, 4, 2))
print(simp_alert(18000, 20, 6, 5, 1))