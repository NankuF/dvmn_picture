import os

from PIL import Image


def cut_left(color, size):
    return color.crop(box=(size, 0, color.width, color.height))


def cut_right(color, size):
    return color.crop(box=(0, 0, color.width - size, color.height))


def cut_left_and_right(color, size):
    return color.crop(box=(size // 2, 0, color.width - size // 2, color.height))


def shift_picture_left(color, size):
    picture_left = cut_left(color, size)
    picture_middle = cut_left_and_right(color, size)
    return Image.blend(picture_left, picture_middle, alpha=0.3)


def shift_picture_right(color, size):
    picture_right = cut_right(color, size)
    picture_middle = cut_left_and_right(color, size)
    return Image.blend(picture_right, picture_middle, alpha=0.3)


PIXEL = 50


def get_modified_picture(picture):
    """Только jpg картинки"""
    rgb_image = Image.open(f'./need_modified/{picture}')
    red, blue, green = rgb_image.split()

    red_left = shift_picture_left(red, PIXEL)
    blue_right = shift_picture_right(blue, PIXEL)
    green_middle = cut_left_and_right(green, PIXEL)

    new_picture = Image.merge('RGB', (red_left, green_middle, blue_right))
    new_picture.save(f'./modified_pictures/new_{picture}')


def get_avatar(picture):
    """Только jpg картинки"""
    avatar = Image.open(f'./modified_pictures/new_{picture}')
    avatar.thumbnail((80, 80))
    avatar.save(f'./avatars/avatar_{picture}')


def get_jpg():
    files = os.listdir('./need_modified')
    pictures = []
    for file in files:
        if '.jpg' in file:
            pictures.append(file)
    return pictures


def main():
    pictures = get_jpg()
    for picture in pictures:
        get_modified_picture(picture)
        get_avatar(picture)


if __name__ == '__main__':
    main()
