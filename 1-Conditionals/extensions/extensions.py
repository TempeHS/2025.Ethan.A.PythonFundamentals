def main():
    x = input("input file ").strip()
    if x.endswith("gif"):
        print("image/gif")
    elif x.endswith("jpg" or "jpeg"):
        print("image/jpg")
    elif x.endswith("png"):
        print("image/png")
    elif x.endswith("pdf"):
        print("document/pdf")
    elif x.endswith("txt"):
        print("document/txt")
    elif x.endswith("zip"):
        print("file/zip")
    else:
        print("application/octet-stream")


main()
