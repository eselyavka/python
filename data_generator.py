"""
Module which generate fake tsv data file.
If --bin argument provided binary data file.

CREATE TABLE test_bin
  (
     hit_date DATE,
     f1       INT,
     f2       SMALLINT,
     f3       TINYINT,
     f4       VARCHAR(5),
     f5       INT,
     f6       BIGINT,
     f7       BIGINT
  );
"""

import argparse
import random
import struct
import string

MEGABYTES = 1000
BATCH_SIZE_MEGABYTES = 100
DEFAULT_OUTPUT_FN = '/tmp/data.tsv'

def data_constructor(is_bin, rnd):
    """
        Construct list with random values

        Args:
            is_bin: flag which indicate binary construction
            rnd: flag which invoke random library
        Returns:
            list: list with random values
    """
    if rnd:
        year = random.randint(2000, 2016)-1900 if is_bin else random.randint(2000, 2016)
        month = "%02d" % (random.randint(1, 12))
        day = "%02d" % (random.randint(1, 31))
        date = int(str(year)+month+day)
        rnd_str = ''.join([random.choice(string.ascii_uppercase +
                                         string.digits)
                           for _ in range(random.randint(1, 5))])
        if is_bin:
            rnd_len = len(rnd_str)

        values = [date,
                  random.randint(1, 100000),
                  random.randint(1, 30000),
                  random.randint(0, 127)]
        if is_bin:
            values.append(rnd_len)
        values.append(rnd_str)
        values.append(random.randint(0, 10000000))
        values.append(random.randint(1, 100000000000))
        values.append(random.randint(1, 200000000000))
    else:
        # use constant data set
        # '2016-08-20    85175   2089    52  IH7FR   2690744 24228276039 177420773741'
        if is_bin:
            values = [1160820,
                      85175,
                      2089,
                      52,
                      5,
                      'IH7FR',
                      2690744,
                      long(24228276039),
                      long(177420773741)]
        else:
            values = ['2016-08-20',
                      85175,
                      2089,
                      52,
                      'IH7FR',
                      2690744,
                      24228276039,
                      177420773741]
    return values

def data_packer(is_bin, rnd):
    """
    Pack data according to format

    Args:
        is_bin: flag which indicate writing to binary file
        rnd: flag which invoke random library
    Returns:
        String: paked data acccording to format

    """
    values = data_constructor(is_bin, rnd)
    if is_bin:
        values.insert(0, 0b00000000)
        values.insert(0, struct.calcsize('<B I I H B H {0}s I Q Q'.format(values[5])))
        s_fmt = struct.Struct("<H B I I H B H {0}s I Q Q".format(values[6]))
        bin_data = s_fmt.pack(*tuple(values))
        return bin_data
    else:
        return '\t'.join(map(str, values)) + '\n'

def data_writer(data_fn, is_bin=False, rnd=False):
    """
        Write random data to file

        Args:
            data_fn: data file name
            is_bin: flag which indicate writing to binary file
        Returns:
            None
    """
    fh = open(data_fn, 'wb' if is_bin else 'w')
    for _ in xrange(MEGABYTES/BATCH_SIZE_MEGABYTES):
        data = [data_packer(is_bin, rnd) for _ in xrange((BATCH_SIZE_MEGABYTES<<20)/39)]
        fh.writelines(data)
    fh.close()

def process_args():
    """
    Handle command line arguments

    Args:
        None
    Returns:
        None
    """
    parser = argparse.ArgumentParser(description='Generate fake ib data file in \
                                                  tsv and binary formats.')
    parser.add_argument('--output-file',
                        default=DEFAULT_OUTPUT_FN,
                        help='filename to write fake data')
    parser.add_argument('--binary',
                        action='store_true',
                        help='flag which indicate writing to binary file')
    parser.add_argument('--rnd',
                        action='store_true',
                        help='flag which invoke random library in data \
                              file generation process')
    propagator_args = parser.parse_args()
    return propagator_args

def main():
    """CLI entry point."""
    cli_args = process_args()
    data_writer(cli_args.output_file,
                cli_args.binary,
                cli_args.rnd)

if __name__ == '__main__':
    main()
