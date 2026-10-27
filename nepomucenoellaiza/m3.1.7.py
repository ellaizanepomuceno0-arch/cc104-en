the_weather_is_good = True
sheep_counter = 120
true_or_false_condition = True
nice_restaurant_is_found = True
tickets_are_available = True


def go_for_a_walk():
    print("Going for a walk.")


def have_lunch():
    print("Having lunch.")


def sleep_and_dream():
    print("Sleeping and dreaming.")


def make_a_bed():
    print("Making a bed.")


def take_a_shower():
    print("Taking a shower.")


def feed_the_sheepdogs():
    print("Feeding the sheepdogs.")


def have_fun():
    print("Having fun.")


def go_to_a_theater():
    print("Going to a theater.")


def eat_a_sandwich():
    print("Eating a sandwich.")


def go_to_the_theater():
    print("Going to the theater.")


def go_shopping():
    print("Going shopping.")


def enjoy_the_movie():
    print("Enjoying the movie.")


def perform_if_condition_true():
    print("The condition is true.")


def perform_if_condition_false():
    print("The condition is false.")


if the_weather_is_good:
    go_for_a_walk()

have_lunch()

if sheep_counter >= 120:  # Evaluate a test expression
    sleep_and_dream()  # Execute if test expression is True

if sheep_counter >= 120:
    make_a_bed()
    take_a_shower()
    sleep_and_dream()

feed_the_sheepdogs()

if true_or_false_condition:
    perform_if_condition_true()
else:
    perform_if_condition_false()

if the_weather_is_good:
    go_for_a_walk()
else:
    go_to_the_theater()

have_lunch()

if the_weather_is_good:
    go_for_a_walk()
    have_fun()
else:
    go_to_a_theater()
    enjoy_the_movie()

have_lunch()

if the_weather_is_good:
    if nice_restaurant_is_found:
        have_lunch()
    else:
        eat_a_sandwich()
else:
    if tickets_are_available:
        go_to_the_theater()
    else:
        go_shopping()

