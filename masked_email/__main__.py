import pyperclip
import typer
import uvicorn

from masked_email.core import generate_masked_email

app = typer.Typer()


@app.command("generate")
def cmd_generate(
        description: str = typer.Option(default=None),
        jmap_host: str = typer.Option(envvar="JMAP_HOST", prompt=True),
        jmap_api_key: str = typer.Option(envvar="JMAP_API_KEY", prompt=True),
        copy: bool = typer.Option(envvar="MASKED_EMAIL_COPY_ALWAYS", default=False, is_flag=True),
        domain: str = typer.Option(envvar="MASKED_EMAIL_DOMAIN", default=None),
        prefix: str = typer.Option(envvar="MASKED_EMAIL_PREFIX", default=None),
):
    email = generate_masked_email(description, domain, jmap_api_key, jmap_host, prefix)
    if copy:
        pyperclip.copy(email)
        typer.echo(f"Created masked email: {email} and copied to clipboard.")
    else:
        typer.echo(f"Created masked email: {email}. ")


@app.command("server")
def run_server(host: str = typer.Option(envvar="ME_SERVER_HOST", default="0.0.0.0"),
               port: int = typer.Option(envvar="ME_SERVER_PORT", default=8000)):
    uvicorn.run("masked_email.server:app", host=host, port=port, reload=False,
                workers=2, limit_concurrency=2, limit_max_requests=1)


if __name__ == "__main__":
    app()
