import os

from PIL import Image

PIXEL = 50

PATH_TO_AVATARS_DIR = './avatars/'
PATH_TO_MODIFIED_PICTURES_DIR = './modified_pictures/'
PATH_TO_NEED_MODIFIED_DIR = './need_modified/'


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
            img.save(f'{PATH_TO_NEED_MODIFIED_DIR}{file}', format='JPEG')
        pictures.append(file)
    return pictures


def main():
    pictures = get_jpg()
    for picture in pictures:
        rgb_image = Image.open(f'{PATH_TO_NEED_MODIFIED_DIR}{picture}')
        red, blue, green = rgb_image.split()

        red_picture_left = red.crop(box=(PIXEL, 0, red.width, red.height))
        red_picture_middle = red.crop(box=(PIXEL // 2, 0, red.width - PIXEL // 2, red.height))
        red_new = Image.blend(red_picture_left, red_picture_middle, alpha=0.3)

        blue_picture_right = blue.crop(box=(0, 0, blue.width - PIXEL, blue.height))
        blue_picture_middle = blue.crop(box=(PIXEL // 2, 0, blue.width - PIXEL // 2, blue.height))
        blue_new = Image.blend(blue_picture_right, blue_picture_middle, alpha=0.3)

        green_middle = green.crop(box=(PIXEL // 2, 0, green.width - PIXEL // 2, green.height))

        new_picture = Image.merge('RGB', (red_new, green_middle, blue_new))
        new_picture.save(f'{PATH_TO_MODIFIED_PICTURES_DIR}new_{picture}')
        create_avatar(picture)


if __name__ == '__main__':
    main()
