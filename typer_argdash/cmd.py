import typer

cli = typer.Typer()


@cli.command()
def first(a: str, b: str, c: bool = False):
    typer.secho(f"{a=} {b=} {c=}")


@cli.command()
def second(a: str, b: str, c: bool = False):
    typer.secho(f"{a=} {b=} {c=}")
