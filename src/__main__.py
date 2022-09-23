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
# parser.add_argument('')

options = parser.parse_args()

m = app_new.main()

if __name__ == '__main__':
    if options.p:
        progress_bar = True
    else:
        progress_bar = False
    if options.a:
        print('Running All Steps')
        # app.run_all()
        m.run(progress_bar)
    elif options.s1:
        print('s1')
    elif options.s2:
        print('s2')
    elif options.s3:
        # app.run_step_3()
        print('s3')
    elif options.s4:
        print('s4')
    elif options.s5:
        print('s5')
