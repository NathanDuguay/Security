

class BruteForce:
    # liste pour brute force faible
    weak = "abcdefghijklmnopqrstuvwxyz"
    # liste pour brute force moyen
    medium = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    # liste pour brute force fort
    strong = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    # password a trouver
    password = ""
    #password en liste
    check = ['', '', '', '', '']
    #ignorer
    #command_string = ''
    broke = False

    def __init__(self, password):
        self.password = password

    def faible(self):
        test_pass = ''
        self.check = self.weak[0] * len(self.password)
        self.check = list(self.check)
        for i in self.weak:
            self.check[4] = i
            for j in self.weak:
                self.check[3] = j
                for k in self.weak:
                    self.check[2] = k
                    for l in self.weak:
                        self.check[1] = l
                        for char in self.weak:
                            self.check[0] = char
                            test_pass = test_pass.join(self.check)
                            if test_pass == self.password:
                                self.broke = True
                                return self.check
                            else:
                                test_pass = ""

        return self.check

    def moyen(self):
        test_pass = ''
        self.check = self.medium[0] * len(self.password)
        self.check = list(self.check)
        for i in self.medium:
            self.check[4] = i
            for j in self.medium:
                self.check[3] = j
                for k in self.medium:
                    self.check[2] = k
                    for l in self.medium:
                        self.check[1] = l
                        for char in self.medium:
                            self.check[0] = char
                            test_pass = test_pass.join(self.check)
                            if test_pass == self.password:
                                self.broke = True
                                return self.check
                            else:
                                test_pass = ""

        return self.check

    def fort(self):
        test_pass = ''
        self.check = self.strong[0] * len(self.password)
        self.check = list(self.check)
        for i in self.strong:
            self.check[4] = i
            for j in self.strong:
                self.check[3] = j
                for k in self.strong:
                    self.check[2] = k
                    for l in self.strong:
                        self.check[1] = l
                        for char in self.strong:
                            self.check[0] = char
                            test_pass = test_pass.join(self.check)
                            if test_pass == self.password:
                                self.broke = True
                                return self.check
                            else:
                                print(test_pass)
                                test_pass = ""

        return self.check
#   Projet personnel, ignorer
#    def faible(self):
#        test_pass = ''
#        self.check = self.weak[0] * len(self.password)
#        self.check = list(reversed(self.check))
#        increments = 0
#        while not self.broke:
#            if increments != 0:
#                for j in range(increments, 0, -1):
#                    exec(self.standard_line(j))
#                exec(self.last_line())
#            else:
#                exec(str(self.last_line()))
#            increments += 1
#        return self.check
#
#    def standard_line(self, index):
#       standard_command_line = 'for letter in self.weak:\n' \
#                                'self.check['+index+'] = letter\n'
#        return standard_command_line
#
#    def last_line(self):
#        last_command_line = 'for char in self.weak:\n' \
#                            '   self.check[0] = char\n' \
#                            '   test_pass = test_pass.join(reversed(self.check))\n' \
#                            '   if test_pass == self.password:\n' \
#                            '       broke = True\n' \
#                            '       return self.check\n' \
#                            '   else:\n' \
#                            '       test_pass = "" '
#        return last_command_line
