#!/bin/env python3

from PIL import Image
import math
import os


def image_processing(
    file_path: str,
    allowed_size_threshold: int,
    allowed_res_threshold: tuple[int],
    allowed_format_list: list[str] = ["webp", "png", "jpg", "jpeg"],
):
    """
    This is the entering point for the image processing to start.
    This function takes these positional args:
    1. `file_path` - Image file absolute path.
    2. `allowed_format_list` - A list of image format that are acceptable.
    3. `allowed_size_threshold` - Maximum size of an image that is acceptable in KB.
    4. `allowed_res_threshold` - Maximum resolution an image can have. Value should be in tuple[int] data type.
    """
    file_size_KB = round(os.path.getsize(file_path) / 1024, 3)
    if allowed_size_threshold < file_size_KB:
        return False, "File size limit exceed!"
    if "jpg" in allowed_format_list:
        allowed_format_list.append("jpeg")
    allowed_format_list = set(allowed_format_list)
    with Image.open(file_path) as img:
        img_width, img_height = img.size
        max_width, max_height = allowed_res_threshold
        if img_width > max_width or img_height > max_height:
            return (
                False,
                f"Resolution limit exceed: Max width:{max_width}, Max height: {max_height}!",
            )
        if img.format.lower() not in allowed_format_list:
            return False, "File format not allowed!"
        return True, None
