#!/bin/env python3

from PIL import Image
import math
from django.core.files.uploadedfile import InMemoryUploadedFile, TemporaryUploadedFile
from time import time_ns


def image_processing(
    file: InMemoryUploadedFile | TemporaryUploadedFile,
    allowed_size_threshold: int = 2000,
    allowed_res_threshold: tuple[int] = (1920, 1080),
    allowed_format_list: list[str] = ["webp", "png", "jpg", "jpeg"],
):
    """
    This is the entering point for the image processing to start.
    This function takes these positional args:
    1. `file_path` - Image file absolute path.
    2. `allowed_format_list` - A list of image format that are acceptable.
    3. `allowed_size_threshold` - Maximum size of an image that is acceptable in KB.
    4. `allowed_res_threshold` - Maximum resolution an image can have. Value should be in tuple[int] data type.

    Returs:
    tuple(approval, reason, extension)
    """
    file_size_KB = round(file.size / 1024, 3)
    if allowed_size_threshold < file_size_KB:
        return False, "File size limit exceed!", None
    if "jpg" in allowed_format_list:
        allowed_format_list.append("jpeg")
    allowed_format_list = set(allowed_format_list)
    with Image.open(file) as img:
        img_width, img_height = img.size
        max_width, max_height = allowed_res_threshold
        if img_width > max_width or img_height > max_height:
            return (
                False,
                f"Resolution limit exceed: Max width:{max_width}, Max height: {max_height}!",
                None,
            )
        if img.format.lower() not in allowed_format_list:
            return False, "File format not allowed!", None
        return True, None, img.format.lower()


def image_saver(file: InMemoryUploadedFile | TemporaryUploadedFile, extension: str):
    """
    This function will save the image to the /data/images/ path with "extension" as extension and returns the file name.
    """
    try:
        file_name = f"{time_ns()}.{extension}"
        image_storage_path = "/data/images/"
        with open(f"{image_storage_path}{file_name}", "wb") as img_file:
            if file is TemporaryUploadedFile:
                for chunk in file.chucks():
                    img_file.write(chunk)
            else:
                img_file.write(file.read())
        return True, file_name
    except Exception as error:
        return False, str(error)
