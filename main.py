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

    country_dict = get_order_dict(player_dict, COUNTRY)

    print_header("Players by country:")
    print_sorted_player_information(country_dict, player_dict)

def open_file(filename):
    '''Returns a file object if the given filename could be found and returns None otherwise'''
    try:
        return open(filename)
    except FileNotFoundError:
        return None

def get_player_dict(file_object):
    ''' Returns a dictionary where the key is the name of a player and the value is a tuple containing the rank, country, rating and birthyear of a player'''
    player_dict = dict()

    for line in file_object:
        rank, name, country, rating, birthyear = line.strip().split("; ")
        lastname, firstname= name.split(", ")
        player_dict[f"{firstname} {lastname}"] = (int(rank), country, int(rating), int(birthyear))

    return player_dict

def get_order_dict(player_dict, key):
    '''Returns a dictionary where the key is the given key and the value is a list of player names'''
    order_dict = dict()

    for name, data in player_dict.items():
        country = data[key]
        if country in order_dict:
            order_dict[country].append(name)
        else:
            order_dict[country] = [name]

    return order_dict

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
