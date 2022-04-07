#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import EvalExp as eval

#%% Test des expr
eval1=eval.EvalExp()
print("1 2 + => ",eval1.evaluate("1 2 +"))
eval2=eval.EvalExp()
print("1 2 3 * + => ",eval2.evaluate("1 2 3 * +"))
eval3=eval.EvalExp()
print("1 2 * 3 + => ",eval3.evaluate("1 2 * 3 +"))

print("Réponses :")
eval4=eval.EvalExp()
print("2 3 + => ",eval4.evaluate("2 3 +"))

eval5=eval.EvalExp()
print("1 3 + 2 * => ",eval5.evaluate("1 3 + 2 *"))

eval6=eval.EvalExp()
print("4 3 * 2 5 + + => ",eval6.evaluate("4 3 * 2 5 + +"))
