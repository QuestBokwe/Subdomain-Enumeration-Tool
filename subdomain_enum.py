import socket

def subdomain_enumerator(domain, wordlist_file):
    """Brute-force subdomains of a given domain using a wordlist."""
    found = []
    with open(wordlist_file) as f:
        for sub in f:
            sub = sub.strip()
            subdomain = sub + "." + domain
            try:
                socket.gethostbyname(subdomain)
                print(f"[+] {subdomain}")
                found.append(subdomain)
            except socket.gaierror:
                pass
    return found

# Main code
if __name__ == "__main__":
    domain = input("Enter a domain (without www.): ")
    wordlist_file = "subdomains.txt"

    print(f"Starting subdomain enumeration for {domain}")
    subdomains = subdomain_enumerator(domain, wordlist_file)

    print("Done.")
    print(f"We found {len(subdomains)} subdomains.")
