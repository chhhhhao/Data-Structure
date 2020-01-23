import os


def DiskUsage(path):
    total = os.path.getsize(path)
    if os.path.isdir(path):
        for filename in os.listdir(path):
            child = os.path.join(path, filename)
            total += DiskUsage(child)
    print(total, path)
    return total


if __name__ == "__main__":
    DiskUsage(".")

