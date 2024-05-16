import psutil
import systemd.journal

perm_space = 5 * 1024 ** 3  # bytes


def get_size(bytes, suffix='B'):
    factor = 1024
    for unit in ['', 'K', 'M', 'G', 'T', 'P']:
        if bytes < factor:
            return f'{bytes:.2f} {unit}{suffix}'
        bytes /= factor


def check_space():
    disk_usage = psutil.disk_usage('/')
    free_space = disk_usage.free

    systemd.journal.send('-' * 40)
    systemd.journal.send('Start function check_space')
    systemd.journal.send(f'Free space = {get_size(free_space)}')
    if free_space < perm_space:
        systemd.journal.send(f'There is less than {get_size(perm_space)} of free disk space left')
    else:
        systemd.journal.send(f'There is more than {get_size(perm_space)} of free disk space left')



if __name__ == '__main__':
    check_space()