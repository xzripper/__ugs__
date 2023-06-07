class Types:
    BALLISTIC = 'BALLISTIC'
    MISSILE_CARRIER = 'MC'
    MIG = 'MIG'
    KAB = 'KAB'
    ROCKET = 'ROCKET'
    UAV = 'UAV'
    X = 'X'
    STRAT_BOMBER = 'SB'
    CALIBER = 'CALIBER'
    KILLJOY = 'KILLJOY'
    ARTILLERY = 'ARTILLERY'
    UNKNOWN = 'UNKNOWN'

    HANG_UP = 'HANG_UP'

class States:
    POSITIVE = 'POSITIVE'
    NEGATIVE = 'NEGATIVE'
    UNKNOWN = 'UNKNOWN'

class Codes:
    POSITIVE_BALLISTIC = 0x8
    NEGATIVE_BALLISTIC = 0x16
    POSITIVE_MC = 0x32
    NEGATIVE_MC = 0x48
    POSITIVE_MIG = 0x64
    NEGATIVE_MIG = 0x128
    POSITIVE_KAB = 0x256
    NEGATIVE_KAB = 0x512
    POSITIVE_ROCKET = 0x1024
    NEGATIVE_ROCKET = 0x2048
    POSITIVE_UAV = 0x4096
    NEGATIVE_UAV = 0x8192
    POSITIVE_X = 0x16384
    NEGATIVE_X = 0x32768
    POSITIVE_SB = 0x65536
    NEGATIVE_SB = 0x131072
    POSITIVE_CALIBER = 0x262144
    NEGATIVE_CALIBER = 0x524288
    POSITIVE_KILLJOY = 0x1048576
    NEGATIVE_KILLJOY = 0x2097152
    POSITIVE_ARTILLERY = 0x4194304
    NEGATIVE_ARTILLERY = 0x8388608

    HANG_UP = -1

KEYWORDS = ['ракетонос', 'міг', 'балістичн', 'балісти', 'каб', 'ракета', 'бпла', 'x-101', 'x-555', 'ту-', 'калібр', 'кинджал', 'артобстріл']
STATES_POSITIVE = ['не виявлено', 'не зафіксовано', 'відбій', 'відбою', 'наразі минула']
STATES_NEGATIVE = ['зліт', 'загроза', 'загроза застосування', 'відмічено пуски', 'заходять', 'пуск', 'пускових позицій', 'артобстріл']

alerts = ['відбій', 'повітряна', 'повітряна тривога']

alert_msg = 'Повітряна тривога у $region.'
alert_hang_up_msg = 'Відбій тривоги у $region.'

OUT_MSGS = {
    Codes.POSITIVE_BALLISTIC: 'Відбій застосування баллістики.',
    Codes.NEGATIVE_BALLISTIC: 'Загроза застосування баллістики.',
    Codes.POSITIVE_MC: 'Відбій застосування ракетоносіів.',
    Codes.NEGATIVE_MC: 'Загроза застосування ракетоносіів.',
    Codes.POSITIVE_MIG: 'Відбій застосування літаків "МІГ".',
    Codes.NEGATIVE_MIG: 'Загроза застосування літаків "МІГ".',
    Codes.POSITIVE_KAB: 'Відбій застосування КАБ.',
    Codes.NEGATIVE_KAB: 'Загроза застосування КАБ.',
    Codes.POSITIVE_ROCKET: 'Відбій застосування ракет(?).',
    Codes.NEGATIVE_ROCKET: 'Загроза застосування ракет(?).',
    Codes.POSITIVE_UAV: 'Відбій застосування БпЛА.',
    Codes.NEGATIVE_UAV: 'Загроза застосування БпЛА.',
    Codes.POSITIVE_X: 'Відбій застосування X-101/555.',
    Codes.NEGATIVE_X: 'Загроза застосування X-101/555.',
    Codes.POSITIVE_SB: 'Відбій застосування стратегічних бомбардувальників.',
    Codes.NEGATIVE_SB: 'Загроза застосування стратегічних бомбардувальників.',
    Codes.POSITIVE_CALIBER: 'Відбій застосування Калібрів.',
    Codes.NEGATIVE_CALIBER: 'Загроза застосування Калібрів.',
    Codes.POSITIVE_KILLJOY: 'Відбій застосування Кинджалів.',
    Codes.NEGATIVE_KILLJOY: 'Загроза застосування Кинджалів.',
    Codes.POSITIVE_ARTILLERY: 'Відбій артобстрілу.',
    Codes.NEGATIVE_ARTILLERY: 'Загроза артобстрілу.',
    Codes.HANG_UP: 'Відбій тривоги.'
}

ukrainian_regions = [
    'воли', 'волинська', 'волинь',
    'рівне', 'рівненська',
    'житомир', 'житомирська',
    'киів', 'київ', 'киівська', 'м київ', 'м. київ',
    'чернігів', 'чернігівська', 'чернігівщина',
    'суми', 'сумська', 'сумщина',
    'харків', 'харківська',
    'луганськ', 'луганщина',
    'донецьк', 'донеччина',
    'запоріжжя', 'запорізька',
    'херсон', 'херсонська', 'херсонщина',
    'крим', 'ар крим', 'ар. крим', 'севастополь',
    'миколаів', 'миколаівська', 'миколаївська', 'миколаївщина',
    'одесса', 'одеса', 'одещина', 'одеська',
    'кіровоград', 'кропивницький',
    'полтава', 'полтавщина',
    'черкаси', 'черкаська', 'черкащина',
    'вінниця', 'вінницька',
    'хмельницьк', 'хмельницька',
    'чернівецька',
    'тернопіль', 'тернопільщина', 'тернопільська',
    'львів', 'львівська', 'львівщина',
    'івано-франківськ', 'івано франківськ',
    'закарпатська', 'закарпатщина'
]

def analyze_rocket_alert(info):
    info = info.lower()

    _type = ...
    _state = ...
    _region = 'Загально'

    if KEYWORDS[0] in info: _type = Types.MISSILE_CARRIER
    elif KEYWORDS[1] in info: _type = Types.MIG
    elif KEYWORDS[2] in info or KEYWORDS[3] in info: _type = Types.BALLISTIC
    elif KEYWORDS[4] in info: _type = Types.KAB
    elif KEYWORDS[5] in info: _type = Types.ROCKET
    elif KEYWORDS[6] in info: _type = Types.UAV
    elif KEYWORDS[7] in info or KEYWORDS[8] in info: _type = Types.X
    elif KEYWORDS[9] in info: _type = Types.STRAT_BOMBER
    elif KEYWORDS[10] in info: _type = Types.CALIBER
    elif KEYWORDS[11] in info: _type = Types.KILLJOY
    elif KEYWORDS[12] in info: _type = Types.ARTILLERY

    if any(pos_state in info for pos_state in STATES_POSITIVE): _state = States.POSITIVE
    elif any(neg_state in info for neg_state in STATES_NEGATIVE): _state = States.NEGATIVE

    for _reg in ukrainian_regions:
        if _reg in info:
            _region = _reg.capitalize()

    if _type == ... and _state == States.POSITIVE:
        return (OUT_MSGS[Codes.HANG_UP], _state, _region)

    elif _type == ... or _state == ...:
        return None

    else:
        return (eval(f'OUT_MSGS[Codes.{_state}_{_type}]'), _state, _region) # Refactor this in future.

def analyze_alert(info):
    info = info.lower()

    _region = ...

    for _reg in ukrainian_regions:
        if _reg in info:
            _region = _reg.capitalize()

    if alerts[0] in info:
        if _region != ...:
            return (alert_hang_up_msg.replace('$region', _region.capitalize()), True)

        else:
            return None

    elif alerts[1] in info or alerts[2] in info:
        if _region != ...:
            return (alert_msg.replace('$region', _region.capitalize()), False)

        else:
            return None

    else:
        return None
