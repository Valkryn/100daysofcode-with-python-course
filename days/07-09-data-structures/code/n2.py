# from states import us_state_abbrev , states_list
import states


def main(states):
    print(print_10th(states))
    print(dict_45th(states.us_state_abbrev))
    print(dict_27th(states.us_state_abbrev))


def print_10th(data, n=10):
    abbrev_states = list(data.us_state_abbrev.items())
    st_lst = data.states_list
    all = abbrev_states + st_lst
    new_lst = []
    i = 0
    while i < len(all):
        new_lst.append(all[i])
        i = i + n
    return new_lst


def dict_45th(data, n=45):
    data_list = list(data.keys())
    return data_list[n]


def dict_27th(data, n=27):
    data_list = list(data.values())
    return data_list[n]


if __name__ == '__main__':
    main(states)
