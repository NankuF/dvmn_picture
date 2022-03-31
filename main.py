import os

from PIL import Image

PIXEL = 50

PATH_TO_AVATARS_DIR = './avatars/'
PATH_TO_MODIFIED_PICTURES_DIR = './modified_pictures/'
PATH_TO_NEED_MODIFIED_DIR = './need_modified/'


def cut_left_and_right(color, size):
    return color.crop(box=(size // 2, 0, color.width - size // 2, color.height))


def shift_picture_left(color, size):
    picture_left = color.crop(box=(size, 0, color.width, color.height))
    picture_middle = cut_left_and_right(color, size)
    return Image.blend(picture_left, picture_middle, alpha=0.3)


def shift_picture_right(color, size):
    picture_right = color.crop(box=(0, 0, color.width - size, color.height))
    picture_middle = cut_left_and_right(color, size)
    return Image.blend(picture_right, picture_middle, alpha=0.3)


def create_modified_picture(picture):
    rgb_image = Image.open(f'{PATH_TO_NEED_MODIFIED_DIR}{picture}')
    red, blue, green = rgb_image.split()

    red_left = shift_picture_left(red, PIXEL)
    blue_right = shift_picture_right(blue, PIXEL)
    green_middle = cut_left_and_right(green, PIXEL)

    new_picture = Image.merge('RGB', (red_left, green_middle, blue_right))
    new_picture.save(f'{PATH_TO_MODIFIED_PICTURES_DIR}new_{picture}')


def create_avatar(picture):
    avatar = Image.open(f'{PATH_TO_MODIFIED_PICTURES_DIR}new_{picture}')
    avatar.thumbnail((80, 80))
    avatar.save(f'{PATH_TO_AVATARS_DIR}avatar_{picture}')


def get_jpg():
    files = os.listdir(f'{PATH_TO_NEED_MODIFIED_DIR}')
    pictures = []
    for file in files:
        img = Image.open(f'{PATH_TO_NEED_MODIFIED_DIR}{file}')
        if img.mode != 'RGB':
            img = img.convert('RGB')
            img.save(file, format='JPEG')
        pictures.append(file)
    return pictures


def main():
    pictures = get_jpg()
    for picture in pictures:
        create_modified_picture(picture)
        create_avatar(picture)


if __name__ == '__main__':
    main()
