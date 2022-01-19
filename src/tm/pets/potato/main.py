from time import sleep
from timeit import default_timer as timer

import click as click
from playsound import playsound
from rich.progress import Progress
_DEFAULT_TIME_SEC = 20 * 60


@click.command()
@click.option('--time', default=_DEFAULT_TIME_SEC, help='time in second')
def startPomodoro(time):
    with Progress() as progress:
        task1 = progress.add_task("[green]Progress: ", total=time)
        start = timer()
        while not progress.finished:
            progress.update(task1, completed=timer() - start)
            sleep(1)
    playsound('alarm.wav')


if __name__ == '__main__':
    startPomodoro()
