def report_formatter(func):
    def wrapper(*args, **kwargs):
        print("\n" + "=" * 50)
        result = func(*args, **kwargs)
        print("=" * 50)
        return result
    return wrapper


class DynamicReport:

    templates = {
        "Business": "Professional Format",
        "Education": "Academic Format",
        "Research": "Scientific Format"
    }

    def __init__(self, title, content, template):
        self.title = title
        self.content = content
        self.template = template

    # Class Method
    @classmethod
    def add_template(cls, name, style):
        cls.templates[name] = style
        print(f"\nNew Template Added -> {name}")

    # Magic Method
    def __str__(self):
        style = self.templates.get(self.template, "Default Format")
        return (
            f"Title      : {self.title}\n"
            f"Content    : {self.content}\n"
            f"Template   : {self.template}\n"
            f"Style      : {style}"
        )

    @report_formatter
    def display(self):
        print(self)


print("Available Templates:")
for t in DynamicReport.templates:
    print("-", t)

choice = input("\nDo you want to add a new template? (yes/no): ").lower()

if choice == "yes":
    name = input("Template Name: ")
    style = input("Template Style: ")
    DynamicReport.add_template(name, style)

print("\nCreate Your Report")

title = input("Enter Report Title: ")
content = input("Enter Report Content: ")
template = input("Choose Template: ")

report = DynamicReport(title, content, template)

report.display()