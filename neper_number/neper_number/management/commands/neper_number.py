import argparse

parser = argparse.ArgumentParser(description='Calculating neper number.')
parser.add_argument('-p', type=int, required=True,
                    help='Number of members in row')

parser.add_argument("-t", "-threads", type=int, default='1',
                    help="Number of threads")

parser.add_argument('-o', '-output', type=str, default='result.txt',
                    help='Name of output file')

parser.add_argument('-q', '-quiet',
                    help='quiet mode')

arguments = parser.parse_args()

members = arguments.p
quiet_mode = arguments.q
output_name = arguments.o
threads = arguments.t


def main():
    print("i am here")
    # for t in range(0, threads):
    #     runprocess()


if __name__ == '__main_':
    main()
