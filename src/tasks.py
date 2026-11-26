from enum import Enum, auto
from random import random
from time import sleep

from terminal_utils import (
    LOADING_ELLIPSIS,
    press_enter_to_continue,
    print_line_sequence,
    yes_no_input,
)


class TaskResult(Enum):
    SUCCESS = auto()

    FRIVOLOUS_REPORT = auto()
    ANOMALY_STOPPED_BY_REPORT = auto()

    ANOMALY_INSTANT_VICTORY = auto()
    ANOMALY_PASSED_MINOR = auto()
    ANOMALY_PASSED_CATASTROPHIC = auto()


def weather_task(infohazard_chance: float = 0.05) -> TaskResult:

    infohazard = infohazard_chance > 0 and random() < infohazard_chance

    if infohazard:
        return weather_task_fallback_connection()

    print_line_sequence(
        ("DATA RECEIVED", "", "CONTRIBUTING COLONIES: 35", "DATA SIZE: 17 KB", "")
    )

    choice = yes_no_input("SEND TO CSO METEOROLOGY DEPARTMENT? (Y/N)")
    sleep(1)

    if choice:
        print_line_sequence(("SENDING DATA", *LOADING_ELLIPSIS, "DATA SENT"))
        result = TaskResult.SUCCESS
    else:
        print_line_sequence(
            (
                "DATA WITHHELD",
                "REPORTING SUSPICIOUS DATA TO DEPARTMENT OF ANOMALIES",
                *LOADING_ELLIPSIS,
                "REPORT SENT",
            )
        )
        result = TaskResult.FRIVOLOUS_REPORT
    press_enter_to_continue()
    return result


# It is named like this for immersion in the traceback
# when the game crashes itself for failed task
def GOODBYE() -> TaskResult:
    print_line_sequence(
        ("DATA RECEIVED", "", "CONTRIBUTING COLONIES: 01", "DATA SiZE: 241 KL", "")
    )

    choice = yes_no_input("SEND TO CSO METEOROLOGY DEPARTMENT? (Y/N)")
    sleep(1)

    if choice:
        print_line_sequence(
            (
                "SENDING DATA",
                *LOADING_ELLIPSIS,
                "DATA? SENT",
                "Thank you for your assistance, mortal.",
                "Your services",
                "Are required",
                "No longer.",
            )
        )
        sleep(3)
        raise ConnectionError(
            "The connection to the CSO Central Server was terminated: Server stopped responding."
        )
    else:
        print_line_sequence(
            (
                "DATA WITHHELD",
                "REPORTING SUSPICIOUS DATA TO DEPARTMENT OF ANOMALIES",
                *LOADING_ELLIPSIS,
                "REPORT SENT",
            )
        )
        press_enter_to_continue()
        return TaskResult.ANOMALY_STOPPED_BY_REPORT


# More innocious alias to appear in the other part of the traceback
weather_task_fallback_connection = GOODBYE
