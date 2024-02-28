"""
Even though Windows and macOS sometimes hide them, most files have file extensions, a suffix that starts with a period (.) at the end of their name. 
For instance, file names for GIFs end with .gif, and file names for JPEGs end with .jpg or .jpeg. 
When you double-click on a file to open it, your computer uses its file extension to determine which program to launch.

Web browsers, by contrast, rely on media types, formerly known as MIME types, to determine how to display files that live on the web. 
When you download a file from a web server, that server sends an HTTP header, along with the file itself, indicating the file's media type. 
For instance, the media type for a GIF is image/gif, and the media type for a JPEG is image/jpeg. 
To determine the media type for a file, a web server typically looks at the file's extension, mapping one to the other.

See developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types/Common_types for common types.

In a file called extensions.py, 
implement a program that prompts the user for the name of a file 
and then outputs that file's media type if the file's name ends, case-insensitively, in any of these suffixes:

    .gif => image/gif
    .jpg => image/gif
    .jpeg => image/gif
    .png => image/gif
    .pdf => application/pdf
    .txt => text/plain
    .zip => application/zip
    all others => application/octet-stream

If the file's name ends with some other suffix or has no suffix at all, output application/octet-stream instead, which is a common default.
"""

def main():
    file = get_file()
    file_suffix = get_file_suffix()
    media_type = assess_media_type(file_suffix)
    print(f"Media type is: ", media_type)


def get_file():
    while True:
        try:
            user_file = input("File name: ").strip().lower()
            if user_file.index(".") > 0:
                return user_file
        except ValueError:
            print("Enter a file name with extension ")


def get_file_suffix(user_file):
    dot_index = user_file.index(".")
    return user_file[dot_index:]



def assess_media_type(suffix):
    match suffix:
        case ".gif" | ".jpg" | ".jpeg" | ".png":
            return "image/gif"
        case ".pdf":
            return "application/pdf"
        case ".txt":
            return "text/plain"
        case ".zip":
            return "application/zip"
        case _:
            return "application/octet-stream"


main()