from collections.abc import Callable, Iterable
from shutil import get_terminal_size
from time import sleep


def clear_terminal() -> None:
    print("\n".join(["" for _ in range(get_terminal_size()[1])]))


def press_enter_to_continue() -> None:
    print()
    print("PRESS ENTER TO CONTINUE")
    input()
    clear_terminal()


def validated_input(
    prompt: str, predicate: Callable[[str], bool], user_input_prefix: str = "> "
) -> str:
    while True:
        print(prompt)
        raw_input = input(user_input_prefix)
        print()
        if predicate(raw_input):
            return raw_input
        print("INVALID, PLEASE TRY AGAIN")


def yes_no_input(prompt: str, user_input_prefix: str = "> ") -> bool:
    return (
        validated_input(
            prompt, lambda b: b in frozenset({"y, n", "Y", "N"}), user_input_prefix
        ).upper()
        == "Y"
    )


def print_loading_ellipsis() -> None:
    sleep(1)
    print_line_sequence(LOADING_ELLIPSIS)


LOADING_ELLIPSIS = (".", "..", "...", "")


def print_line_sequence(
    line_sequence: Iterable[str | Iterable[str]], trailing_sleep: bool = True
) -> None:
    i = iter(line_sequence)
    print(next(i))
    for line in i:
        if not isinstance(line, str):
            for sub_line in line:
                print(sub_line)
        else:
            sleep_and_print_line(line)
    if trailing_sleep:
        sleep(1)


def sleep_and_print_line(line: str) -> None:
    if not line.isspace():
        sleep(1)
    print(line)


if __name__ == "__main__":

    print_line_sequence(
        (
            "Line 1",
            "Line 2",
            "Line 3 with newline",
            "",
            ("Extra long", "line that", "prints at once"),
            "And that's all",
        )
    )
