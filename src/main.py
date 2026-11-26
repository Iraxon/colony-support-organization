from time import sleep

from tasks import weather_task
from terminal_utils import (
    LOADING_ELLIPSIS,
    clear_terminal,
    press_enter_to_continue,
    print_line_sequence,
    print_loading_ellipsis,
    validated_input,
)


def intro() -> str:
    """
    Play the intro and return the user's
    username
    """

    clear_terminal()
    print_line_sequence(("CSO AEGIS v1.0.0", "(C) CSO 2056", "", "WELCOME OPERATOR"))

    username = validated_input("PLEASE ENTER USERNAME", lambda u: u.isalnum())
    sleep(1)

    print_line_sequence(
        (
            "CHECKING DEVICE PASSKEY",
            *LOADING_ELLIPSIS,
            ("DEVICE PASSKEY ACCEPTED", f"WELCOME {username}"),
        )
    )
    press_enter_to_continue()

    return username


username = intro()
tasks = (("RECORD WEATHER DATA", weather_task),)
while True:
    # Main menu
    print_line_sequence(
        (
            "TO-DO:",
            "",
            *(
                f"{i + 1} :: {task_description}"
                for i, (task_description, _) in enumerate(tasks)
            ),
            "",
        )
    )
    task_index = (
        int(
            validated_input(
                "ENTER A TASK NUMBER TO PROCEED",
                lambda s: len(s) == 1 and s.isnumeric() and 0 < int(s) <= len(tasks),
            )
        )
        - 1
    )
    sleep(1)
    print("TASK SELECTED")
    sleep(1)
    print("CONNECTING")
    print_loading_ellipsis()
    print("CONNECTED")
    press_enter_to_continue()

    _, task_subroutine = tasks[task_index]
    task_subroutine()
