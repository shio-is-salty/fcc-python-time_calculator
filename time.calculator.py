def add_time(start, duration, day=""):

  day = day.lower()
  days = {
    "monday": 1,
    "tuesday": 2,
    "wednesday": 3,
    "thursday": 4,
    "friday": 5,
    "saturday": 6,
    "sunday": 7
  }

  day_counter = 0

  if day:
    day = int(days[day])

  (time, format) = start.split()

  (hour, minute) = time.split(":")
  (dhour, dminute) = duration.split(":")

  AM_PM = format

  if format == "PM":
    hour = int(hour) + 12

  while int(dminute) >= 60:
    dminute = int(dminute) - 60
    dhour = int(dhour) + 1

  while int(dhour) >= 24:
    dhour = int(dhour) - 24
    if day:
      if day >= 7:
        day = 1
      else:
        day = int(day) + 1
    day_counter = int(day_counter) + 1

  new_hour = int(hour) + int(dhour)
  new_min = int(minute) + int(dminute)

  while int(new_min) >= 60:
    new_min = int(new_min) - 60
    new_hour += 1

  while int(new_hour) >= 24:
    new_hour = int(new_hour) - 24
    if day:
      if day >= 7:
        day = 1
      else:
        day = int(day) + 1
    day_counter = int(day_counter) + 1

  if int(new_hour) >= 12 and int(new_min) > 0:
    AM_PM = "PM"
  else:
    AM_PM = "AM"

  if int(new_hour) > 12:
    new_hour = int(new_hour) - 12

  if int(new_hour) == 0:
    new_hour = "12"

  if len(str(new_min)) < 2:
    new_min = "0" + str(new_min)

  get_day = ""

  if day:
    if day >= 1 and day <= 7:
      get_day = str(list(days.keys())[list(
        days.values()).index(day)]).capitalize()

  if day_counter > 1 and day:
    new_time = str(new_hour) + ":" + str(new_min) + " " + str(
      AM_PM) + ", " + get_day + " (" + str(day_counter) + " days later)"
  elif day_counter == 0 and day:
    new_time = str(new_hour) + ":" + str(new_min) + " " + str(
      AM_PM) + ", " + get_day
  elif day_counter == 1 and day:
    new_time = str(new_hour) + ":" + str(new_min) + " " + str(
      AM_PM) + ", " + str(get_day) + " " + "(next day)"

  elif day_counter > 1:
    new_time = str(new_hour) + ":" + str(new_min) + " " + str(
      AM_PM) + " " + "(" + str(day_counter) + " days later)"
  elif day:
    new_time = str(new_hour) + ":" + str(new_min) + " " + str(
      AM_PM) + ", " + get_day

  elif day_counter == 1:
    new_time = str(new_hour) + ":" + str(new_min) + " " + str(
      AM_PM) + " " + "(next day)"

  else:
    new_time = str(new_hour) + ":" + str(new_min) + " " + str(AM_PM)

  return new_time
