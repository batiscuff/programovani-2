import random
import config as cfg


random.seed()  # initialization random generator


def generate_line_with_objs(objs_list, counts_list):
    enemy, bush = objs_list
    e_count, b_count = counts_list

    # Creating list with enemies and bushes
    enemies_list = [enemy] * e_count
    bushes_list = [bush] * b_count
    
    # Creating a spaces list based on enemies and bushes lists
    obj_in_line = len(enemies_list) + len(bushes_list)
    spaces_list = [" "] * (cfg.MAX_OBJ_IN_LINE - obj_in_line)

    result_list = enemies_list + bushes_list + spaces_list
    random.shuffle(result_list)
    return cfg.WALL + "".join(result_list) + cfg.WALL + "\n"


def generate_map():
    top_and_bottom_line = cfg.MAP_WIDTH * cfg.WALL

    MAP = f"{top_and_bottom_line}\n"
    for _ in range(cfg.MAP_HEIGHT - 2):
        enemies_count = random.randint(0, 2)
        bushes_count = random.randint(0, 4)
        MAP += generate_line_with_objs([cfg.ENEMY, cfg.BUSH], 
                                       [enemies_count, bushes_count])
    MAP += f"{top_and_bottom_line}\n"
    return MAP


def main():
    game_map = generate_map()
    print(game_map)


if __name__ == "__main__":
    main()
