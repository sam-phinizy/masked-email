import jmapc.fastmail as fastmail
import pyperclip
import typer
from jmapc import Client

app = typer.Typer()


@app.command("generate")
def cmd_generate(
        description: str = typer.Option(default=None),
        jmap_host: str = typer.Option(envvar="JMAP_HOST", prompt=True),
        jmap_api_key: str = typer.Option(envvar="JMAP_API_KEY", prompt=True),
        copy: bool = typer.Option(envvar="MASKED_EMAIL_COPY_ALWAYS", default=False, is_flag=True),
):
    method = fastmail.MaskedEmailSet(
        create=dict(
            create=fastmail.MaskedEmail(
                id=None,
                description=description,

            )
        )
    )
    client = Client.create_with_api_token(
        host=jmap_host, api_token=jmap_api_key
    )
    result: fastmail.MaskedEmailSetResponse = client.request(method)

    email = result.created["create"].email

    if copy:
        pyperclip.copy(email)
        typer.echo(f"Created masked email: {email} and copied to clipboard.")
    else:
        typer.echo(f"Created masked email: {email}. ")


if __name__ == "__main__":
    app()
