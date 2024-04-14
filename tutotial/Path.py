from pathlib import Path

# Two path
# Absolute path (c:\)
# relative path

path = Path("ecommerce")
print(path.exists())
# check is the file/directory exist

path = Path("emails")
print(path.mkdir())
# make directory

path = Path("emails")
print(path.rmdir())
# remove directory

path = Path()
for file in path.glob("*.py"):
    print(file)
# write down all python file in "" directory
