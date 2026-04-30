from typing import Dict, List, Optional, Union, TypeAlias

DirContent: TypeAlias = List[str]
SubDirs: TypeAlias = List[Dict]
RepoStructure: TypeAlias = Dict[str, Union[str, DirContent, SubDirs]]


class RepositoryScanner:
    def __init__(self, repository: RepoStructure) -> None:
        self._validatioon_structure(repository)
        self.repository = repository
    
    def _validatioon_structure(self, directory: RepoStructure) -> None:
        if not isinstance(directory, dict):
            raise TypeError("Expected: directory is RepoStructure")
        
        stack_of_dirs = [[directory]]
        while stack_of_dirs:
            curr_dir = stack_of_dirs.pop()
            for dir in curr_dir:
                if not isinstance(dir, dict):
                    raise TypeError("Expected: directory is RepoStructure")
                if  dir.get("name") is None or dir.get("files") is None or dir.get("dirs") is None:
                    raise ValueError("Expected: primary keys of 'name', 'files' and 'dirs' in structure")
                if not isinstance(dir["files"], list) or not isinstance(dir["dirs"], list):
                    raise TypeError("Expected: 'files' and 'dirs' are lists")
                stack_of_dirs.append(dir["dirs"])

    def find_python_files_recursive(
        self,
        directory: Optional[RepoStructure] = None,
        current_path: str = ""
    ) -> List[str]:
        if directory is None:
            directory = [self.repository]
        
        curr_dir = []
        for dir in directory:
            current_path_ = f'{current_path}/{dir['name']}'
            for file in dir["files"]:
                if file.endswith(".py"):
                    curr_dir.append(f'{current_path_}/{file}')
            curr_dir.extend(self.find_python_files_recursive(dir["dirs"], current_path_))
        
        return sorted(curr_dir)


    def find_python_files_non_recursive(self) -> List[str]:
        stack = [(self.repository, "")]

        result = []
        while stack:
            curr_dir, current_path = stack.pop()

            dir_name = curr_dir["name"]
            new_path = f"{current_path}/{dir_name}" if current_path else f"/{dir_name}"
            

            for file in curr_dir["files"]:
                if file.endswith(".py"):
                    result.append(f"{new_path}/{file}")
                    
            for sub_dir in curr_dir["dirs"]:
                stack.append((sub_dir, new_path))
                
        return sorted(result)


if __name__ == "__main__":
    repository = {
        "name": "legacy_project",
        "files": ["readme.md", "requirements.txt", "main.py"],
        "dirs": [
            {
                "name": "src",
                "files": ["__init__.py", "helpers.py"],
                "dirs": [
                    {
                        "name": "utils",
                        "files": ["database.py", "config.yaml"],
                        "dirs": []
                    }
                ]
            },
            {
                "name": "tests",
                "files": ["test_main.py", "conftest.py"],
                "dirs": []
            }
        ]
    }

    repo = RepositoryScanner(repository)
    print(*repo.find_python_files_non_recursive(), sep='\n')
