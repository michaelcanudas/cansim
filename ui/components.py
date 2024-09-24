def get_text(prompt: str) -> str:
    put_text("{}: ".format(prompt))
    return input()


def get_select(options: list[str]) -> str:
    print("\n".join(
        ["  ({}) {}".format(i, options[i]) for i in range(0, len(options))]
    ), end="\n\n")

    return get_text("response (number)")


def put_text(content: str):
    print(content, end="")


def put_head(content: str):
    print("# {} #".format(content), end="\n\n")