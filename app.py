import click

from scanner.scanner import client_connection

import click

@click.command()
@click.option('--ip_address', prompt='Enter the target IP address')
@click.option('--starting_port', prompt='Enter starting port number')
@click.option('--ending_port', prompt='Enter the ending port number')
def scan(ip_address,starting_port,ending_port):
    
    client_connection(
        ip_address,
        (int(starting_port),
         int(ending_port)
        )
    )

if __name__ == '__main__':
    scan()