import os


MOUNT_DIR = '/content/gdrive_dev'
MY_DRIVE = 'MyDrive'
DEV_DIR = 'dev'
BOOK_DIR = 'book'


def path(location:str) -> str:
  return os.path.join(MOUNT_DIR, MY_DRIVE, DEV_DIR, location)


def path_b(location:str) -> str:
  return os.path.join(MOUNT_DIR, MY_DRIVE, BOOK_DIR, location)


def path_nb(location:str='') -> str:
  if location:
    return os.path.join(MOUNT_DIR, MY_DRIVE, DEV_DIR, 'notebooks', location)
  return os.path.join(MOUNT_DIR, MY_DRIVE, DEV_DIR, 'notebooks')


from google.colab import drive
drive.mount(MOUNT_DIR, force_remount=True)


os.listdir(path_nb())
