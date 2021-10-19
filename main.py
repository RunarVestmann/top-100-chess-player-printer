RANK = 0
COUNTRY = 1
RATING = 2
BIRTHYEAR = 3

def main():
    filename = input("Enter filename: ")
    file_object = open_file(filename)
    if file_object == None:
        print(f"File: {filename} was not found")
        return

    player_dict = get_player_dict(file_object)

    file_object.close()

    country_dict = get_country_dict(player_dict)

    print_header("Players by country:")
    print_sorted_player_information(country_dict, player_dict)

def open_file(filename):
    try:
        return open(filename)
    except FileNotFoundError:
        return None

def get_player_dict(file_object):
    player_dict = dict()

    for line in file_object:
        rank, name, country, rating, birthyear = line.strip().split("; ")
        lastname, firstname= name.split(", ")
        player_dict[f"{firstname} {lastname}"] = (int(rank), country, int(rating), int(birthyear))

    return player_dict

def get_country_dict(player_dict):
    country_dict = dict()

    for name, data in player_dict.items():
        country = data[COUNTRY]
        if country in country_dict:
            country_dict[country].append(name)
        else:
            country_dict[country] = [name]

    return country_dict

def print_header(heading):
    print(heading)
    print("-" * len(heading))

def get_average_rating(players, player_dict):
    if len(players) == 0:
        return 0.0

    total_rating = 0
    for player in players:
        rating = player_dict[player][RATING]
        total_rating += rating

    return total_rating / len(players)

def print_sorted_player_information(order_dict, player_dict):
    for key in sorted(order_dict):
        players = order_dict[key]
        average_rating = get_average_rating(players, player_dict)
        print(f"{key} ({len(players)}) ({average_rating:.1f}):")
        for player in players:
            print(f"{player:>40}{player_dict[player][RATING]:>10d}")

if __name__ == "__main__":
    main()