from jmapc import Client, fastmail as fastmail


def generate_masked_email(description, domain, jmap_api_key, jmap_host, prefix):
    method = fastmail.MaskedEmailSet(
        create=dict(
            create=fastmail.MaskedEmail(
                description=description,
                for_domain=domain,
                email_prefix=prefix,
            )
        )
    )
    client = Client.create_with_api_token(
        host=jmap_host, api_token=jmap_api_key
    )
    result: fastmail.MaskedEmailSetResponse = client.request(method)
    email = result.created["create"].email
    return email
