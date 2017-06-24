import math
import datetime

from multiprocessing import Process, Queue
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = """Calculates the neper number"""

    def print(self, obj):
        self.stdout.write(str(obj))

    def add_arguments(self, parser):
        parser.add_argument('-p', type=int,
                            help='Number of members in row')

        parser.add_argument("-t", "-threads", type=int, default='1',
                            help="Number of threads")

        parser.add_argument('-o', '-output', type=str, default='result.txt',
                            help='Name of output file')

        parser.add_argument('-q', '-quiet', type=str, default='False',
                            help='quiet mode')

    def generate_work_per_thread(self, members, threads):
        list_of_work = {i: list() for i in range(threads)}
        for k in range(members):
            thread = k % threads
            list_of_work[thread].append(k)

        '''
        In order every thread to have equal work to do with another one.
        For 6 threads and 100 memebrs we will have:
        {
            0: [0, 6, 12, 18, 24, 30, 36, 42, 48, 54, 60, 66, 72, 78, 84, 90, 96],
            1: [1, 7, 13, 19, 25, 31, 37, 43, 49, 55, 61, 67, 73, 79, 85, 91, 97],
            2: [2, 8, 14, 20, 26, 32, 38, 44, 50, 56, 62, 68, 74, 80, 86, 92, 98],
            3: [3, 9, 15, 21, 27, 33, 39, 45, 51, 57, 63, 69, 75, 81, 87, 93, 99],
            4: [4, 10, 16, 22, 28, 34, 40, 46, 52, 58, 64, 70, 76, 82, 88, 94],
            5: [5, 11, 17, 23, 29, 35, 41, 47, 53, 59, 65, 71, 77, 83, 89, 95]
        }
        '''
        return list_of_work

    def calculate_row_sum(self, members, threads):
        res = Queue()

        def calculate_member(k, res):
            print(" k is {}".format(k))
            member_res = ((3 * k) * (3 * k) + 1) / math.factorial(3 * k)
            res.put(member_res)
            print(" res is {}".format(res))

            print("member is {}".format(member_res))

        separated_work = self.generate_work_per_thread(members, threads)

        for t in separated_work:
            for k in separated_work[t]:
                p = Process(target=calculate_member,
                            args=(k, res))
                p.start()
            print("Thread {} started".format(t))

        neper_number = sum([res.get() for _ in range(0, members)])
        print("Neper number is {}".format(neper_number))

    def handle(self, *args, **options):
        members = options.get('p')
        threads = options.get('t')
        output_name = options.get('o')
        quiet_mode = options.get('q')

        start_time = datetime.datetime.now()
        stringed_start_time = start_time.time().isoformat()
        print("Executing start time is {}".format(stringed_start_time))

        result = self.calculate_row_sum(members, threads)

        end_time = datetime.datetime.now()
        stringed_end_time = end_time.time().isoformat()

        print("Executing end time is {}".format(stringed_end_time))

        time_taken = (end_time - start_time).total_seconds()

        print("Total executing time is {}".format(time_taken))
        print("result is {}".format(result))

        print(" {} members, {} threads, {} output_name, {}queet mode".format(members, threads, output_name, quiet_mode))
        print("here we implement the algorithm")
