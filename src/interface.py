from rich.panel import Panel
from rich.console import Console
from rich.table import Table
from datetime import datetime


class Interface:
    def __init__(self):
        self.console = Console()

    def display_welcome_menu(self):
        current_time = datetime.now()
        date_str = current_time.strftime("%d.%m.%Y")
        time_str = current_time.strftime("%H:%M:%S")

        table = Table(show_header=False, border_style="cyan")
        table.add_column("Key", style="yellow")
        table.add_column("Value", style="green")

        table.add_row("Автор", "QIYANA")
        table.add_row("Форум", "https://lolz.live/kqlol/")
        table.add_row("Используемая модель", "Qwen/Qwen2.5-Coder-0.5B-Instruct")
        table.add_row("Дата", date_str)
        table.add_row("Время запуска", time_str)

        welcome_panel = Panel(
            table,
            title="[bold yellow]🤖 QIYANAChat v1.0[/]",
            subtitle="[italic cyan]Powered by QIYANA[/]",
            border_style="yellow",
            padding=(1, 2)
        )

        self.console.clear()
        self.console.print("\n")
        self.console.print(welcome_panel)
        self.console.print("\n[bold cyan]Команды:[/] [yellow]'exit'[/] - выход, [yellow]'save'[/] - сохранить диалог\n")