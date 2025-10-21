import random

plants = ["rose", "tomato", "oak"]
growth = {"rose": 2, "tomato": 4, "oak": 1}
resources = {"water": 5, "fertilizer": 3}
history = []  # (turn, plant, change)
turn = 0
# print("🌿 Welcome to Garden Keeper!")


def add_plant(plants, growth):
    new_plant = input("Enter a new plant name: ").strip().lower()

    if new_plant in plants:
        print(f"{new_plant} is already in your garden")
        return

    plants.append(new_plant)
    growth[new_plant] = 0
    print(f"🪴 Added {new_plant} to your garden!")


def grow_all(plants, growth):
    for plant in plants:
        growth[plant] = growth.get(plant, 0) + 1
    print("All plants grew a little.")


def water(plant, growth, resources):
    if plant in growth and resources["water"] > 0:
        growth[plant] += 2
        resources["water"] -= 1
        print(f"{plant} grew! Water left: {resources['water']}")
        return 2
    else:
        print(" Not enough water or invalid plant.")
        return 0


def water_other(plant, growth, resources):
    if plant not in growth and resources["water"] <= 0:
        print(" Not enough water or invalid plant.")
        return 0

    growth[plant] += 2
    resources["water"] -= 1
    print(f"{plant} grew! Water left: {resources['water']}")
    return 2


def fertilize(plant, growth, resources):
    if plant in growth and resources["fertilizer"] > 0:
        growth[plant] += 3
        resources["fertilizer"] -= 1
        print(f"{plant} thrived! Fertilizer left: {resources['fertilizer']}")
        return 3
    else:
        print(" No fertilizer left.")
        return 0


def weather_event(plants, growth):
    event = random.choice(["rain", "drought", "normal"])
    if event == "rain":
        for p in plants:
            growth[p] += 1
        print(" It rained! All plants grew faster.")
        return event
    elif event == "drought":
        for p in plants:
            growth[p] = max(0, growth[p] - 1)
        print(" Drought! Some plants dried a bit.")
        return event
    else:
        print("Mild weather today.")
        return event


def random_event(plants, growth, resources):
    event = random.choice(
        ["nothing", "bonus_water", "bonus_fertilizer", "pests"]
    )
    if event == "bonus_water":
        resources["water"] += 1
        print(" A rain barrel filled! +1 water.")
    elif event == "bonus_fertilizer":
        resources["fertilizer"] += 1
        print(" You found some compost! +1 fertilizer.")
    elif event == "pests":
        victim = random.choice(plants)
        growth[victim] = max(0, growth[victim] - 2)
        print(f" Pests ate some of your {victim}!")
    else:
        print(" Nothing unusual happened this turn.")


def record_history(history, turn, plant, change):
    history.append((turn, plant, change))


def save_game(filename, plants, growth, history):
    with open(filename, "w") as f:
        for p in plants:
            f.write(f"{p},{growth[p]}\n")
    print(f"Game saved to {filename}")


def load_game(filename):
    plants, growth = [], {}
    with open(filename) as f:
        for line in f:
            p, g = line.strip().split(",")
            plants.append(p)
            growth[p] = int(g)
    return plants, growth


if __name__ == "__main__":
    print("🌿 Welcome to Garden Keeper!")

    while True:
        turn += 1
        print(f"\n Turn {turn}")
        action = input(
            "Action? (add / water / fertilize / grow / report / quit):"
        ).lower()
        if action == "quit":
            break
        elif action == "add":
            add_plant(plants, growth)
        elif action == "grow":
            grow_all(plants, growth)
        elif action == "water":
            p = input("Which plant? ")
            delta = water(p, growth, resources)
            record_history(history, turn, p, delta)
        elif action == "fertilize":
            p = input("Which plant? ")
            delta = fertilize(p, growth, resources)
            record_history(history, turn, p, delta)
        elif action == "report":
            sorted_plants = sorted(
                [(v, k) for k, v in growth.items()], reverse=True
            )
            print(" Garden Report:")
            for value, name in sorted_plants:
                print(f"{name:10} {value}")
            random_event(plants, growth, resources)
            weather_event(plants, growth)

print("\n Final Garden Report:")
sorted_plants = sorted([(v, k) for k, v in growth.items()], reverse=True)
for value, name in sorted_plants:
    print(f"{name:10} {value}")
print("\n Growth History:")
for record in history:
    print(record)

save_game("garden_save.txt", plants, growth, history)
