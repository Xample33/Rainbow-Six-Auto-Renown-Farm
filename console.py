from rich import print as rprint
from rich import box
from rich.align import Align
from rich.layout import Layout
from rich.panel import Panel, Text
from rich.table import Table
from rich.live import Live

from time import sleep

class RichTerminalUpdater:
    
    UPDATE_DELAY = 0.2
    
    def __init__(self, rainbow_six_bot) -> None:
        self.rainbow_six_bot = rainbow_six_bot
        self.layout = self.make_layout()
        self.live = Live(self.layout, transient=True, auto_refresh=False)
        
    def make_layout(self) -> Layout:
        layout = Layout(name="root")

        layout.split(
            Layout(name="header", size=3),
            Layout(name="main", ratio=1)
        )
        layout["main"].split_row(
            Layout(name="left"),
            Layout(name="right", ratio=2, minimum_size=60),
        )
        layout["main"]["right"].split_column(
            Layout(name="top", ratio=2),
            Layout(name="bottom", ratio=1)
        )
        return layout

    def header(self):
        grid = Table.grid(expand=True)
        grid.add_column(justify="center", ratio=1)
        grid.add_column(justify="right")
        
        grid.add_row(
            '[b]Rainbow Six Auto Renown Farm [white]by Xample33',
            f'[bold green]v{self.rainbow_six_bot.version}'
        )
        return Panel(grid, style="gold3")

    def left(self) -> Panel:
        grid = Table.grid(padding=(1,1,1,1), pad_edge=True)
        grid.add_column(justify='left')
        
        grid.add_row('Status: ',f'[green]{self.rainbow_six_bot.status_text}')
        grid.add_row('Resolution: ',f'[cyan]{self.rainbow_six_bot.display_size}')
        grid.add_row('Match count: ',f'[yellow]{self.rainbow_six_bot.match_count}')
        grid.add_row('Start time: ',f'[magenta]{self.rainbow_six_bot.start_time}')
        grid.add_row('Loop count: ',f'[blue]{self.rainbow_six_bot.loop_count}/300')

        panel = Panel(
            Align.left((grid)),
            box=box.ROUNDED,
            border_style="white"  # Change border style and color
        )

        return panel
    
    def right_top(self) -> Panel:
        grid = Table.grid(padding=(1,1,1,1), pad_edge=True)
        grid.add_column(justify='left')
        
        grid.add_row('Version: ', f'{self.rainbow_six_bot.version_status}')
        
        grid.add_row('Exit: ', 'Press [bold cyan]\[ctrl + c][/bold cyan] to exit.') if self.rainbow_six_bot.require_stop == False else None
        
        if self.rainbow_six_bot.require_stop == True:
            grid.add_row('[bold red]Error: ', f'[bold red]{self.rainbow_six_bot.detailed_error}')
            grid.add_row('', 'Press enter or close the window to exit.')
            grid.add_row('', '[bold italic]If you think this is a bug, please report it on GitHub.')

        message_panel = Panel(
            Align.left((grid)),
            box=box.ROUNDED,
            border_style="white"
        )

        return message_panel
    
    def right_bottom(self) -> Panel:
        table = Table(box=box.SIMPLE, expand=False, show_header=False, pad_edge=False, padding=(0,0,0,0))
        table.add_row('[bold]Additional Information:[/bold]')
        table.add_row('- If you like the project, please leave a star [bold red]<3[/bold red]')
        table.add_row('- Feel free to [bold red]report[/bold red] bugs or suggest improvements!')
        table.add_row('- Contact me on Telegram! [bold blue]@Xamplee[/bold blue]')

        message_panel = Panel(
            Align.left((table)),
            box=box.ROUNDED, 
            border_style="green",
            title='[link=https://github.com/Xample33/Rainbow-Six-Auto-Renown-Farm bold white]GitHub page here (ctrl + click)[/link]'
        )

        return message_panel

    def update_console(self) -> None:
        self.layout["header"].update(self.header())
        self.layout['main']['left'].update(self.left())
        self.layout["main"]['right']['top'].update(self.right_top())
        self.layout["main"]['right']['bottom'].update(self.right_bottom())
            
        rprint(self.layout)
        sleep(self.UPDATE_DELAY)
