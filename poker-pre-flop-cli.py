def space_decorator(func):
    def space_wrapper():
        print('')
        func()
        print('')
    return space_wrapper


@space_decorator
def pre_flop_action_raise():
    print("ACTION TO TAKE >> Raise")


@space_decorator
def pre_flop_action_raise_or_fold():
    print("ACTION TO TAKE >> Raise or Fold")


@space_decorator
def pre_flop_action_raise_or_call():
    print("ACTION TO TAKE >> Raise or Call")


@space_decorator
def pre_flop_action_raise_call_or_fold():
    print("ACTION TO TAKE >> Raise, Call, or Fold")


@space_decorator
def pre_flop_action_call():
    print("ACTION TO TAKE >> Call")


@space_decorator
def pre_flop_action_call_or_fold():
    print("ACTION TO TAKE >> Call or Fold")


@space_decorator
def pre_flop_action_fold():
    print("ACTION TO TAKE >> Fold")


@space_decorator
def pre_flop_action_3bet():
    print("ACTION TO TAKE >> 3Bet")


@space_decorator
def pre_flop_action_3bet_or_fold():
    print("ACTION TO TAKE >> 3Bet or Fold")


@space_decorator
def pre_flop_action_3bet_or_call():
    print("ACTION TO TAKE >> 3Bet or Call")


@space_decorator
def pre_flop_action_3bet_call_or_fold():
    print("ACTION TO TAKE >> 3Bet, Call, or Fold")


@space_decorator
def pre_flop_action_4bet():
    print("ACTION TO TAKE >> 4Bet")


@space_decorator
def pre_flop_action_4bet_or_fold():
    print("ACTION TO TAKE >> 4Bet or Fold")


# RFI Ranges
def utg_rfi():
    if (hole_cards == "AA" or
            hole_cards == "KK" or
            hole_cards == "QQ" or
            hole_cards == "JJ" or
            hole_cards == "TT" or
            hole_cards == "99" or
            hole_cards == "88" or
            hole_cards == "77" or
            hole_cards == "ATo" or
            hole_cards == "AJo" or
            hole_cards == "AQo" or
            hole_cards == "AKo" or
            hole_cards == "A2s" or
            hole_cards == "A3s" or
            hole_cards == "A4s" or
            hole_cards == "A5s" or
            hole_cards == "A6s" or
            hole_cards == "A7s" or
            hole_cards == "A8s" or
            hole_cards == "A9s" or
            hole_cards == "ATs" or
            hole_cards == "AJs" or
            hole_cards == "AQs" or
            hole_cards == "AKs" or
            hole_cards == "KJo" or
            hole_cards == "KQo" or
            hole_cards == "K9s" or
            hole_cards == "KTs" or
            hole_cards == "KJs" or
            hole_cards == "KQs" or
            hole_cards == "Q9s" or
            hole_cards == "QTs" or
            hole_cards == "QJs" or
            hole_cards == "J9s" or
            hole_cards == "JTs" or
            hole_cards == "T9s"):
        pre_flop_action_raise()
    elif (hole_cards == "55" or
            hole_cards == "66" or
            hole_cards == "K8s" or
            hole_cards == "98s" or
            hole_cards == "87s" or
            hole_cards == "76s" or
            hole_cards == "65s"):
        pre_flop_action_raise_or_fold()
    else:
        pre_flop_action_fold()


def mp_rfi():
    if (hole_cards == "AA" or
            hole_cards == "KK" or
            hole_cards == "QQ" or
            hole_cards == "JJ" or
            hole_cards == "TT" or
            hole_cards == "99" or
            hole_cards == "88" or
            hole_cards == "77" or
            hole_cards == "66" or
            hole_cards == "55" or
            hole_cards == "ATo" or
            hole_cards == "AJo" or
            hole_cards == "AQo" or
            hole_cards == "AKo" or
            hole_cards == "A2s" or
            hole_cards == "A3s" or
            hole_cards == "A4s" or
            hole_cards == "A5s" or
            hole_cards == "A6s" or
            hole_cards == "A7s" or
            hole_cards == "A8s" or
            hole_cards == "A9s" or
            hole_cards == "ATs" or
            hole_cards == "AJs" or
            hole_cards == "AQs" or
            hole_cards == "AKs" or
            hole_cards == "KJo" or
            hole_cards == "KQo" or
            hole_cards == "K9s" or
            hole_cards == "KTs" or
            hole_cards == "KJs" or
            hole_cards == "KQs" or
            hole_cards == "Q9s" or
            hole_cards == "QTs" or
            hole_cards == "QJs" or
            hole_cards == "J9s" or
            hole_cards == "JTs" or
            hole_cards == "T9s" or
            hole_cards == "98s" or
            hole_cards == "87s" or
            hole_cards == "76s" or
            hole_cards == "65s" or
            hole_cards == "54s"):
        pre_flop_action_raise()
    elif (hole_cards == "33" or
          hole_cards == "44" or
          hole_cards == "K7s" or
          hole_cards == "K8s" or
          hole_cards == "QJs" or
          hole_cards == "T8s"):
        pre_flop_action_raise_or_fold()
    else:
        pre_flop_action_fold()


def co_rfi():
    if (hole_cards == "AA" or
            hole_cards == "KK" or
            hole_cards == "QQ" or
            hole_cards == "JJ" or
            hole_cards == "TT" or
            hole_cards == "99" or
            hole_cards == "88" or
            hole_cards == "77" or
            hole_cards == "66" or
            hole_cards == "55" or
            hole_cards == "44" or
            hole_cards == "33" or
            hole_cards == "22" or
            hole_cards == "A9o" or
            hole_cards == "ATo" or
            hole_cards == "AJo" or
            hole_cards == "AQo" or
            hole_cards == "AKo" or
            hole_cards == "A2s" or
            hole_cards == "A3s" or
            hole_cards == "A4s" or
            hole_cards == "A5s" or
            hole_cards == "A6s" or
            hole_cards == "A7s" or
            hole_cards == "A8s" or
            hole_cards == "A9s" or
            hole_cards == "ATs" or
            hole_cards == "AJs" or
            hole_cards == "AQs" or
            hole_cards == "AKs" or
            hole_cards == "KJo" or
            hole_cards == "KQo" or
            hole_cards == "K6s" or
            hole_cards == "K7s" or
            hole_cards == "K8s" or
            hole_cards == "K9s" or
            hole_cards == "KTs" or
            hole_cards == "KJs" or
            hole_cards == "KQs" or
            hole_cards == "QJo" or
            hole_cards == "Q8s" or
            hole_cards == "Q9s" or
            hole_cards == "QTs" or
            hole_cards == "QJs" or
            hole_cards == "J9s" or
            hole_cards == "JTs" or
            hole_cards == "T9s" or
            hole_cards == "98s" or
            hole_cards == "87s" or
            hole_cards == "76s" or
            hole_cards == "65s" or
            hole_cards == "54s"):
        pre_flop_action_raise()
    elif (hole_cards == "A8o" or
            hole_cards == "KTo" or
            hole_cards == "K3s" or
            hole_cards == "K4s" or
            hole_cards == "K5s" or
            hole_cards == "QTo" or
            hole_cards == "Q7s" or
            hole_cards == "JTo" or
            hole_cards == "J7s" or
            hole_cards == "J8s" or
            hole_cards == "T7s" or
            hole_cards == "T8s" or
            hole_cards == "97s" or
            hole_cards == "86s"):
        pre_flop_action_raise_or_fold()
    else:
        pre_flop_action_fold()


def btn_rfi():
    if (hole_cards == "AA" or
            hole_cards == "KK" or
            hole_cards == "QQ" or
            hole_cards == "JJ" or
            hole_cards == "TT" or
            hole_cards == "99" or
            hole_cards == "88" or
            hole_cards == "77" or
            hole_cards == "66" or
            hole_cards == "55" or
            hole_cards == "44" or
            hole_cards == "33" or
            hole_cards == "22" or
            hole_cards == "A5o" or
            hole_cards == "A6o" or
            hole_cards == "A7o" or
            hole_cards == "A8o" or
            hole_cards == "A9o" or
            hole_cards == "ATo" or
            hole_cards == "AJo" or
            hole_cards == "AQo" or
            hole_cards == "AKo" or
            hole_cards == "A2s" or
            hole_cards == "A3s" or
            hole_cards == "A4s" or
            hole_cards == "A5s" or
            hole_cards == "A6s" or
            hole_cards == "A7s" or
            hole_cards == "A8s" or
            hole_cards == "A9s" or
            hole_cards == "ATs" or
            hole_cards == "AJs" or
            hole_cards == "AQs" or
            hole_cards == "AKs" or
            hole_cards == "K8o" or
            hole_cards == "K9o" or
            hole_cards == "KTo" or
            hole_cards == "KJo" or
            hole_cards == "KQo" or
            hole_cards == "K2s" or
            hole_cards == "K3s" or
            hole_cards == "K4s" or
            hole_cards == "K5s" or
            hole_cards == "K6s" or
            hole_cards == "K7s" or
            hole_cards == "K8s" or
            hole_cards == "K9s" or
            hole_cards == "KTs" or
            hole_cards == "KJs" or
            hole_cards == "KQs" or
            hole_cards == "Q9o" or
            hole_cards == "QTo" or
            hole_cards == "QJo" or
            hole_cards == "Q4s" or
            hole_cards == "Q5s" or
            hole_cards == "Q6s" or
            hole_cards == "Q8s" or
            hole_cards == "Q9s" or
            hole_cards == "QTs" or
            hole_cards == "QJs" or
            hole_cards == "J9o" or
            hole_cards == "JTo" or
            hole_cards == "J6s" or
            hole_cards == "J7s" or
            hole_cards == "J8s" or
            hole_cards == "J9s" or
            hole_cards == "JTs" or
            hole_cards == "T9o" or
            hole_cards == "T7s" or
            hole_cards == "T8s" or
            hole_cards == "T9s" or
            hole_cards == "97s" or
            hole_cards == "98s" or
            hole_cards == "87s" or
            hole_cards == "76s" or
            hole_cards == "65s" or
            hole_cards == "54s"):
        pre_flop_action_raise()
    elif (hole_cards == "A4o" or
            hole_cards == "Q2s" or
            hole_cards == "Q3s" or
            hole_cards == "J8o" or
            hole_cards == "J4s" or
            hole_cards == "J5s" or
            hole_cards == "T8o" or
            hole_cards == "T6s" or
            hole_cards == "98o" or
            hole_cards == "96s" or
            hole_cards == "86s" or
            hole_cards == "75s"):
        pre_flop_action_raise_or_fold()
    else:
        pre_flop_action_fold()


def sb_rfi():
    if (hole_cards == "AA" or
            hole_cards == "KK" or
            hole_cards == "QQ" or
            hole_cards == "JJ" or
            hole_cards == "TT" or
            hole_cards == "99" or
            hole_cards == "88" or
            hole_cards == "77" or
            hole_cards == "66" or
            hole_cards == "55" or
            hole_cards == "44" or
            hole_cards == "33" or
            hole_cards == "22" or
            hole_cards == "A5o" or
            hole_cards == "A6o" or
            hole_cards == "A7o" or
            hole_cards == "A8o" or
            hole_cards == "A9o" or
            hole_cards == "ATo" or
            hole_cards == "AJo" or
            hole_cards == "AQo" or
            hole_cards == "AKo" or
            hole_cards == "A2s" or
            hole_cards == "A3s" or
            hole_cards == "A4s" or
            hole_cards == "A5s" or
            hole_cards == "A6s" or
            hole_cards == "A7s" or
            hole_cards == "A8s" or
            hole_cards == "A9s" or
            hole_cards == "ATs" or
            hole_cards == "AJs" or
            hole_cards == "AQs" or
            hole_cards == "AKs" or
            hole_cards == "K8o" or
            hole_cards == "K9o" or
            hole_cards == "KTo" or
            hole_cards == "KJo" or
            hole_cards == "KQo" or
            hole_cards == "K2s" or
            hole_cards == "K3s" or
            hole_cards == "K4s" or
            hole_cards == "K5s" or
            hole_cards == "K6s" or
            hole_cards == "K7s" or
            hole_cards == "K8s" or
            hole_cards == "K9s" or
            hole_cards == "KTs" or
            hole_cards == "KJs" or
            hole_cards == "KQs" or
            hole_cards == "Q9o" or
            hole_cards == "QTo" or
            hole_cards == "QJo" or
            hole_cards == "Q4s" or
            hole_cards == "Q5s" or
            hole_cards == "Q6s" or
            hole_cards == "Q8s" or
            hole_cards == "Q9s" or
            hole_cards == "QTs" or
            hole_cards == "QJs" or
            hole_cards == "J9o" or
            hole_cards == "JTo" or
            hole_cards == "J6s" or
            hole_cards == "J7s" or
            hole_cards == "J8s" or
            hole_cards == "J9s" or
            hole_cards == "JTs" or
            hole_cards == "T9o" or
            hole_cards == "T7s" or
            hole_cards == "T8s" or
            hole_cards == "T9s" or
            hole_cards == "98o" or
            hole_cards == "97s" or
            hole_cards == "98s" or
            hole_cards == "87s" or
            hole_cards == "76s" or
            hole_cards == "65s" or
            hole_cards == "54s"):
        pre_flop_action_raise()
    elif (hole_cards == "A2o" or
            hole_cards == "A3o" or
            hole_cards == "A4o" or
            hole_cards == "K7o" or
            hole_cards == "Q8o" or
            hole_cards == "Q2s" or
            hole_cards == "Q3s" or
            hole_cards == "J8o" or
            hole_cards == "J4s" or
            hole_cards == "J5s" or
            hole_cards == "T8o" or
            hole_cards == "T6s" or
            hole_cards == "98o" or
            hole_cards == "96s" or
            hole_cards == "86s" or
            hole_cards == "75s"):
        pre_flop_action_raise_or_fold()
    else:
        pre_flop_action_fold()


# VS RFI Ranges
def mp_vs_utg_rfi():
    if (hole_cards == "AA" or
            hole_cards == "KK" or
            hole_cards == "QQ" or
            hole_cards == "JJ" or
            hole_cards == "TT" or
            hole_cards == "AQo" or
            hole_cards == "AKo" or
            hole_cards == "A4s" or
            hole_cards == "A5s" or
            hole_cards == "AJs" or
            hole_cards == "AQs" or
            hole_cards == "AKs" or
            hole_cards == "KJs" or
            hole_cards == "KQs" or
            hole_cards == "QJs"):
        pre_flop_action_3bet()
    elif (hole_cards == "99" or
          hole_cards == "A9s" or
          hole_cards == "ATs" or
          hole_cards == "KTs" or
          hole_cards == "76s" or
          hole_cards == "65s" or
          hole_cards == "54s"):
        pre_flop_action_3bet_or_fold()
    else:
        pre_flop_action_fold()


def co_vs_utg_rfi():
    if (hole_cards == "AA" or
            hole_cards == "KK" or
            hole_cards == "QQ" or
            hole_cards == "JJ" or
            hole_cards == "TT" or
            hole_cards == "99" or
            hole_cards == "AQo" or
            hole_cards == "AKo" or
            hole_cards == "A4s" or
            hole_cards == "A5s" or
            hole_cards == "A9s" or
            hole_cards == "ATs" or
            hole_cards == "AJs" or
            hole_cards == "AQs" or
            hole_cards == "AKs" or
            hole_cards == "KTs" or
            hole_cards == "KJs" or
            hole_cards == "KQs" or
            hole_cards == "QJs"):
        pre_flop_action_3bet()
    elif (hole_cards == "88" or
            hole_cards == "KQo" or
            hole_cards == "QTs" or
            hole_cards == "76s" or
            hole_cards == "65s" or
            hole_cards == "54s"):
        pre_flop_action_3bet_or_fold()
    else:
        pre_flop_action_fold()


def btn_vs_utg_rfi():
    if (hole_cards == "AA" or
            hole_cards == "KK" or
            hole_cards == "QQ" or
            hole_cards == "AKo" or
            hole_cards == "A4s" or
            hole_cards == "A5s" or
            hole_cards == "AKs" or
            hole_cards == "QTs" or
            hole_cards == "QJs"):
        pre_flop_action_3bet()
    elif hole_cards == "AJo" or hole_cards == "K9s":
        pre_flop_action_3bet_or_fold()
    elif (hole_cards == "JJ" or
          hole_cards == "TT" or
          hole_cards == "AQo" or
          hole_cards == "A3s" or
          hole_cards == "A8s" or
          hole_cards == "A9s" or
          hole_cards == "AQs" or
          hole_cards == "KQo" or
          hole_cards == "KTs" or
          hole_cards == "T9s"):
        pre_flop_action_3bet_or_call()
    elif (hole_cards == "98s" or
          hole_cards == "87s" or
          hole_cards == "76s" or
          hole_cards == "65s" or
          hole_cards == "54s"):
        pre_flop_action_3bet_call_or_fold()
    elif (hole_cards == "99" or
          hole_cards == "88" or
          hole_cards == "77" or
          hole_cards == "66" or
          hole_cards == "ATs" or
          hole_cards == "AJs" or
          hole_cards == "KJs" or
          hole_cards == "KQs" or
          hole_cards == "JTs"):
        pre_flop_action_call()
    elif hole_cards == "55" or hole_cards == "44" or hole_cards == "33" or hole_cards == "22":
        pre_flop_action_call_or_fold()
    else:
        pre_flop_action_fold()


def sb_vs_utg_rfi():
    if hole_cards == "AA" or hole_cards == "KK" or hole_cards == "AKs":
        pre_flop_action_3bet()
    elif hole_cards == "AQo" or hole_cards == "A9s":
        pre_flop_action_3bet_or_fold()
    elif (hole_cards == "QQ" or
            hole_cards == "JJ" or
            hole_cards == "AKo" or
            hole_cards == "AJs" or
            hole_cards == "KJs" or
            hole_cards == "KQs"):
        pre_flop_action_3bet_or_call()
    elif hole_cards == "A5s" or hole_cards == "KTs":
        pre_flop_action_3bet_call_or_fold()
    elif hole_cards == "TT" or hole_cards == "AQs":
        pre_flop_action_call()
    elif (hole_cards == "99" or
            hole_cards == "88" or
            hole_cards == "77" or
            hole_cards == "66" or
            hole_cards == "55" or
            hole_cards == "A4s" or
            hole_cards == "ATs" or
            hole_cards == "QTs" or
            hole_cards == "QJs" or
            hole_cards == "JTs" or
            hole_cards == "T9s" or
            hole_cards == "98s" or
            hole_cards == "87s" or
            hole_cards == "76s" or
            hole_cards == "65s"):
        pre_flop_action_call_or_fold()
    else:
        pre_flop_action_fold()


def bb_vs_utg_rfi():
    if (hole_cards == "AA" or
            hole_cards == "KK" or
            hole_cards == "QQ" or
            hole_cards == "AKo" or
            hole_cards == "AKs"):
        pre_flop_action_3bet()
    elif (hole_cards == "JJ" or
            hole_cards == "A2s" or
            hole_cards == "A3s" or
            hole_cards == "A4s" or
            hole_cards == "A5s" or
            hole_cards == "A8s" or
            hole_cards == "A9s" or
            hole_cards == "ATs" or
            hole_cards == "AJs" or
            hole_cards == "AQs" or
            hole_cards == "K6s" or
            hole_cards == "K7s" or
            hole_cards == "KTs" or
            hole_cards == "KJs" or
            hole_cards == "KQs" or
            hole_cards == "Q9s" or
            hole_cards == "QTs" or
            hole_cards == "QJs" or
            hole_cards == "JTs" or
            hole_cards == "87s" or
            hole_cards == "76s" or
            hole_cards == "65s" or
            hole_cards == "54s"):
        pre_flop_action_3bet_or_call()
    elif (hole_cards == "TT" or
            hole_cards == "99" or
            hole_cards == "88" or
            hole_cards == "77" or
            hole_cards == "66" or
            hole_cards == "55" or
            hole_cards == "44" or
            hole_cards == "33" or
            hole_cards == "22" or
            hole_cards == "ATo" or
            hole_cards == "AJo" or
            hole_cards == "AQo" or
            hole_cards == "A6s" or
            hole_cards == "A7s" or
            hole_cards == "KJo" or
            hole_cards == "KQo" or
            hole_cards == "K2s" or
            hole_cards == "K3s" or
            hole_cards == "K4s" or
            hole_cards == "K5s" or
            hole_cards == "K8s" or
            hole_cards == "K9s" or
            hole_cards == "Q6s" or
            hole_cards == "Q7s" or
            hole_cards == "Q8s" or
            hole_cards == "J8s" or
            hole_cards == "J9s" or
            hole_cards == "T7s" or
            hole_cards == "T8s" or
            hole_cards == "T9s" or
            hole_cards == "96s" or
            hole_cards == "97s" or
            hole_cards == "98s" or
            hole_cards == "86s" or
            hole_cards == "75s" or
            hole_cards == "64s" or
            hole_cards == "53s" or
            hole_cards == "43s"):
        pre_flop_action_call()
    elif (hole_cards == "QJo" or
            hole_cards == "Q3s" or
            hole_cards == "Q4s" or
            hole_cards == "Q5s" or
            hole_cards == "J7s" or
            hole_cards == "52s" or
            hole_cards == "42s"):
        pre_flop_action_call_or_fold()
    else:
        pre_flop_action_fold()


def co_vs_mp_rfi():
    if (hole_cards == "AA" or
            hole_cards == "KK" or
            hole_cards == "QQ" or
            hole_cards == "JJ" or
            hole_cards == "TT" or
            hole_cards == "99" or
            hole_cards == "88" or
            hole_cards == "AQo" or
            hole_cards == "AKo" or
            hole_cards == "A4s" or
            hole_cards == "A5s" or
            hole_cards == "A9s" or
            hole_cards == "ATs" or
            hole_cards == "AJs" or
            hole_cards == "AQs" or
            hole_cards == "AKs" or
            hole_cards == "KQo" or
            hole_cards == "KTs" or
            hole_cards == "KJs" or
            hole_cards == "KQs" or
            hole_cards == "QTs" or
            hole_cards == "QJs" or
            hole_cards == "JTs"):
        pre_flop_action_3bet()
    elif (hole_cards == "AJo" or
            hole_cards == "76s" or
            hole_cards == "65s" or
            hole_cards == "54s"):
        pre_flop_action_3bet_or_fold()
    else:
        pre_flop_action_fold()


def btn_vs_mp_rfi():
    if (hole_cards == "AA" or
            hole_cards == "KK" or
            hole_cards == "QQ" or
            hole_cards == "AKo" or
            hole_cards == "A4s" or
            hole_cards == "A5s" or
            hole_cards == "AKs" or
            hole_cards == "QTs" or
            hole_cards == "QJs"):
        pre_flop_action_3bet()
    elif hole_cards == "AJo" or hole_cards == "A6s" or hole_cards == "K9s":
        pre_flop_action_3bet_or_fold()
    elif (hole_cards == "JJ" or
            hole_cards == "TT" or
            hole_cards == "AQo" or
            hole_cards == "A3s" or
            hole_cards == "A8s" or
            hole_cards == "A9s" or
            hole_cards == "AQs" or
            hole_cards == "KQo" or
            hole_cards == "KTs" or
            hole_cards == "KJs" or
            hole_cards == "KQs" or
            hole_cards == "Q9s" or
            hole_cards == "J9s" or
            hole_cards == "JTs" or
            hole_cards == "T9s"):
        pre_flop_action_3bet_or_call()
    elif (hole_cards == "A7s" or
            hole_cards == "98s" or
            hole_cards == "87s" or
            hole_cards == "76s" or
            hole_cards == "65s" or
            hole_cards == "54s"):
        pre_flop_action_3bet_call_or_fold()
    elif (hole_cards == "99" or
            hole_cards == "88" or
            hole_cards == "77" or
            hole_cards == "66" or
            hole_cards == "ATs" or
            hole_cards == "AJs"):
        pre_flop_action_call()
    elif (hole_cards == "55" or
            hole_cards == "44" or
            hole_cards == "33" or
            hole_cards == "22"):
        pre_flop_action_call_or_fold()
    else:
        pre_flop_action_fold()


def sb_vs_mp_rfi():
    if (hole_cards == "AA" or
            hole_cards == "KK" or
            hole_cards == "QQ" or
            hole_cards == "JJ" or
            hole_cards == "TT" or
            hole_cards == "99" or
            hole_cards == "AQo" or
            hole_cards == "AKo" or
            hole_cards == "A5s" or
            hole_cards == "ATs" or
            hole_cards == "AJs" or
            hole_cards == "AQs" or
            hole_cards == "AKs" or
            hole_cards == "KTs" or
            hole_cards == "KJs" or
            hole_cards == "KQs" or
            hole_cards == "QTs" or
            hole_cards == "QJs" or
            hole_cards == "JTs"):
        pre_flop_action_3bet()
    elif hole_cards == "88" or hole_cards == "A4s":
        pre_flop_action_3bet_or_fold()
    else:
        pre_flop_action_fold()


def bb_vs_mp_rfi():
    if (hole_cards == "AA" or
            hole_cards == "KK" or
            hole_cards == "QQ" or
            hole_cards == "AKo" or
            hole_cards == "AKs"):
        pre_flop_action_3bet()
    elif (hole_cards == "JJ" or
            hole_cards == "TT" or
            hole_cards == "A2s" or
            hole_cards == "A3s" or
            hole_cards == "A4s" or
            hole_cards == "A5s" or
            hole_cards == "A8s" or
            hole_cards == "A9s" or
            hole_cards == "ATs" or
            hole_cards == "AJs" or
            hole_cards == "AQs" or
            hole_cards == "K6s" or
            hole_cards == "K7s" or
            hole_cards == "KTs" or
            hole_cards == "KJs" or
            hole_cards == "KQs" or
            hole_cards == "Q9s" or
            hole_cards == "QTs" or
            hole_cards == "QJs" or
            hole_cards == "JTs" or
            hole_cards == "87s" or
            hole_cards == "76s" or
            hole_cards == "65s" or
            hole_cards == "54s"):
        pre_flop_action_3bet_or_call()
    elif (hole_cards == "99" or
            hole_cards == "88" or
            hole_cards == "77" or
            hole_cards == "66" or
            hole_cards == "55" or
            hole_cards == "44" or
            hole_cards == "33" or
            hole_cards == "22" or
            hole_cards == "ATo" or
            hole_cards == "AJo" or
            hole_cards == "AQo" or
            hole_cards == "A6s" or
            hole_cards == "A7s" or
            hole_cards == "KJo" or
            hole_cards == "KQo" or
            hole_cards == "K2s" or
            hole_cards == "K3s" or
            hole_cards == "K4s" or
            hole_cards == "K5s" or
            hole_cards == "K8s" or
            hole_cards == "K9s" or
            hole_cards == "QJo" or
            hole_cards == "Q6s" or
            hole_cards == "Q7s" or
            hole_cards == "Q8s" or
            hole_cards == "J8s" or
            hole_cards == "J9s" or
            hole_cards == "T7s" or
            hole_cards == "T8s" or
            hole_cards == "T9s" or
            hole_cards == "96s" or
            hole_cards == "97s" or
            hole_cards == "98s" or
            hole_cards == "86s" or
            hole_cards == "75s" or
            hole_cards == "64s" or
            hole_cards == "53s" or
            hole_cards == "43s"):
        pre_flop_action_call()
    elif (hole_cards == "A9o" or
            hole_cards == "KTo" or
            hole_cards == "QTo" or
            hole_cards == "Q3s" or
            hole_cards == "Q4s" or
            hole_cards == "Q5s" or
            hole_cards == "JTo" or
            hole_cards == "J7s" or
            hole_cards == "85s" or
            hole_cards == "74s" or
            hole_cards == "63s" or
            hole_cards == "52s" or
            hole_cards == "42s"):
        pre_flop_action_call_or_fold()
    else:
        pre_flop_action_fold()


def btn_vs_co_rfi():
    if (hole_cards == "AA" or
            hole_cards == "KK" or
            hole_cards == "QQ" or
            hole_cards == "AKo" or
            hole_cards == "AQs" or
            hole_cards == "AKs" or
            hole_cards == "QTs" or
            hole_cards == "QJs"):
        pre_flop_action_3bet()
    elif hole_cards == "ATo" or hole_cards == "KJo" or hole_cards == "K8s":
        pre_flop_action_3bet_or_fold()
    elif (hole_cards == "JJ" or
            hole_cards == "TT" or
            hole_cards == "99" or
            hole_cards == "88" or
            hole_cards == "77" or
            hole_cards == "66" or
            hole_cards == "55" or
            hole_cards == "AJo" or
            hole_cards == "AQo" or
            hole_cards == "A3s" or
            hole_cards == "A4s" or
            hole_cards == "A5s" or
            hole_cards == "A6s" or
            hole_cards == "A7s" or
            hole_cards == "A8s" or
            hole_cards == "A9s" or
            hole_cards == "ATs" or
            hole_cards == "AJs" or
            hole_cards == "KQo" or
            hole_cards == "KTs" or
            hole_cards == "KJs" or
            hole_cards == "KQs" or
            hole_cards == "Q9s" or
            hole_cards == "J9s" or
            hole_cards == "JTs" or
            hole_cards == "T9s"):
        pre_flop_action_3bet_or_call()
    elif (hole_cards == "A2s" or
            hole_cards == "K9s" or
            hole_cards == "98s" or
            hole_cards == "87s" or
            hole_cards == "76s" or
            hole_cards == "65s" or
            hole_cards == "54s"):
        pre_flop_action_3bet_call_or_fold()
    elif (hole_cards == "44" or
            hole_cards == "33" or
            hole_cards == "22"):
        pre_flop_action_call_or_fold()
    else:
        pre_flop_action_fold()


def sb_vs_co_rfi():
    if (hole_cards == "AA" or
            hole_cards == "KK" or
            hole_cards == "QQ" or
            hole_cards == "JJ" or
            hole_cards == "TT" or
            hole_cards == "99" or
            hole_cards == "AQo" or
            hole_cards == "AKo" or
            hole_cards == "A5s" or
            hole_cards == "ATs" or
            hole_cards == "AJs" or
            hole_cards == "AQs" or
            hole_cards == "AKs" or
            hole_cards == "KTs" or
            hole_cards == "KJs" or
            hole_cards == "KQs" or
            hole_cards == "QTs" or
            hole_cards == "QJs" or
            hole_cards == "JTs"):
        pre_flop_action_3bet()
    elif (hole_cards == "88" or
            hole_cards == "77" or
          hole_cards == "AJo" or
          hole_cards == "A4s" or
          hole_cards == "A9s" or
          hole_cards == "K9s" or
          hole_cards == "J9s" or
          hole_cards == "T9s"):
        pre_flop_action_3bet_or_fold()
    else:
        pre_flop_action_fold()


def bb_vs_co_rfi():
    if (hole_cards == "AA" or
            hole_cards == "KK" or
            hole_cards == "QQ" or
            hole_cards == "JJ" or
            hole_cards == "AKo" or
            hole_cards == "AQs" or
            hole_cards == "AKs"):
        pre_flop_action_3bet()
    elif (hole_cards == "TT" or
            hole_cards == "AQo" or
            hole_cards == "A2s" or
            hole_cards == "A3s" or
            hole_cards == "A4s" or
            hole_cards == "A5s" or
            hole_cards == "ATs" or
            hole_cards == "AJs" or
            hole_cards == "KQo" or
            hole_cards == "K6s" or
            hole_cards == "K7s" or
            hole_cards == "KTs" or
            hole_cards == "KJs" or
            hole_cards == "KQs" or
            hole_cards == "Q4s" or
            hole_cards == "Q5s" or
            hole_cards == "Q9s" or
            hole_cards == "QTs" or
            hole_cards == "QJs" or
            hole_cards == "J9s" or
            hole_cards == "JTs" or
            hole_cards == "T9s" or
            hole_cards == "87s" or
            hole_cards == "76s" or
            hole_cards == "65s" or
            hole_cards == "54s"):
        pre_flop_action_3bet_or_call()
    elif (hole_cards == "99" or
            hole_cards == "88" or
            hole_cards == "77" or
            hole_cards == "66" or
            hole_cards == "55" or
            hole_cards == "44" or
            hole_cards == "33" or
            hole_cards == "22" or
            hole_cards == "A9o" or
            hole_cards == "ATo" or
            hole_cards == "AJo" or
            hole_cards == "A6s" or
            hole_cards == "A7s" or
            hole_cards == "A8s" or
            hole_cards == "A9s" or
            hole_cards == "KTo" or
            hole_cards == "KJo" or
            hole_cards == "K2s" or
            hole_cards == "K3s" or
            hole_cards == "K4s" or
            hole_cards == "K5s" or
            hole_cards == "K8s" or
            hole_cards == "K9s" or
            hole_cards == "QTo" or
            hole_cards == "QJo" or
            hole_cards == "Q6s" or
            hole_cards == "Q7s" or
            hole_cards == "Q8s" or
            hole_cards == "JTo" or
            hole_cards == "J7s" or
            hole_cards == "J8s" or
            hole_cards == "T7s" or
            hole_cards == "T8s" or
            hole_cards == "96s" or
            hole_cards == "97s" or
            hole_cards == "98s" or
            hole_cards == "86s" or
            hole_cards == "75s" or
            hole_cards == "64s" or
            hole_cards == "53s" or
            hole_cards == "43s"):
        pre_flop_action_call()
    elif (hole_cards == "A9o" or
            hole_cards == "KTo" or
            hole_cards == "QTo" or
            hole_cards == "Q3s" or
            hole_cards == "Q4s" or
            hole_cards == "Q5s" or
            hole_cards == "JTo" or
            hole_cards == "J7s" or
            hole_cards == "85s" or
            hole_cards == "74s" or
            hole_cards == "63s" or
            hole_cards == "52s" or
            hole_cards == "42s"):
        pre_flop_action_call_or_fold()
    else:
        pre_flop_action_fold()


def sb_vs_btn_rfi():
    if (hole_cards == "AA" or
            hole_cards == "KK" or
            hole_cards == "QQ" or
            hole_cards == "JJ" or
            hole_cards == "TT" or
            hole_cards == "99" or
            hole_cards == "88" or
            hole_cards == "77" or
            hole_cards == "AJo" or
            hole_cards == "AQo" or
            hole_cards == "AKo" or
            hole_cards == "A4s" or
            hole_cards == "A5s" or
            hole_cards == "A6s" or
            hole_cards == "A7s" or
            hole_cards == "A8s" or
            hole_cards == "A9s" or
            hole_cards == "ATs" or
            hole_cards == "AJs" or
            hole_cards == "AQs" or
            hole_cards == "AKs" or
            hole_cards == "KQo" or
            hole_cards == "K9s" or
            hole_cards == "KTs" or
            hole_cards == "KJs" or
            hole_cards == "KQs" or
            hole_cards == "QTs" or
            hole_cards == "QJs" or
            hole_cards == "J9s" or
            hole_cards == "JTs" or
            hole_cards == "T9s"):
        pre_flop_action_3bet()
    elif (hole_cards == "66" or
            hole_cards == "55" or
          hole_cards == "ATo" or
          hole_cards == "A7s" or
          hole_cards == "KJo" or
          hole_cards == "Q9s"):
        pre_flop_action_3bet_or_fold()
    else:
        pre_flop_action_fold()


def bb_vs_btn_rfi():
    if (hole_cards == "AA" or
            hole_cards == "KK" or
            hole_cards == "QQ" or
            hole_cards == "JJ" or
            hole_cards == "TT" or
            hole_cards == "AKo" or
            hole_cards == "AQs" or
            hole_cards == "AKs" or
            hole_cards == "J9s" or
            hole_cards == "JTs" or
            hole_cards == "T9s"):
        pre_flop_action_3bet()
    elif (hole_cards == "99" or
            hole_cards == "88" or
            hole_cards == "ATo" or
            hole_cards == "AJo" or
            hole_cards == "AQo" or
            hole_cards == "A2s" or
            hole_cards == "A3s" or
            hole_cards == "A4s" or
            hole_cards == "A5s" or
            hole_cards == "ATs" or
            hole_cards == "AJs" or
            hole_cards == "KJo" or
            hole_cards == "KQo" or
            hole_cards == "K6s" or
            hole_cards == "K7s" or
            hole_cards == "K9s" or
            hole_cards == "KTs" or
            hole_cards == "KJs" or
            hole_cards == "KQs" or
            hole_cards == "Q8s" or
            hole_cards == "Q9s" or
            hole_cards == "QTs" or
            hole_cards == "QJs" or
            hole_cards == "J7s" or
            hole_cards == "J8s" or
            hole_cards == "T6s" or
            hole_cards == "T7s" or
            hole_cards == "T8s" or
            hole_cards == "97s" or
            hole_cards == "98s" or
            hole_cards == "87s" or
            hole_cards == "76s" or
            hole_cards == "65s" or
            hole_cards == "54s"):
        pre_flop_action_3bet_or_call()
    elif (hole_cards == "77" or
            hole_cards == "66" or
            hole_cards == "55" or
            hole_cards == "44" or
            hole_cards == "33" or
            hole_cards == "22" or
            hole_cards == "A5o" or
            hole_cards == "A7o" or
            hole_cards == "A8o" or
            hole_cards == "A9o" or
            hole_cards == "A6s" or
            hole_cards == "A7s" or
            hole_cards == "A8s" or
            hole_cards == "A9s" or
            hole_cards == "K9o" or
            hole_cards == "KTo" or
            hole_cards == "K2s" or
            hole_cards == "K3s" or
            hole_cards == "K4s" or
            hole_cards == "K5s" or
            hole_cards == "K8s" or
            hole_cards == "QTo" or
            hole_cards == "QJo" or
            hole_cards == "Q2s" or
            hole_cards == "Q3s" or
            hole_cards == "Q4s" or
            hole_cards == "Q5s" or
            hole_cards == "Q6s" or
            hole_cards == "Q7s" or
            hole_cards == "J9o" or
            hole_cards == "JTo" or
            hole_cards == "J4s" or
            hole_cards == "J5s" or
            hole_cards == "J6s" or
            hole_cards == "T9o" or
            hole_cards == "96s" or
            hole_cards == "85s" or
            hole_cards == "86s" or
            hole_cards == "74s" or
            hole_cards == "75s" or
            hole_cards == "64s" or
            hole_cards == "53s" or
            hole_cards == "43s"):
        pre_flop_action_call()
    elif (hole_cards == "A4o" or
            hole_cards == "A6o" or
            hole_cards == "K8o" or
            hole_cards == "Q9o" or
            hole_cards == "T8o" or
            hole_cards == "98o" or
            hole_cards == "87o" or
            hole_cards == "76o" or
            hole_cards == "65o" or
            hole_cards == "63s" or
            hole_cards == "52s" or
            hole_cards == "42s"):
        pre_flop_action_call_or_fold()
    else:
        pre_flop_action_fold()


def bb_vs_sb_rfi():
    if (hole_cards == "AA" or
            hole_cards == "KK" or
            hole_cards == "QQ" or
            hole_cards == "JJ" or
            hole_cards == "TT" or
            hole_cards == "AQo" or
            hole_cards == "AKo" or
            hole_cards == "A4s" or
            hole_cards == "A5s" or
            hole_cards == "AQs" or
            hole_cards == "AKs"):
        pre_flop_action_3bet()
    elif (hole_cards == "99" or
            hole_cards == "88" or
            hole_cards == "A2o" or
            hole_cards == "A3o" or
            hole_cards == "A4o" or
            hole_cards == "AJo" or
            hole_cards == "A2s" or
            hole_cards == "A3s" or
            hole_cards == "ATs" or
            hole_cards == "AJs" or
            hole_cards == "K6o" or
            hole_cards == "KJo" or
            hole_cards == "KQo" or
            hole_cards == "KTs" or
            hole_cards == "KJs" or
            hole_cards == "KQs" or
            hole_cards == "Q9s" or
            hole_cards == "QTs" or
            hole_cards == "QJs" or
            hole_cards == "J8s" or
            hole_cards == "J9s" or
            hole_cards == "JTs" or
            hole_cards == "T8s" or
            hole_cards == "T9s" or
            hole_cards == "98s" or
            hole_cards == "87s" or
            hole_cards == "76s" or
            hole_cards == "65s" or
            hole_cards == "54s"):
        pre_flop_action_3bet_or_call()
    elif (hole_cards == "77" or
            hole_cards == "66" or
            hole_cards == "55" or
            hole_cards == "44" or
            hole_cards == "33" or
            hole_cards == "22" or
            hole_cards == "A5o" or
            hole_cards == "A6o" or
            hole_cards == "A7o" or
            hole_cards == "A8o" or
            hole_cards == "A9o" or
            hole_cards == "ATo" or
            hole_cards == "A6s" or
            hole_cards == "A7s" or
            hole_cards == "A8s" or
            hole_cards == "A9s" or
            hole_cards == "K7o" or
            hole_cards == "K8o" or
            hole_cards == "K9o" or
            hole_cards == "KTo" or
            hole_cards == "K2s" or
            hole_cards == "K3s" or
            hole_cards == "K4s" or
            hole_cards == "K5s" or
            hole_cards == "K6s" or
            hole_cards == "K7s" or
            hole_cards == "K8s" or
            hole_cards == "K9s" or
            hole_cards == "Q8o" or
            hole_cards == "Q9o" or
            hole_cards == "QTo" or
            hole_cards == "QJo" or
            hole_cards == "Q2s" or
            hole_cards == "Q3s" or
            hole_cards == "Q4s" or
            hole_cards == "Q5s" or
            hole_cards == "Q6s" or
            hole_cards == "Q7s" or
            hole_cards == "Q8o" or
            hole_cards == "J8o" or
            hole_cards == "J9o" or
            hole_cards == "JTo" or
            hole_cards == "J2s" or
            hole_cards == "J3s" or
            hole_cards == "J4s" or
            hole_cards == "J5s" or
            hole_cards == "J6s" or
            hole_cards == "J7s" or
            hole_cards == "T9o" or
            hole_cards == "T2s" or
            hole_cards == "T3s" or
            hole_cards == "T4s" or
            hole_cards == "T5s" or
            hole_cards == "T6s" or
            hole_cards == "T7s" or
            hole_cards == "95s" or
            hole_cards == "96s" or
            hole_cards == "97s" or
            hole_cards == "85s" or
            hole_cards == "86s" or
            hole_cards == "74s" or
            hole_cards == "75s" or
            hole_cards == "63s" or
            hole_cards == "64s" or
            hole_cards == "52s" or
            hole_cards == "53s" or
            hole_cards == "42s" or
            hole_cards == "43s" or
            hole_cards == "32s"):
        pre_flop_action_call()
    elif (hole_cards == "T8o" or
            hole_cards == "98o" or
            hole_cards == "87o" or
            hole_cards == "84s" or
            hole_cards == "76o" or
            hole_cards == "73s" or
            hole_cards == "65o"):
        pre_flop_action_call_or_fold()
    else:
        pre_flop_action_fold()


# Cold 4Bet Ranges
def cold_4bet_co_vs_mp_3bet():
    if hole_cards == "AA" or hole_cards == "KK" or hole_cards == "QQ" or hole_cards == "AKo" or hole_cards == "AKs":
        pre_flop_action_4bet()
    elif hole_cards == "A5s" or hole_cards == "AQs" or hole_cards == "KQs":
        pre_flop_action_4bet_or_fold()
    else:
        pre_flop_action_fold()


def cold_4bet_btn_vs_mp_3bet():
    if hole_cards == "AA" or hole_cards == "KK" or hole_cards == "QQ" or hole_cards == "AKo" or hole_cards == "AKs":
        pre_flop_action_4bet()
    elif hole_cards == "JJ" or hole_cards == "A5s" or hole_cards == "AQs" or hole_cards == "KQs":
        pre_flop_action_4bet_or_fold()
    else:
        pre_flop_action_fold()


def cold_4bet_btn_vs_co_3bet():
    if hole_cards == "AA" or hole_cards == "KK" or hole_cards == "QQ" or hole_cards == "AKo" or hole_cards == "AKs":
        pre_flop_action_4bet()
    elif (hole_cards == "JJ" or hole_cards == "TT" or hole_cards == "AQo" or hole_cards == "A5s" or
          hole_cards == "AQs" or hole_cards == "KJs" or hole_cards == "KQs"):
        pre_flop_action_4bet_or_fold()
    else:
        pre_flop_action_fold()


def cold_4bet_sb_vs_mp_3bet():
    if hole_cards == "AA" or hole_cards == "KK" or hole_cards == "QQ" or hole_cards == "AKo" or hole_cards == "AKs":
        pre_flop_action_4bet()
    elif hole_cards == "A5s" or hole_cards == "AQs" or hole_cards == "KQs":
        pre_flop_action_4bet_or_fold()
    else:
        pre_flop_action_fold()


def cold_4bet_sb_vs_co_3bet():
    if (hole_cards == "AA" or hole_cards == "KK" or hole_cards == "QQ" or hole_cards == "AKo" or
            hole_cards == "AQs" or hole_cards == "AKs" or hole_cards == "KQs"):
        pre_flop_action_4bet()
    elif hole_cards == "JJ" or hole_cards == "A5s" or hole_cards == "KJs":
        pre_flop_action_4bet_or_fold()
    else:
        pre_flop_action_fold()


def cold_4bet_sb_vs_btn_3bet():
    if (hole_cards == "AA" or hole_cards == "KK" or hole_cards == "QQ" or hole_cards == "AKo" or
            hole_cards == "AQs" or hole_cards == "AKs" or hole_cards == "KQs"):
        pre_flop_action_4bet()
    elif hole_cards == "JJ" or hole_cards == "AQo" or hole_cards == "AJs" or hole_cards == "KJs":
        pre_flop_action_4bet_or_fold()
    else:
        pre_flop_action_fold()


def cold_4bet_bb_vs_mp_3bet():
    if (hole_cards == "AA" or hole_cards == "KK" or hole_cards == "QQ" or hole_cards == "AKo" or
            hole_cards == "AQs" or hole_cards == "AKs" or hole_cards == "KQs"):
        pre_flop_action_4bet()
    elif hole_cards == "JJ" or hole_cards == "A5s":
        pre_flop_action_4bet_or_fold()
    else:
        pre_flop_action_fold()


def cold_4bet_bb_vs_co_3bet():
    if (hole_cards == "AA" or hole_cards == "KK" or hole_cards == "QQ" or hole_cards == "AKo" or
            hole_cards == "AQs" or hole_cards == "AKs" or hole_cards == "KQs"):
        pre_flop_action_4bet()
    elif hole_cards == "JJ" or hole_cards == "AQo" or hole_cards == "A5s" or hole_cards == "KJs":
        pre_flop_action_4bet_or_fold()
    else:
        pre_flop_action_fold()


def cold_4bet_bb_vs_btn_3bet():
    if (hole_cards == "AA" or hole_cards == "KK" or hole_cards == "QQ" or hole_cards == "AKo" or
            hole_cards == "AQs" or hole_cards == "AKs" or hole_cards == "KQs"):
        pre_flop_action_4bet()
    elif hole_cards == "JJ" or hole_cards == "TT" or hole_cards == "AQo" or hole_cards == "AJs" or hole_cards == "KJs":
        pre_flop_action_4bet_or_fold()
    else:
        pre_flop_action_fold()


def cold_4bet_bb_vs_sb_3bet_utg_or_mp_open():
    if (hole_cards == "AA" or hole_cards == "KK" or hole_cards == "QQ" or hole_cards == "JJ" or
            hole_cards == "TT" or hole_cards == "AKo" or hole_cards == "AJs" or hole_cards == "AQs" or
            hole_cards == "AKs" or hole_cards == "KJs" or hole_cards == "KQs"):
        pre_flop_action_4bet()
    elif hole_cards == "AQo":
        pre_flop_action_4bet_or_fold()
    else:
        pre_flop_action_fold()


def cold_4bet_bb_vs_sb_3bet_co_open():
    if (hole_cards == "AA" or hole_cards == "KK" or hole_cards == "QQ" or hole_cards == "JJ" or
            hole_cards == "TT" or hole_cards == "AKo" or hole_cards == "AJs" or hole_cards == "AQs" or
            hole_cards == "AKs" or hole_cards == "KJs" or hole_cards == "KQs"):
        pre_flop_action_4bet()
    elif hole_cards == "AQo" or hole_cards == "ATs":
        pre_flop_action_4bet_or_fold()
    else:
        pre_flop_action_fold()


def cold_4bet_bb_vs_sb_3bet_btn_open():
    if (hole_cards == "AA" or hole_cards == "KK" or hole_cards == "QQ" or hole_cards == "JJ" or
            hole_cards == "TT" or hole_cards == "AQo" or hole_cards == "AKo" or hole_cards == "AJs" or
            hole_cards == "AQs" or hole_cards == "AKs" or hole_cards == "KJs" or hole_cards == "KQs"):
        pre_flop_action_4bet()
    elif hole_cards == "99" or hole_cards == "ATs" or hole_cards == "KTs":
        pre_flop_action_4bet_or_fold()
    else:
        pre_flop_action_fold()


def title_decorator(func):
    def title_wrapper():
        print("********************")
        func()
        print("********************")
        print('')
    return title_wrapper


@title_decorator
def title():
    print('Welcome to Poker AI')


title()


def question_error_decorator(func):
    def error_wrapper():
        print('')
        func()
        print('')
    return error_wrapper


@question_error_decorator
def error_hole_cards():
    print('ERROR: Enter hole cards correctly (i.e. AA, 98s, QJo)')


@question_error_decorator
def error_my_table_pos():
    print('ERROR: Enter a correct table position 1 to 5.')


@question_error_decorator
def error_pf_scenario():
    print('ERROR: Enter a correct scenario 1 to 3.')


@question_error_decorator
def error_did_opp_3bet():
    print('ERROR: Can only enter 1 if opponent 3 bet you.')


@question_error_decorator
def error_opp_tbl_pos():
    print('ERROR: Enter the correct table position of opponent')


hole_cards_list = {'AA', 'KK', 'QQ', 'JJ', 'TT', '99', '88', '77', '66', '55', '44', '33', '22',
                   'A2o', 'A3o', 'A4o', 'A5o', 'A6o', 'A7o', 'A8o', 'A9o', 'ATo', 'AJo', 'AQo', 'AKo',
                   'A2s', 'A3s', 'A4s', 'A5s', 'A6s', 'A7s', 'A8s', 'A9s', 'ATs', 'AJs', 'AQs', 'AKs',
                   'K2o', 'K3o', 'K4o', 'K5o', 'K6o', 'K7o', 'K8o', 'K9o', 'KTo', 'KJo', 'KQo',
                   'K2s', 'K3s', 'K4s', 'K5s', 'K6s', 'K7s', 'K8s', 'K9s', 'KTs', 'KJs', 'KQs',
                   'Q2o', 'Q3o', 'Q4o', 'Q5o', 'Q6o', 'Q7o', 'Q8o', 'Q9o', 'QTo', 'QJo',
                   'Q2s', 'Q3s', 'Q4s', 'Q5s', 'Q6s', 'Q7s', 'Q8s', 'Q9s', 'QTs', 'QJs',
                   'J2o', 'J3o', 'J4o', 'J5o', 'J6o', 'J7o', 'J8o', 'J9o', 'JTo',
                   'J2s', 'J3s', 'J4s', 'J5s', 'J6s', 'J7s', 'J8s', 'J9s', 'JTs',
                   'T2o', 'T3o', 'T4o', 'T5o', 'T6o', 'T7o', 'T8o', 'T9o',
                   'T2s', 'T3s', 'T4s', 'T5s', 'T6s', 'T7s', 'T8s', 'T9s',
                   '92o', '93o', '94o', '95o', '96o', '97o', '98o',
                   '92s', '93s', '94s', '95s', '96s', '97s', '98s',
                   '82o', '83o', '84o', '85o', '86o', '87o',
                   '82s', '83s', '84s', '85s', '86s', '87s',
                   '72o', '73o', '74o', '75o', '76o',
                   '72s', '73s', '74s', '75s', '76s',
                   '62o', '63o', '64o', '65o',
                   '62s', '63s', '64s', '65s',
                   '52o', '53o', '54o',
                   '52s', '53s', '54s',
                   '42o', '43o',
                   '42s', '43s',
                   '32o',
                   '32s'}

while True:
    hole_cards = input('1. Enter your hole cards: ')
    if len(hole_cards) == 3:
        hole_cards = hole_cards[0:2].upper() + hole_cards[-1].lower()
        if hole_cards in hole_cards_list:
            break
    elif len(hole_cards) == 2:
        hole_cards = hole_cards.upper()
        if hole_cards in hole_cards_list:
            break
    else:
        error_hole_cards()

table_position_list = {'1', '2', '3', '4', '5', '6'}

while True:
    my_table_position = input("2. Enter your table position (1-UTG, 2-MP, 3-CO, 4-BTN, 5-SB, 6-BB): ")
    if my_table_position in table_position_list:
        break
    else:
        error_my_table_pos()

pre_flop_scenario_list = {'1', '2', '3'}

while True:
    pre_flop_scenario = input("3. Choose a scenario (1-RFI, 2-VS RFI, 3-Cold 4Bet): ")
    if pre_flop_scenario in pre_flop_scenario_list:
        break
    else:
        error_pf_scenario()

opp_3_bet_response_list = '1'
utg_vs_opp_3bet_tbl_pos_list = {'2', '3', '4', '5', '6'}
mp_vs_opp_3bet_tbl_pos_list = {'3', '4', '5', '6'}
co_vs_opp_3bet_tbl_pos_list = {'4', '5', '6'}
btn_vs_opp_3bet_tbl_pos_list = {'5', '6'}
sb_vs_opp_3bet_tbl_pos_list = '6'
vs_utg_rfi_list = '1'

co_vs_rfi_list = {'1', '2'}
btn_vs_rfi_list = {'1', '2', '3'}
sb_vs_rfi_list = {'1', '2', '3', '4'}
bb_vs_rfi_list = {'1', '2', '3', '4', '5'}

btn_cold_4bet_list = {'2', '3'}
sb_cold_4bet_list = {'2', '3', '4'}
bb_cold_4bet_list = {'2', '3', '4', '5'}
bb_cold_4bet_list2 = {'1', '3', '4'}

# utg_rfi_play_list = {'AA', 'KK', 'AKs', 'AQo', 'QQ', 'JJ', 'AKo', 'AJs', 'KQs', 'A5s', 'ATs', 'KTs', 'KJs', 'TT',
#                      'AQs', '99', '88', '77', '66', '55', 'QJs', 'JTs', 'T9s', '98s', '87s', '76s', '65s'}
# mp_rfi_play_list = {}
# co_rfi_play_list = {}
# btn_rfi_play_list = {}
# sb_rfi_play_list = {}
#################
# Scenario - RFI
#################
if pre_flop_scenario == "1":
    if my_table_position == "1":
        utg_rfi()
        while True:
            opponent_3bet = input('4. Did opponent 3Bet (1-Yes)? ')
            if opponent_3bet == opp_3_bet_response_list:
                break
            else:
                error_did_opp_3bet()
        while True:
            opponent_table_position = input("5. Enter opponent's table position (2-MP, 3-CO, 4-BTN, 5-SB, 6-BB): ")
            if opponent_table_position in utg_vs_opp_3bet_tbl_pos_list:
                break
            else:
                error_opp_tbl_pos()
        if opponent_3bet == "1":
            # UTG vs MP/CO 3Bet
            if opponent_table_position == "2" or opponent_table_position == "3":
                if hole_cards == "AA" or hole_cards == "KK" or hole_cards == "AKs":
                    pre_flop_action_4bet()
                elif hole_cards == "AQo":
                    pre_flop_action_raise_or_fold()
                elif (hole_cards == "QQ" or hole_cards == "JJ" or hole_cards == "AKo" or hole_cards == "AJs" or
                      hole_cards == "KQs"):
                    pre_flop_action_raise_or_call()
                elif hole_cards == "A5s" or hole_cards == "ATs" or hole_cards == "KTs" or hole_cards == "KJs":
                    pre_flop_action_raise_call_or_fold()
                elif hole_cards == "TT" or hole_cards == "AQs":
                    pre_flop_action_call()
                elif (hole_cards == "99" or hole_cards == "88" or hole_cards == "77" or hole_cards == "66" or
                      hole_cards == "55" or hole_cards == "QJs" or hole_cards == "JTs" or hole_cards == "T9s" or
                      hole_cards == "98s" or hole_cards == "87s" or hole_cards == "76s" or hole_cards == "65s"):
                    pre_flop_action_call_or_fold()
                else:
                    pre_flop_action_fold()

            # UTG vs BTN 3Bet
            elif opponent_table_position == "4":
                if hole_cards == "AA" or hole_cards == "KK" or hole_cards == "AKs":
                    pre_flop_action_4bet()
                elif hole_cards == "AQo":
                    pre_flop_action_raise_or_fold()
                elif (hole_cards == "QQ" or hole_cards == "JJ" or hole_cards == "AKo" or hole_cards == "AJs" or
                      hole_cards == "KJs" or hole_cards == "KQs"):
                    pre_flop_action_raise_or_call()
                elif hole_cards == "A5s" or hole_cards == "ATs" or hole_cards == "KTs":
                    pre_flop_action_raise_call_or_fold()
                elif hole_cards == "TT" or hole_cards == "AQs":
                    pre_flop_action_call()
                elif (hole_cards == "99" or hole_cards == "88" or hole_cards == "77" or hole_cards == "66" or
                      hole_cards == "55" or hole_cards == "A4s" or hole_cards == "QTs" or hole_cards == "QJs" or
                      hole_cards == "JTs" or hole_cards == "T9s" or hole_cards == "98s" or hole_cards == "87s" or
                      hole_cards == "76s" or hole_cards == "65s"):
                    pre_flop_action_call_or_fold()
                else:
                    pre_flop_action_fold()

            # UTG vs SB 3Bet
            elif opponent_table_position == "5":
                if hole_cards == "AA" or hole_cards == "KK" or hole_cards == "AKs":
                    pre_flop_action_4bet()
                elif hole_cards == "AQo" or hole_cards == "A9s":
                    pre_flop_action_raise_or_fold()
                elif (hole_cards == "QQ" or hole_cards == "JJ" or hole_cards == "AKo" or hole_cards == "AJs" or
                      hole_cards == "KJs" or hole_cards == "KQs"):
                    pre_flop_action_raise_or_call()
                elif hole_cards == "A5s" or hole_cards == "KTs":
                    pre_flop_action_raise_call_or_fold()
                elif hole_cards == "TT" or hole_cards == "AQs":
                    pre_flop_action_call()
                elif (hole_cards == "99" or hole_cards == "88" or hole_cards == "77" or hole_cards == "66" or
                      hole_cards == "55" or hole_cards == "A4s" or hole_cards == "QTs" or hole_cards == "QJs" or
                      hole_cards == "JTs" or hole_cards == "T9s" or hole_cards == "98s" or hole_cards == "87s" or
                      hole_cards == "76s" or hole_cards == "65s"):
                    pre_flop_action_call_or_fold()
                else:
                    pre_flop_action_fold()

            # UTG vs BB 3Bet
            elif opponent_table_position == "6":
                if hole_cards == "AA":
                    pre_flop_action_4bet()
                elif hole_cards == "A9s":
                    pre_flop_action_raise_or_fold()
                elif (hole_cards == "KK" or hole_cards == "AKo" or hole_cards == "AJs" or hole_cards == "AKs" or
                      hole_cards == "KJs"):
                    pre_flop_action_raise_or_call()
                elif hole_cards == "A4s" or hole_cards == "A5s" or hole_cards == "KTs":
                    pre_flop_action_raise_call_or_fold()
                elif (hole_cards == "QQ" or hole_cards == "JJ" or hole_cards == "TT" or hole_cards == "AQs" or
                      hole_cards == "KQs"):
                    pre_flop_action_call()
                elif (hole_cards == "99" or hole_cards == "88" or hole_cards == "77" or hole_cards == "66" or
                      hole_cards == "55" or hole_cards == "ATs" or hole_cards == "QJs" or hole_cards == "JTs" or
                      hole_cards == "T9s" or hole_cards == "87s" or hole_cards == "76s" or hole_cards == "65s"):
                    pre_flop_action_call_or_fold()
                else:
                    pre_flop_action_fold()

    # MP RFI
    elif my_table_position == "2":
        mp_rfi()
        while True:
            opponent_3bet = input('4. Did opponent 3Bet (1-Yes)? ')
            if opponent_3bet == opp_3_bet_response_list:
                break
            else:
                error_did_opp_3bet()
        while True:
            opponent_table_position = input("5. Enter opponent's table position (3-CO, 4-BTN, 5-SB, 6-BB): ")
            if opponent_table_position in mp_vs_opp_3bet_tbl_pos_list:
                break
            else:
                error_opp_tbl_pos()
        if opponent_3bet == "1":
            # MP vs CO 3Bet
            if opponent_table_position == "3":
                if (hole_cards == "AA" or hole_cards == "KK" or hole_cards == "QQ" or hole_cards == "AKo" or
                        hole_cards == "AKs" or hole_cards == "KJs"):
                    pre_flop_action_4bet()
                elif hole_cards == "KTs":
                    pre_flop_action_raise_or_fold()
                elif (hole_cards == "JJ" or hole_cards == "TT" or hole_cards == "AQo" or hole_cards == "AJs" or
                      hole_cards == "KQs"):
                    pre_flop_action_raise_or_call()
                elif hole_cards == "A5s" or hole_cards == "ATs":
                    pre_flop_action_raise_call_or_fold()
                elif hole_cards == "AQs":
                    pre_flop_action_call()
                elif (hole_cards == "99" or hole_cards == "88" or hole_cards == "77" or hole_cards == "66" or
                      hole_cards == "55" or hole_cards == "44" or hole_cards == "33" or hole_cards == "QJs" or
                      hole_cards == "JTs" or hole_cards == "T8s" or hole_cards == "T9s" or hole_cards == "98s" or
                      hole_cards == "87s" or hole_cards == "76s" or hole_cards == "65s" or hole_cards == "54s"):
                    pre_flop_action_call_or_fold()
                else:
                    pre_flop_action_fold()

            # MP vs BTN 3Bet
            elif opponent_table_position == "4":
                if (hole_cards == "AA" or hole_cards == "KK" or hole_cards == "QQ" or hole_cards == "AKo" or
                        hole_cards == "AKs" or hole_cards == "KTs" or hole_cards == "KJs"):
                    pre_flop_action_4bet()
                elif hole_cards == "A4s":
                    pre_flop_action_raise_or_fold()
                elif (hole_cards == "JJ" or hole_cards == "TT" or hole_cards == "AQo" or hole_cards == "AJs" or
                      hole_cards == "KQs"):
                    pre_flop_action_raise_or_call()
                elif hole_cards == "A5s" or hole_cards == "ATs":
                    pre_flop_action_raise_call_or_fold()
                elif hole_cards == "AQs":
                    pre_flop_action_call()
                elif (hole_cards == "99" or hole_cards == "88" or hole_cards == "77" or hole_cards == "66" or
                      hole_cards == "55" or hole_cards == "44" or hole_cards == "33" or hole_cards == "QJs" or
                      hole_cards == "JTs" or hole_cards == "T8s" or hole_cards == "T9s" or hole_cards == "98s" or
                      hole_cards == "87s" or hole_cards == "76s" or hole_cards == "65s" or hole_cards == "54s"):
                    pre_flop_action_call_or_fold()
                else:
                    pre_flop_action_fold()

            # MP vs SB 3Bet
            elif opponent_table_position == "5":
                if hole_cards == "AA" or hole_cards == "KK" or hole_cards == "AKs":
                    pre_flop_action_4bet()
                elif hole_cards == "AJo":
                    pre_flop_action_raise_or_fold()
                elif (hole_cards == "QQ" or hole_cards == "JJ" or hole_cards == "AQo" or hole_cards == "AKo" or
                      hole_cards == "AJs" or hole_cards == "KTs" or hole_cards == "KJs" or hole_cards == "KQs"):
                    pre_flop_action_raise_or_call()
                elif hole_cards == "A4s" or hole_cards == "A5s":
                    pre_flop_action_raise_call_or_fold()
                elif hole_cards == "TT" or hole_cards == "99" or hole_cards == "AQs":
                    pre_flop_action_call()
                elif (hole_cards == "88" or hole_cards == "77" or hole_cards == "66" or hole_cards == "55" or
                      hole_cards == "44" or hole_cards == "33" or hole_cards == "ATs" or hole_cards == "QTs" or
                      hole_cards == "QJs" or hole_cards == "JTs" or hole_cards == "T8s" or hole_cards == "T9s" or
                      hole_cards == "98s" or hole_cards == "87s" or hole_cards == "76s" or hole_cards == "65s" or
                      hole_cards == "54s"):
                    pre_flop_action_call_or_fold()
                else:
                    pre_flop_action_fold()

            # MP vs BB 3Bet
            elif opponent_table_position == "6":
                if hole_cards == "AA" or hole_cards == "KK" or hole_cards == "AKs":
                    pre_flop_action_4bet()
                elif hole_cards == "AQo" or hole_cards == "A9s" or hole_cards == "K9s":
                    pre_flop_action_raise_or_fold()
                elif (hole_cards == "AKo" or hole_cards == "A5s" or hole_cards == "ATs" or hole_cards == "KTs" or
                      hole_cards == "KJs"):
                    pre_flop_action_raise_or_call()
                elif hole_cards == "A4s":
                    pre_flop_action_raise_call_or_fold()
                elif (hole_cards == "QQ" or hole_cards == "JJ" or hole_cards == "TT" or hole_cards == "AJs" or
                      hole_cards == "AQs" or hole_cards == "KQs"):
                    pre_flop_action_call()
                elif (hole_cards == "99" or hole_cards == "88" or hole_cards == "77" or hole_cards == "66" or
                      hole_cards == "55" or hole_cards == "44" or hole_cards == "33" or hole_cards == "QTs" or
                      hole_cards == "QJs" or hole_cards == "JTs" or hole_cards == "T9s" or hole_cards == "98s" or
                      hole_cards == "87s" or hole_cards == "76s" or hole_cards == "65s" or hole_cards == "54s"):
                    pre_flop_action_call_or_fold()
                else:
                    pre_flop_action_fold()

    # CO RFI
    elif my_table_position == "3":
        co_rfi()
        while True:
            opponent_3bet = input('4. Did opponent 3Bet (1-Yes)? ')
            if opponent_3bet == opp_3_bet_response_list:
                break
            else:
                error_did_opp_3bet()
        while True:
            opponent_table_position = input("5. Enter opponent's table position (4-BTN, 5-SB, 6-BB): ")
            if opponent_table_position in co_vs_opp_3bet_tbl_pos_list:
                break
            else:
                error_opp_tbl_pos()
        if opponent_3bet == "1":
            # CO vs BTN 3Bet
            if opponent_table_position == "4":
                if (hole_cards == "AA" or hole_cards == "KK" or hole_cards == "QQ" or hole_cards == "JJ" or
                        hole_cards == "AKo" or hole_cards == "AKs"):
                    pre_flop_action_4bet()
                elif hole_cards == "AJo":
                    pre_flop_action_raise_or_fold()
                elif (hole_cards == "TT" or hole_cards == "AQo" or hole_cards == "ATs" or hole_cards == "AJs" or
                      hole_cards == "KTs" or hole_cards == "KJs" or hole_cards == "QJs"):
                    pre_flop_action_raise_or_call()
                elif (hole_cards == "A4s" or hole_cards == "A5s" or hole_cards == "KQo" or hole_cards == "K9s" or
                      hole_cards == "JTs"):
                    pre_flop_action_raise_call_or_fold()
                elif (hole_cards == "99" or hole_cards == "88" or hole_cards == "AQs" or hole_cards == "KQs" or
                      hole_cards == "87s" or hole_cards == "76s" or hole_cards == "65s" or hole_cards == "54s"):
                    pre_flop_action_call()
                elif (hole_cards == "77" or hole_cards == "66" or hole_cards == "55" or hole_cards == "44" or
                      hole_cards == "33" or hole_cards == "22" or hole_cards == "A9s" or hole_cards == "QTs" or
                      hole_cards == "T9s" or hole_cards == "98s"):
                    pre_flop_action_call_or_fold()
                else:
                    pre_flop_action_fold()
            # CO vs SB 3Bet
            elif opponent_table_position == "5":
                if hole_cards == "AA" or hole_cards == "KK" or hole_cards == "AKs":
                    pre_flop_action_4bet()
                elif hole_cards == "AJo" or hole_cards == "A8s":
                    pre_flop_action_raise_or_fold()
                elif (hole_cards == "QQ" or hole_cards == "JJ" or hole_cards == "AQo" or hole_cards == "AKo" or
                      hole_cards == "A5s" or hole_cards == "KTs"):
                    pre_flop_action_raise_or_call()
                elif (hole_cards == "A3s" or hole_cards == "A4s" or hole_cards == "A9s" or hole_cards == "KQo" or
                      hole_cards == "K9s"):
                    pre_flop_action_raise_call_or_fold()
                elif (hole_cards == "TT" or hole_cards == "99" or hole_cards == "88" or hole_cards == "ATs" or
                      hole_cards == "AJs" or hole_cards == "AQs" or hole_cards == "KJs" or hole_cards == "KQs" or
                      hole_cards == "QJs" or hole_cards == "JTs" or hole_cards == "87s" or hole_cards == "76s"):
                    pre_flop_action_call()
                elif (hole_cards == "77" or hole_cards == "66" or hole_cards == "55" or hole_cards == "44" or
                      hole_cards == "33" or hole_cards == "22" or hole_cards == "QTs" or hole_cards == "T9s" or
                      hole_cards == "98s" or hole_cards == "65s" or hole_cards == "54s"):
                    pre_flop_action_call_or_fold()
                else:
                    pre_flop_action_fold()
            # CO vs BB 3Bet
            elif opponent_table_position == "6":
                if hole_cards == "AA" or hole_cards == "KK" or hole_cards == "AKs":
                    pre_flop_action_4bet()
                elif hole_cards == "AJo":
                    pre_flop_action_raise_or_fold()
                elif (hole_cards == "QQ" or hole_cards == "AQo" or hole_cards == "AKo" or hole_cards == "A5s" or
                      hole_cards == "A9s"):
                    pre_flop_action_raise_or_call()
                elif (hole_cards == "A3s" or hole_cards == "A4s" or hole_cards == "A8s" or hole_cards == "KQo" or
                      hole_cards == "K9s"):
                    pre_flop_action_raise_call_or_fold()
                elif (hole_cards == "TT" or hole_cards == "99" or hole_cards == "88" or hole_cards == "ATs" or
                      hole_cards == "AJs" or hole_cards == "AQs" or hole_cards == "KJs" or hole_cards == "KQs" or
                      hole_cards == "QJs" or hole_cards == "JTs" or hole_cards == "87s" or hole_cards == "76s"):
                    pre_flop_action_call()
                elif (hole_cards == "88" or hole_cards == "77" or hole_cards == "66" or hole_cards == "55" or
                      hole_cards == "44" or hole_cards == "33" or hole_cards == "22" or hole_cards == "T9s" or
                      hole_cards == "98s" or hole_cards == "87s" or hole_cards == "65s" or hole_cards == "54s"):
                    pre_flop_action_call_or_fold()
                else:
                    pre_flop_action_fold()

    # BTN RFI
    elif my_table_position == "4":
        btn_rfi()
        while True:
            opponent_3bet = input('4. Did opponent 3Bet (1-Yes)? ')
            if opponent_3bet == opp_3_bet_response_list:
                break
            else:
                error_did_opp_3bet()
        while True:
            opponent_table_position = input("5. Enter opponent's table position (5-SB, 6-BB): ")
            if opponent_table_position in btn_vs_opp_3bet_tbl_pos_list:
                break
            else:
                error_opp_tbl_pos()
        # I'm BTN vs 3Bet
        if opponent_3bet == "1":
            # BTN vs SB 3Bet
            if opponent_table_position == "5":
                if hole_cards == "AA" or hole_cards == "KK" or hole_cards == "QQ" or hole_cards == "AKs":
                    pre_flop_action_4bet()
                elif hole_cards == "ATo" or hole_cards == "A6s" or hole_cards == "KJo" or hole_cards == "K5s":
                    pre_flop_action_raise_or_fold()
                elif (hole_cards == "JJ" or hole_cards == "TT" or hole_cards == "AJo" or hole_cards == "A4s" or
                      hole_cards == "A8s" or hole_cards == "A9s" or hole_cards == "KQo" or hole_cards == "K9s" or
                      hole_cards == "J9s" or hole_cards == "54s"):
                    pre_flop_action_raise_or_call()
                elif hole_cards == "A3s" or hole_cards == "A7s" or hole_cards == "Q9s":
                    pre_flop_action_raise_call_or_fold()
                elif (hole_cards == "99" or hole_cards == "88" or hole_cards == "77" or hole_cards == "66" or
                      hole_cards == "55" or hole_cards == "44" or hole_cards == "33" or hole_cards == "22" or
                      hole_cards == "AQo" or hole_cards == "A5s" or hole_cards == "ATs" or hole_cards == "AJs" or
                      hole_cards == "AQs" or hole_cards == "KTs" or hole_cards == "KJs" or hole_cards == "KQs" or
                      hole_cards == "QTs" or hole_cards == "QJs" or hole_cards == "JTs" or hole_cards == "T9s" or
                      hole_cards == "87s" or hole_cards == "76s" or hole_cards == "65s"):
                    pre_flop_action_call()
                elif (hole_cards == "K6s" or hole_cards == "K7s" or hole_cards == "K8s" or hole_cards == "T8s" or
                      hole_cards == "97s" or hole_cards == "98s"):
                    pre_flop_action_call_or_fold()
                else:
                    pre_flop_action_fold()
            # BTN vs BB 3Bet
            elif opponent_table_position == "6":
                if (hole_cards == "AA" or hole_cards == "KK" or hole_cards == "QQ" or hole_cards == "AKo" or
                        hole_cards == "AKs"):
                    pre_flop_action_4bet()
                elif hole_cards == "ATo" or hole_cards == "A2s" or hole_cards == "K5s":
                    pre_flop_action_raise_or_fold()
                elif (hole_cards == "JJ" or hole_cards == "AJo" or hole_cards == "A4s" or hole_cards == "A7s" or
                      hole_cards == "A8s" or hole_cards == "KQo" or hole_cards == "T8s"):
                    pre_flop_action_raise_or_call()
                elif hole_cards == "A3s" or hole_cards == "A6s" or hole_cards == "KJo" or hole_cards == "Q9s":
                    pre_flop_action_raise_call_or_fold()
                elif (hole_cards == "TT" or hole_cards == "99" or hole_cards == "88" or hole_cards == "77" or
                      hole_cards == "66" or hole_cards == "AQo" or hole_cards == "A5s" or hole_cards == "A9s" or
                      hole_cards == "ATs" or hole_cards == "AJs" or hole_cards == "AQs" or hole_cards == "K9s" or
                      hole_cards == "KTs" or hole_cards == "KJs" or hole_cards == "KQs" or hole_cards == "QTs" or
                      hole_cards == "QJs" or hole_cards == "J9s" or hole_cards == "JTs" or hole_cards == "T9s" or
                      hole_cards == "87s"):
                    pre_flop_action_call()
                elif (hole_cards == "K6s" or hole_cards == "K7s" or hole_cards == "K8s" or hole_cards == "76s" or
                      hole_cards == "65s" or hole_cards == "54s"):
                    pre_flop_action_call_or_fold()
                else:
                    pre_flop_action_fold()

    # SB RFI
    elif my_table_position == "5":
        sb_rfi()
        while True:
            opponent_3bet = input('4. Did the Big Blind 3Bet (1-Yes)? ')
            if opponent_3bet == opp_3_bet_response_list:
                break
            else:
                error_did_opp_3bet()
        if opponent_3bet == "1":
            if (hole_cards == "AA" or hole_cards == "KK" or hole_cards == "QQ" or hole_cards == "JJ" or
                    hole_cards == "TT" or hole_cards == "ATo" or hole_cards == "AJo" or hole_cards == "AKo" or
                    hole_cards == "AQs" or hole_cards == "AKs"):
                pre_flop_action_4bet()
            elif hole_cards == "A2s":
                pre_flop_action_raise_or_fold()
            elif (hole_cards == "AQo" or hole_cards == "A3s" or hole_cards == "A4s" or hole_cards == "KJo" or
                  hole_cards == "KQo"):
                pre_flop_action_raise_or_call()
            elif hole_cards == "K6s" or hole_cards == "QJo":
                pre_flop_action_raise_call_or_fold()
            elif (hole_cards == "99" or hole_cards == "88" or hole_cards == "77" or hole_cards == "66" or
                  hole_cards == "55" or hole_cards == "A5s" or hole_cards == "A6s" or hole_cards == "A7s" or
                  hole_cards == "A8s" or hole_cards == "A9s" or hole_cards == "ATs" or hole_cards == "AJs" or
                  hole_cards == "K8s" or hole_cards == "K9s" or hole_cards == "KTs" or hole_cards == "KJs" or
                  hole_cards == "KQs" or hole_cards == "Q9s" or hole_cards == "QTs" or hole_cards == "QJs" or
                  hole_cards == "J9s" or hole_cards == "JTs" or hole_cards == "T8s" or hole_cards == "T9s"):
                pre_flop_action_call()
            elif (hole_cards == "44" or hole_cards == "33" or hole_cards == "22" or hole_cards == "K7s" or
                  hole_cards == "Q8s" or hole_cards == "J8s" or hole_cards == "98s" or hole_cards == "87s" or
                  hole_cards == "76s" or hole_cards == "65s" or hole_cards == "54s"):
                pre_flop_action_call_or_fold()
            else:
                pre_flop_action_fold()

####################
# Scenario - vs RFI
####################
elif pre_flop_scenario == "2":
    if my_table_position == "2":
        mp_vs_utg_rfi()
    elif my_table_position == "3":
        while True:
            opponent_table_position = input("4. Enter opponent's table position (1-UTG, 2-MP): ")
            if opponent_table_position in co_vs_rfi_list:
                break
            else:
                error_opp_tbl_pos()
        if opponent_table_position == "1":
            co_vs_utg_rfi()
        elif opponent_table_position == "2":
            co_vs_mp_rfi()
    elif my_table_position == "4":
        while True:
            opponent_table_position = input("4. Enter opponent's table position (1-UTG, 2-MP, 3-CO): ")
            if opponent_table_position in btn_vs_rfi_list:
                break
            else:
                error_opp_tbl_pos()
        if opponent_table_position == "1":
            btn_vs_utg_rfi()
        elif opponent_table_position == "2":
            btn_vs_mp_rfi()
        elif opponent_table_position == "3":
            btn_vs_co_rfi()
    elif my_table_position == "5":
        while True:
            opponent_table_position = input("4. Enter opponent's table position (1-UTG, 2-MP, 3-CO, 4-BTN): ")
            if opponent_table_position in sb_vs_rfi_list:
                break
            else:
                error_opp_tbl_pos()
        if opponent_table_position == "1":
            sb_vs_utg_rfi()
        elif opponent_table_position == "2":
            sb_vs_mp_rfi()
        elif opponent_table_position == "3":
            sb_vs_co_rfi()
        elif opponent_table_position == "4":
            sb_vs_btn_rfi()
    elif my_table_position == "6":
        while True:
            opponent_table_position = input("4. Enter opponent's table position (1-UTG, 2-MP, 3-CO, 4-BTN, 5-SB): ")
            if opponent_table_position in bb_vs_rfi_list:
                break
            else:
                error_opp_tbl_pos()
        if opponent_table_position == "1":
            bb_vs_utg_rfi()
        elif opponent_table_position == "2":
            bb_vs_mp_rfi()
        elif opponent_table_position == "3":
            bb_vs_co_rfi()
        elif opponent_table_position == "4":
            bb_vs_btn_rfi()
        elif opponent_table_position == "5":
            bb_vs_sb_rfi()

######################
# Scenario - Cold 4Bet
######################
elif pre_flop_scenario == "3":

    if my_table_position == "3":  # I'M CO
        cold_4bet_co_vs_mp_3bet()

    elif my_table_position == "4":  # I'M BTN
        while True:
            cold_4bet_question1 = input("4. Which opponent 3Bet (2-MP, 3-CO)? ")
            if cold_4bet_question1 in btn_cold_4bet_list:
                break
            else:
                error_opp_tbl_pos()
        if cold_4bet_question1 == "2":
            cold_4bet_btn_vs_mp_3bet()
        elif cold_4bet_question1 == "3":
            cold_4bet_btn_vs_co_3bet()

    elif my_table_position == "5":  # I'M SB
        while True:
            cold_4bet_question1 = input("4. Which opponent 3Bet (2-MP, 3-CO, 4-BTN)? ")
            if cold_4bet_question1 in sb_cold_4bet_list:
                break
            else:
                error_opp_tbl_pos()
        if cold_4bet_question1 == "2":
            cold_4bet_sb_vs_mp_3bet()
        elif cold_4bet_question1 == "3":
            cold_4bet_sb_vs_co_3bet()
        elif cold_4bet_question1 == "4":
            cold_4bet_sb_vs_btn_3bet()

    elif my_table_position == "6":  # I'M BB
        while True:
            cold_4bet_question1 = input("4. Which opponent 3Bet (2-MP, 3-CO, 4-BTN, 5-SB)? ")
            if cold_4bet_question1 in bb_cold_4bet_list:
                break
            else:
                error_opp_tbl_pos()
        if cold_4bet_question1 == "2":
            cold_4bet_bb_vs_mp_3bet()
        elif cold_4bet_question1 == "3":
            cold_4bet_bb_vs_co_3bet()
        elif cold_4bet_question1 == "4":
            cold_4bet_bb_vs_btn_3bet()
        elif cold_4bet_question1 == "5":
            while True:
                cold_4bet_question2 = input("5. Which opponent open-raised (1-UTG/MP, 3-CO, 4-BTN)? ")
                if cold_4bet_question2 in bb_cold_4bet_list2:
                    break
                else:
                    error_opp_tbl_pos()
            if cold_4bet_question2 == "1":
                cold_4bet_bb_vs_sb_3bet_utg_or_mp_open()
            elif cold_4bet_question2 == "3":
                cold_4bet_bb_vs_sb_3bet_co_open()
            elif cold_4bet_question2 == "4":
                cold_4bet_bb_vs_sb_3bet_btn_open()
