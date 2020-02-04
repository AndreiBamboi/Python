import sys
from math import log
DIGIT_MAP = {
    'zero': '0',
    'one': '1',
    'two': '2',
    'three': '3'
}
def convert(s):
    x=-1
    try:
        number = ''
        for token in s:
            number += DIGIT_MAP[token]
        return int(number)
        # x = int(number)
        print(f"Duten in plm de x={x}")
    # except KeyError:
    #     x =-1
    #     print("Ai facut un mare kkt")
    # except TypeError:
    #     print("We da chiar esti roopt")
    #     x=-1
    except(KeyError, TypeError) as e:
        # print("Scrie cod k lumea rooptule")
        print(f"Eroare de conversie: {e!r}",
              file=sys.stderr)
        raise
        # returne
    # return x


def string_log(s):
    v = convert(s)
    return log(v)
