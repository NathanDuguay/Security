from datetime import datetime
import cmd
import sys
import argparse
from hydra import BruteForce

#difficulty = input("dif")
#password = input("pass")
difficulty = 'fort'
password = 'aC2e5'
start = datetime.now()

Force = BruteForce(password)

if difficulty.lower() == "faible":
    print(Force.faible())
elif difficulty.lower() == "moyen":
    print(Force.moyen())
elif difficulty.lower() == "fort":
    print(Force.fort())

end = datetime.now() - start

print('(hh:mm:ss.ms) {}'.format(end))


