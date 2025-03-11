"""Rejpseplan CLI application entry point."""

import importlib.metadata


def main():
    """Main function to display the version and a stylized header for the pyRejseplan application.
    This function retrieves the current version of the pyRejseplan package using importlib.metadata,
    constructs a stylized ASCII header with the version information, and prints it to the console."""

    version = importlib.metadata.version('pyRejseplan')
    headline = r"""
####################################################################
#                                                                  #
#                  _____      _          _____  _                  #
#                 |  __ \    (_)        |  __ \| |                 #
#      _ __  _   _| |__) |___ _ ___  ___| |__) | | __ _ _ __       #
#     | '_ \| | | |  _  // _ \ / __|/ _ \  ___/| |/ _` | '_ \      #
#     | |_) | |_| | | \ \  __/ \__ \  __/ |    | | (_| | | | |     #
#     | .__/ \__, |_|  \_\___| |___/\___|_|    |_|\__,_|_| |_|     #
#     | |     __/ |         _/ |                                   #
#     |_|    |___/         |__/                                    #
"""
    border = '#' * 68
    blank = '#' + ' ' * 66 + '#' + '\n'
    version_info = '#' + f'pyRejseplan version: {version}'.center(66) + '#\n'
    header = f'{headline}{blank}{version_info}{border}'
    print(header)


if __name__ == '__main__':
    main()
