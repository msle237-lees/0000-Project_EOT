from src import app
import argparse

arg_desc = '''\
            0001-Project_EOT
                End of Term Project for CSE 2300-02 - Discrete Structures.
                Author: Michael Lees
            '''

parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter, description=arg_desc)
parser.add_argument("-c", "--code", help="Runs step 1 from the Readme File.", required=False)
args = parser.parse_args()
print(args)

if __name__ == '__main__':
    if args.code == "step1":
        app.run_step_1()
    elif args.code == "step2":
        app.run_step_2()
    elif args.code == "step3":
        app.run_step_3()
    elif args.code == "step4":
        app.run_step_4()
