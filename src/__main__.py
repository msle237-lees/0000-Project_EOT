from src import app_new
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-a', help='Run all steps', action='store_true')
parser.add_argument('-s1', help='Run only Step 1', action='store_true')
parser.add_argument('-s2', help='Run only Step 2', action='store_true')
parser.add_argument('-s3', help='Run only Step 3', action='store_true')
parser.add_argument('-s4', help='Run only Step 4', action='store_true')
parser.add_argument('-s5', help='Run only Step 5', action='store_true')
parser.add_argument('-p', help='Enable or Disable Progress Bar Updates', action='store_true')
parser.add_argument('-s', help='Save Data within text file', action='store_true')
parser.add_argument('-l', help='Enable or Disable Logging', action='store_true')

options = parser.parse_args()

m = app_new.main()

if __name__ == '__main__':
    if options.a:
        print('Running All Steps')
        m.run(options.p, options.s, options.l)
    elif options.s1:
        print('Running Step 1')
        m.step_1()
    elif options.s2:
        print('Running Step 2')
        m.step_2()
    elif options.s3:
        print('Running Step 3')
        m.step_3()
    elif options.s4:
        print('Running Step 4')
        m.step_4()
    elif options.s5:
        print('Running Step 5')
        m.step_5()
