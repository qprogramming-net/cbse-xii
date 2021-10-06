# User Libraries

In this section, we will learn how to create our own libraries and their respective documentation

## Libraries and Packages

A package is a collection of modules while a library is a collection of one or more packages or subpackages

We will be focusing on creating our own **packages**

## Structure of a Package

Each package contains an `__init__.py` file which contains commands to execute when the package is loaded in a program.

Folders without `__init__.py` files are not categorized as packages.

The file tree of a package is as follows:

- Folder
  - `file.py`
  - Package
    - `__init.py__`
    - `module1.py`
    - `module2.py`
    - Subpackage
      - `__init__.py`
      - `module3.py`

## How to make a package

1. The first step is to identify what the package is for and name it accordingly. The name should be representative of the package's purpose.

   Remember, you must separate words in the names of folders and subfolders either by using camel case (FirstSecond) or underscores (first_second). While creating modules, it is advised to separate words by underscores.

2. Now, you must make your subpackage directories (if required). Use the same naming conventions as the package directory.

3. Make `__init__.py` files for each package and subpackage directory

4. Find the path of the directory in which your Python packages have been installed (`site-packages`).

   You can do so with the following code:

   ```python
   import sys
   for item in sys.path:
       if "site-packages" in item:
           print(item)
           break
   ```

   This will output the path to your `site-packages` directory.

   Now, copy the path and enter it into your file explorer.

5. Once you have opened the path, in another window, copy the folder with your package and paste in the `site-packages` directory.

## Documentation



