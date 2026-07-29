from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.enums import TA_CENTER
from styles import title_style, TITLE, BODY
from reportlab.platypus import Paragraph


def styles():
    story = []
    styles = getSampleStyleSheet()
    title_style.alignment = TA_CENTER

    SUCCESS = "\033[92m"
    WARNING = "\033[91m"
    ERROR = "\033[93m"
    RESET = "\033[0m"

    story.append(
        Paragraph("Operations Analysis", TITLE)
    )

    story.append(
        Paragraph("This report summarises...", BODY)
    )
    print(f"{SUCCESS}Document uploaded{RESET}")
    return styles, WARNING, ERROR


def main():
    styles()


if __name__ == "__main__":
    main()
