import importlib.metadata

def main():
    version = importlib.metadata.version('pyRejseplan')
    header = f"""
    ***************************************
    *                                     *
    *          pyRejseplan                *
    *                                     *
    *          Version {version}          *
    *                                     *
    ***************************************
    """
    print(header)

if __name__ == "__main__":
    main()