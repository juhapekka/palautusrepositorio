class Project:
    def __init__(self, name, description, dependencies, dev_dependencies, license, authors):
        self.name = name
        self.description = description
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies
        self.license = license
        self.authors = authors

    def _format_list(self, items):
        return "\n- " + "\n- ".join(items) if items else "-"

    @property
    def f_authors(self):
        return self._format_list(self.authors)

    @property
    def f_dep(self):
        return self._format_list(self.dependencies)

    @property
    def f_dev_dep(self):
        return self._format_list(self.dev_dependencies)

    def __str__(self):
        return (
            f"Name: {self.name}"
            f"\nDescription: {self.description}"
            f"\nLicense: {self.license}"
            f"\n\nAuthors:{self.f_authors}"
            f"\n\nDependencies:{self.f_dep}"
            f"\n\nDevelopment dependencies:{self.f_dev_dep}"
        )
