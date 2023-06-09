import whois
def domain_lookup(domain):
    try:
        w = whois.whois(domain)
        print("Domain Information:")
        print("Name:", w.name)
        print("Registrar:", w.registrar)
        print("Creation Date:", w.creation_date)
        print("Expiration Date:", w.expiration_date)
        print("Last Updated:", w.updated_date)
        print("Name Servers:", w.name_servers)
        print("Status:", w.status)
    except whois.parser.PywhoisError as e:
        print("Error:", str(e))

# Example usage
domain_name = input("Enter a domain name: ")
domain_lookup(domain_name)
