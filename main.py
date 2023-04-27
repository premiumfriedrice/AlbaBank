import click
from src.db import createUserTable, seedUserTable
from src.app import App


@click.group()
def main():
    pass

@main.command()
def init_db():
    createUserTable()
    seedUserTable()
    
@main.command()
def run():
    app = App()
    app.mainloop()


if __name__ == '__main__':
    main()
