import re

# В этом списке собираются подстроки для проверки через in
from typing import List, Any

bad_line_parts = [
    'Standby redo logfile selected for thread'
]
bad_reg_exprs = [
    re.compile('[A-Z][a-z]{2} [A-Z][a-z]{2} \d{1,2} \d\d:\d\d:\d\d \d{4}'),
    # здесь дополнить другими регулярными выражениями, если потребуется
]


def is_fine_line(line):
    return (not any(bad_line_part in line
                    for bad_line_part in bad_line_parts) and
            not any(bad_reg_expr.match(line)
                    for bad_reg_expr in bad_reg_exprs))


def openning(message):
    with open(message, 'r') as log_file:
        for line in log_file.readlines():
            if is_fine_line(line):
               print(line)