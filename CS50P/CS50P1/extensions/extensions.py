def get_media_type():
    file_name = input("Please enter the file name: ")
    file_extension = file_name.lower().split(".")[-1].strip() if "." in file_name else ""

    if file_extension == "gif":
        print("image/gif")
    elif file_extension in ["jpg", "jpeg"]:
        print("image/jpeg")
    elif file_extension == "png":
        print("image/png")
    elif file_extension in ["pdf", "PDF"]:
        print("application/pdf")
    elif file_extension == "txt":
        print("text/plain")
    elif file_extension == "zip":
        print("application/zip")
    else:
        print("application/octet-stream")

get_media_type()