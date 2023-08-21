import click
import robin_stocks as rh

@click.group()
def main():
    print("hello from main")
@main.command()
def quote(symbols):
    for symbol in symbols:
        print("getting a stock quote for symbol {}".format(symbol))

if __name__ == '__main__':
    main()
