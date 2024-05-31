import typer

from typer_argdash.cmd import cli as cmdcli
from typer_argdash.utils import config_logging

cli = typer.Typer(
    pretty_exceptions_show_locals=False,
    pretty_exceptions_short=True,
    pretty_exceptions_enable=False,
)
cli.add_typer(cmdcli, name="command")


@cli.callback()
def main(
    verbose: int = typer.Option(
        1,
        "--verbose",
        "-v",
        count=True,
    ),
) -> None:
    config_logging(verbose)


@cli.command()
def tlcommand(really: bool = True):
    typer.secho(f"{really=}")
